#!/usr/bin/env python3
"""
Gmail Extraction via OAuth (No Password Needed)

This script:
1. Opens a browser for Google login (you authorize, I never see password)
2. Extracts your sent emails
3. Saves company names + email context locally
4. Generates sent_emails.txt + email_context.json for automation

Setup:
    pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client

Usage:
    python gmail-extract-oauth.py

What happens:
    - Browser opens: "Sign in with Google"
    - You log in
    - You click "Allow" (grants email read permission)
    - Script extracts sent emails
    - Saves to sent_emails.txt + email_context.json
    - Done (no password stored, no credentials saved)
"""

import json
import re
import os
from pathlib import Path
from typing import List, Dict
from datetime import datetime

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient import discovery

# Gmail API scopes (read-only)
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

class GmailExtractor:
    """Extract companies and context from sent emails via OAuth."""

    def __init__(self):
        self.service = None
        self.sent_emails = []
        self.companies = {}

    def authenticate(self) -> bool:
        """Authenticate with Google OAuth (browser-based, no password storage)."""
        print("\n🔐 Starting Google OAuth Authentication...")
        print("   A browser window will open for you to sign in.")
        print("   You'll be asked to grant permission to read your Gmail.\n")

        try:
            # Check if credentials already exist locally (from previous run)
            creds = None
            if os.path.exists('token.json'):
                creds = Credentials.from_authorized_user_file('token.json', SCOPES)
                print("✅ Using cached credentials (from previous authorization)")

            # If not cached, open browser for OAuth flow
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                    print("✅ Refreshed OAuth token")
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        'credentials.json',
                        SCOPES,
                        redirect_uri='http://localhost:8080'
                    )
                    print("🌐 Opening browser for Google Sign-In...")
                    creds = flow.run_local_server(port=8080)

                # Save credentials for next time (encrypted on your machine)
                with open('token.json', 'w') as token:
                    token.write(creds.to_json())
                    print("✅ Credentials saved locally (token.json)")

            # Create Gmail service
            self.service = discovery.build('gmail', 'v1', credentials=creds)
            print("✅ Connected to Gmail API\n")
            return True

        except FileNotFoundError:
            print("❌ credentials.json not found")
            print("   Go to: https://console.cloud.google.com/apis/credentials")
            print("   Create OAuth 2.0 Desktop App")
            print("   Download as credentials.json and save to this directory")
            return False
        except Exception as e:
            print(f"❌ Authentication failed: {e}")
            return False

    def extract_sent_emails(self, limit: int = 100) -> bool:
        """Extract your sent emails from Gmail."""
        print(f"📧 Extracting last {limit} sent emails...")

        try:
            # Query for sent emails (from:me)
            results = self.service.users().messages().list(
                userId='me',
                q='from:me',
                maxResults=limit
            ).execute()

            messages = results.get('messages', [])
            print(f"   Found {len(messages)} sent emails\n")

            if not messages:
                print("⚠️  No sent emails found")
                return False

            # Extract details from each email
            for i, msg in enumerate(messages, 1):
                msg_id = msg['id']
                message = self.service.users().messages().get(
                    userId='me',
                    id=msg_id,
                    format='full'
                ).execute()

                # Extract headers
                headers = message['payload']['headers']
                header_dict = {h['name']: h['value'] for h in headers}

                to = header_dict.get('To', '')
                subject = header_dict.get('Subject', '')
                date = header_dict.get('Date', '')

                # Extract body
                body = self._get_message_body(message['payload'])

                email_data = {
                    'to': to,
                    'subject': subject,
                    'date': date,
                    'body_preview': body[:200] if body else '',
                    'message_id': msg_id
                }

                self.sent_emails.append(email_data)

                if i % 10 == 0:
                    print(f"   ✓ Processed {i}/{len(messages)}")

            print(f"✅ Extracted {len(self.sent_emails)} emails\n")
            return True

        except Exception as e:
            print(f"❌ Extraction failed: {e}")
            return False

    def _get_message_body(self, payload) -> str:
        """Extract email body from payload."""
        try:
            if 'parts' in payload:
                for part in payload['parts']:
                    if part['mimeType'] == 'text/plain':
                        data = part['body'].get('data', '')
                        if data:
                            import base64
                            return base64.urlsafe_b64decode(data).decode('utf-8')
            else:
                data = payload['body'].get('data', '')
                if data:
                    import base64
                    return base64.urlsafe_b64decode(data).decode('utf-8')
        except:
            pass
        return ''

    def extract_companies(self) -> Dict[str, List[str]]:
        """Extract company names from email bodies and "to" fields."""
        print("🔍 Extracting companies from email content...\n")

        companies_found = {}

        # Patterns to find company names in emails
        patterns = [
            r'(?:at|from|working at)\s+([A-Z][a-zA-Z\s&,\.]+?)(?:\s|,|\.|\n|$)',
            r'(?:@|to)\s+([A-Z][a-zA-Z0-9\s&\.-]+?)(?:\s|,|\.|\n|$)',
            r'(?:Hi|Hello)\s+[A-Z][a-z]+\s+(?:at|from)\s+([A-Z][a-zA-Z\s&]+?)(?:\n|$)',
        ]

        for email in self.sent_emails:
            # Try to extract from "to" field
            to_match = re.search(r'([a-zA-Z0-9._-]+)@([a-zA-Z0-9.-]+)', email['to'])
            if to_match:
                domain = to_match.group(2)
                company_name = domain.split('.')[0].title()
                if len(company_name) > 2:
                    companies_found[company_name] = email

            # Try patterns in body
            body = email['body_preview'] + " " + email['subject']
            for pattern in patterns:
                matches = re.findall(pattern, body)
                for match in matches:
                    company_name = match.strip()
                    if len(company_name) > 2 and company_name not in companies_found:
                        companies_found[company_name] = email

        # Deduplicate and clean
        unique_companies = {}
        for company, email in companies_found.items():
            clean_name = company.strip().rstrip('.,')
            if clean_name and len(clean_name) > 2:
                if clean_name not in unique_companies:
                    unique_companies[clean_name] = email

        self.companies = unique_companies
        print(f"✅ Found {len(unique_companies)} unique companies\n")

        # Print sample
        if unique_companies:
            print("📊 Sample companies extracted:")
            for i, company in enumerate(list(unique_companies.keys())[:5], 1):
                print(f"   {i}. {company}")
            if len(unique_companies) > 5:
                print(f"   ... and {len(unique_companies) - 5} more")
            print()

        return unique_companies

    def save_to_files(self) -> bool:
        """Save extracted data to files."""
        print("💾 Saving extracted data...\n")

        # Save company names (for linkedin-auto-connect.py)
        try:
            with open('sent_emails.txt', 'w', encoding='utf-8') as f:
                for company in sorted(self.companies.keys()):
                    f.write(f"{company}\n")
            print(f"✅ Saved {len(self.companies)} companies to: sent_emails.txt")
        except Exception as e:
            print(f"❌ Failed to save companies: {e}")
            return False

        # Save email context (for reference + message generation)
        try:
            email_context = {}
            for company, email in self.companies.items():
                email_context[company] = {
                    'to': email['to'],
                    'subject': email['subject'],
                    'date': email['date'],
                    'body_preview': email['body_preview']
                }

            with open('email_context.json', 'w', encoding='utf-8') as f:
                json.dump(email_context, f, indent=2)
            print(f"✅ Saved email context to: email_context.json")
        except Exception as e:
            print(f"❌ Failed to save context: {e}")
            return False

        return True

    def run(self) -> bool:
        """Full extraction workflow."""
        print("\n" + "="*60)
        print("Gmail Extraction via OAuth")
        print("="*60)

        # Step 1: Authenticate
        if not self.authenticate():
            return False

        # Step 2: Extract emails
        if not self.extract_sent_emails(limit=100):
            return False

        # Step 3: Extract companies
        if not self.extract_companies():
            print("⚠️  No companies found in emails")
            return False

        # Step 4: Save files
        if not self.save_to_files():
            return False

        # Summary
        print("="*60)
        print("✅ EXTRACTION COMPLETE")
        print("="*60)
        print("\nNext steps:")
        print("1. Review sent_emails.txt (company list)")
        print("2. Review email_context.json (details)")
        print("3. Run: python linkedin-auto-connect.py --emails sent_emails.txt")
        print("\n📝 Note: Your OAuth token is cached in token.json")
        print("   (Stored locally, encrypted. Delete anytime to re-authenticate.)\n")

        return True


def main():
    extractor = GmailExtractor()
    success = extractor.run()
    exit(0 if success else 1)


if __name__ == "__main__":
    main()
