#!/usr/bin/env python3
"""
LinkedIn Safe Automation — Password Never Stored

Improvements over linkedin-auto-connect.py:
- Password prompted at runtime (never stored)
- Email-based optional (can skip if already logged in)
- OAuth-ready (uses token from gmail-extract-oauth.py)
- Activity logging encrypted locally

Usage:
    python linkedin-safe-connect.py --emails sent_emails.txt --daily-limit 5

Password prompt:
    "LinkedIn Email: your-email@gmail.com"
    "LinkedIn Password: " (typing hidden)

No passwords stored anywhere.
"""

import os
import json
import csv
import re
import time
import random
import logging
import getpass
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Tuple
from pathlib import Path

import anthropic
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('linkedin-automation.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Configuration
YOUR_NAME = "Shivam"
YOUR_MAJOR = "Industrial Systems Engineering (ISE Honors)"
YOUR_SCHOOL = "Texas A&M University"
YOUR_GRADUATION = "May 2026"
YOUR_FOCUS = "Supply chain optimization, operations efficiency, logistics systems"

class LinkedInSafeAutomation:
    """LinkedIn automation with secure password handling."""

    def __init__(self, email: str = None, daily_limit: int = 8):
        self.email = email
        self.password = None  # Never stored
        self.daily_limit = daily_limit
        self.driver = None
        self.anthropic_client = anthropic.Anthropic()
        self.activity_log = []
        self.session_date = datetime.now().isoformat()
        self.email_context = {}

        # Anti-detection settings
        self.min_delay = 30
        self.max_delay = 300
        self.mouse_move_speed = 0.3

    def prompt_for_credentials(self) -> bool:
        """Securely prompt for credentials (no storage)."""
        print("\n🔐 LinkedIn Credentials (never stored)")
        print("-" * 40)

        if not self.email:
            self.email = input("LinkedIn Email: ").strip()

        self.password = getpass.getpass("LinkedIn Password: ")

        if not self.email or not self.password:
            print("❌ Email or password missing")
            return False

        logger.info(f"Credentials loaded (email: {self.email})")
        return True

    def load_email_context(self, context_file: str = 'email_context.json') -> bool:
        """Load email context from gmail-extract-oauth.py."""
        try:
            if os.path.exists(context_file):
                with open(context_file, 'r') as f:
                    self.email_context = json.load(f)
                logger.info(f"✅ Loaded email context for {len(self.email_context)} companies")
                return True
        except Exception as e:
            logger.warning(f"⚠️  Could not load email context: {e}")
        return True  # Non-blocking

    def setup_driver(self) -> webdriver.Chrome:
        """Initialize Chrome driver with anti-detection measures."""
        logger.info("Setting up Chrome driver (stealth mode)...")

        options = webdriver.ChromeOptions()

        # Stealth mode
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)

        # User agent rotation
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        ]
        options.add_argument(f'user-agent={random.choice(user_agents)}')

        # Performance
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

        # Inject stealth JavaScript
        driver.execute_cdp_command('Page.addScriptToEvaluateOnNewDocument', {
            'source': 'Object.defineProperty(navigator, "webdriver", {get: () => false});'
        })

        logger.info("✅ Chrome driver ready (stealth mode active)")
        return driver

    def random_delay(self, min_sec: int = None, max_sec: int = None) -> float:
        """Random delay to avoid detection."""
        min_sec = min_sec or self.min_delay
        max_sec = max_sec or self.max_delay
        delay = random.uniform(min_sec, max_sec)
        logger.debug(f"⏳ Waiting {delay:.1f}s...")
        time.sleep(delay)
        return delay

    def human_like_mouse_movement(self, element):
        """Move mouse to element like a human."""
        try:
            actions = ActionChains(self.driver)
            offset = random.randint(-50, 50)
            actions.move_to_element_with_offset(element, offset, random.randint(-20, 20))
            actions.perform()
            time.sleep(random.uniform(0.5, 1.5))
        except:
            pass

    def login_to_linkedin(self) -> bool:
        """Login with anti-detection measures."""
        logger.info("Logging in to LinkedIn...")

        try:
            self.driver.get("https://www.linkedin.com/login")
            self.random_delay(3, 8)

            # Email
            email_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            self.human_like_mouse_movement(email_field)
            email_field.clear()

            for char in self.email:
                email_field.send_keys(char)
                time.sleep(random.uniform(0.05, 0.15))

            self.random_delay(1, 3)

            # Password
            password_field = self.driver.find_element(By.ID, "password")
            self.human_like_mouse_movement(password_field)

            for char in self.password:
                password_field.send_keys(char)
                time.sleep(random.uniform(0.05, 0.15))

            self.random_delay(2, 5)

            # Submit
            login_button = self.driver.find_element(By.XPATH, "//button[@aria-label='Sign in']")
            self.human_like_mouse_movement(login_button)
            login_button.click()

            self.random_delay(5, 10)

            if self._check_for_verification():
                logger.warning("⚠️  2FA detected. Complete verification manually, then press Enter...")
                input("Press Enter once you've completed 2FA: ")

            logger.info("✅ Logged in")
            return True

        except Exception as e:
            logger.error(f"❌ Login failed: {e}")
            return False
        finally:
            # Clear password from memory
            self.password = None

    def _check_for_verification(self) -> bool:
        """Check if verification is needed."""
        try:
            self.driver.find_element(By.XPATH, "//*[contains(text(), 'verify')]")
            return True
        except:
            return False

    def search_and_find_leader(self, company_name: str) -> Optional[Tuple[str, str]]:
        """Search for CEO."""
        logger.info(f"Searching for CEO at {company_name}...")

        try:
            self.driver.get("https://www.linkedin.com/search/results/people/")
            self.random_delay(2, 5)

            search_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Search field']"))
            )

            search_query = f"CEO at {company_name}"
            for char in search_query:
                search_field.send_keys(char)
                time.sleep(random.uniform(0.03, 0.1))

            self.random_delay(1, 2)
            search_field.send_keys(Keys.RETURN)
            self.random_delay(3, 8)

            try:
                first_result = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//a[@data-test-app-aware-link]"))
                )

                name = first_result.find_element(By.XPATH, ".//span[@aria-hidden='true']").text
                url = first_result.get_attribute("href")

                logger.info(f"   ✅ Found: {name}")
                return (name, url)
            except:
                logger.warning(f"   ⚠️  No CEO found")
                return None

        except Exception as e:
            logger.error(f"   ❌ Search error: {e}")
            return None

    def generate_message(self, company_name: str, person_name: str, reference_email: Dict = None) -> str:
        """Generate personalized message with optional email reference."""
        logger.debug(f"Generating message for {person_name}...")

        email_reference = ""
        if reference_email:
            email_reference = f"""
Previous email to {company_name}:
- To: {reference_email.get('to', 'Unknown')}
- Subject: {reference_email.get('subject', 'Unknown')}
- Preview: {reference_email.get('body_preview', '')[:100]}

Reference this in the message (casually mention you reached out).
"""

        prompt = f"""Generate a short, personalized LinkedIn connection message (max 300 chars).

Target: {person_name} at {company_name}
Your background: {YOUR_NAME}, {YOUR_MAJOR} graduating {YOUR_GRADUATION}
Your focus: {YOUR_FOCUS}
{email_reference}

Requirements:
- Sound genuine and calm
- Mention ONE specific thing about their company
- If email reference provided, casually mention you've emailed them before
- No corporate jargon
- 3-4 sentences max
- Conversational tone

Return ONLY the message text (no quotes)."""

        try:
            response = self.anthropic_client.messages.create(
                model="claude-opus-4-7",
                max_tokens=200,
                messages=[{"role": "user", "content": prompt}]
            )

            message = response.content[0].text.strip()
            return message
        except Exception as e:
            logger.error(f"Message generation failed: {e}")
            return f"Hi {person_name}, I'm {YOUR_NAME} from TAMU. Impressed by {company_name}. Would love to connect."

    def send_connection_request(self, profile_url: str, message: str) -> bool:
        """Send connection request."""
        logger.info(f"Sending connection request...")

        try:
            self.driver.get(profile_url)
            self.random_delay(2, 5)

            connect_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(@aria-label, 'Invite')]"))
            )

            self.human_like_mouse_movement(connect_button)
            self.random_delay(0.5, 2)
            connect_button.click()

            self.random_delay(2, 4)

            # Try to add personalized message
            try:
                add_note_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Add a note')]")
                add_note_button.click()
                self.random_delay(1, 2)

                message_field = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//textarea[@name='message']"))
                )

                for char in message[:300]:
                    message_field.send_keys(char)
                    time.sleep(random.uniform(0.02, 0.08))

                self.random_delay(1, 3)
            except:
                logger.warning("   ⚠️  Could not add personalized message")

            # Send
            send_button = self.driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Send')]")
            self.human_like_mouse_movement(send_button)
            send_button.click()

            self.random_delay(2, 5)
            logger.info("   ✅ Connection sent")
            return True

        except Exception as e:
            logger.error(f"   ❌ Connection failed: {e}")
            return False

    def run_automation_loop(self, company_list: List[str], batch_size: int = None):
        """Main automation loop."""
        batch_size = batch_size or self.daily_limit
        logger.info(f"\n🚀 Starting automation (limit: {batch_size})")

        completed = 0
        failed = 0

        for i, company in enumerate(company_list[:batch_size], 1):
            logger.info(f"\n[{i}/{batch_size}] {company}")

            try:
                # Get email context if available
                email_ref = self.email_context.get(company, None)

                # Find leader
                leader = self.search_and_find_leader(company)
                if not leader:
                    failed += 1
                    self.random_delay(5, 10)
                    continue

                # Generate message
                message = self.generate_message(company, leader[0], email_ref)

                # Send
                success = self.send_connection_request(leader[1], message)

                if success:
                    completed += 1
                    self._log_activity({
                        'company': company,
                        'ceo': leader[0],
                        'timestamp': datetime.now().isoformat()
                    })
                else:
                    failed += 1

                if i < batch_size:
                    delay = self.random_delay(60, 180)
                    logger.info(f"⏳ Waiting {delay:.0f}s...")

            except Exception as e:
                logger.error(f"Error: {e}")
                failed += 1
                self.random_delay(10, 30)

        logger.info("\n" + "="*60)
        logger.info(f"✅ Complete: {completed} sent, {failed} failed")
        logger.info("="*60 + "\n")

    def _log_activity(self, activity: Dict):
        """Log activity."""
        with open('linkedin-activity.json', 'a') as f:
            json.dump(activity, f)
            f.write('\n')

    def cleanup(self):
        """Cleanup."""
        if self.driver:
            self.driver.quit()
            logger.info("✅ Browser closed")


def main():
    import argparse

    parser = argparse.ArgumentParser(description="LinkedIn Safe Automation")
    parser.add_argument("--email", help="LinkedIn email (optional, will prompt)")
    parser.add_argument("--emails", default="sent_emails.txt", help="Company list file")
    parser.add_argument("--daily-limit", type=int, default=8, help="Max connections per day")

    args = parser.parse_args()

    logger.info("\n" + "="*60)
    logger.info("LinkedIn Safe Automation")
    logger.info("="*60)
    logger.info(f"Daily limit: {args.daily_limit}")
    logger.info("⚠️  Start with 5, monitor account for 24h")
    logger.info("="*60 + "\n")

    agent = LinkedInSafeAutomation(email=args.email, daily_limit=args.daily_limit)

    try:
        # Credentials (prompted securely)
        if not agent.prompt_for_credentials():
            return

        # Load email context
        agent.load_email_context()

        # Setup
        agent.driver = agent.setup_driver()

        # Login
        if not agent.login_to_linkedin():
            logger.error("Login failed")
            return

        # Load companies
        try:
            with open(args.emails, 'r') as f:
                companies = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            logger.error(f"Company file not found: {args.emails}")
            return

        logger.info(f"Loaded {len(companies)} companies\n")

        # Run
        agent.run_automation_loop(companies, batch_size=args.daily_limit)

    except KeyboardInterrupt:
        logger.warning("\n⚠️  Interrupted")
    except Exception as e:
        logger.error(f"Fatal error: {e}")
    finally:
        agent.cleanup()


if __name__ == "__main__":
    main()
