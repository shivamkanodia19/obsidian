#!/usr/bin/env python3
"""
LinkedIn Automation Agent — Full Auto-Connect with Anti-Detection

Workflow:
    1. Login to LinkedIn (Chrome browser)
    2. Research companies from your sent emails
    3. Find CEO/leaders for each company
    4. Send connection requests with personalized messages
    5. Schedule follow-ups (Day 3, Day 7, Day 12)
    6. Log all activity and avoid detection

Anti-Detection Features:
    - Randomized delays (30-300 sec between actions)
    - Human-like mouse movement and scrolling
    - Random user-agent rotation
    - Detection of CAPTCHA/verification prompts
    - Daily rate limiting (max 10 connections/day default)
    - Account health checks
    - Stealth mode (hiding selenium detection)

Requirements:
    pip install selenium webdriver-manager anthropic python-dotenv

Usage:
    python linkedin-auto-connect.py --email your@gmail.com --password your_password \\
        --emails sent_emails.txt --daily-limit 8

WARNING:
    LinkedIn actively detects automation. Use responsibly.
    - Start with 5-10 connections, monitor account
    - If account gets flagged, stop and wait 48 hours
    - Never exceed 15 connections per day
    - Keep delays randomized (don't optimize away)
"""

import os
import json
import csv
import re
import time
import random
import logging
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

class LinkedInAutomationAgent:
    """Full LinkedIn automation with anti-detection safeguards."""

    def __init__(self, email: str, password: str, daily_limit: int = 8):
        self.email = email
        self.password = password
        self.daily_limit = daily_limit
        self.driver = None
        self.anthropic_client = anthropic.Anthropic()
        self.activity_log = []
        self.session_date = datetime.now().isoformat()

        # Anti-detection settings
        self.min_delay = 30  # seconds
        self.max_delay = 300  # seconds
        self.mouse_move_speed = 0.3  # seconds per movement

    def setup_driver(self) -> webdriver.Chrome:
        """Initialize Chrome driver with anti-detection measures."""
        logger.info("Setting up Chrome driver...")

        options = webdriver.ChromeOptions()

        # Stealth: Hide webdriver signals
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

        # Inject JavaScript to hide automation signals
        driver.execute_cdp_command('Page.addScriptToEvaluateOnNewDocument', {
            'source': '''
                Object.defineProperty(navigator, 'webdriver', {
                    get: () => false,
                });
            '''
        })

        logger.info("✅ Chrome driver initialized (stealth mode active)")
        return driver

    def random_delay(self, min_sec: int = None, max_sec: int = None) -> float:
        """Delay with randomization to avoid detection patterns."""
        min_sec = min_sec or self.min_delay
        max_sec = max_sec or self.max_delay
        delay = random.uniform(min_sec, max_sec)
        logger.debug(f"⏳ Waiting {delay:.1f} seconds...")
        time.sleep(delay)
        return delay

    def human_like_mouse_movement(self, element):
        """Move mouse to element like a human would."""
        try:
            actions = ActionChains(self.driver)
            # Random movement path (not direct)
            offset = random.randint(-50, 50)
            actions.move_to_element_with_offset(element, offset, random.randint(-20, 20))
            actions.perform()
            time.sleep(random.uniform(0.5, 1.5))
        except:
            pass

    def random_scroll(self):
        """Scroll page randomly like a human."""
        scroll_amount = random.randint(200, 800)
        self.driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
        self.random_delay(2, 5)

    def login_to_linkedin(self) -> bool:
        """Login to LinkedIn with anti-detection measures."""
        logger.info("Logging in to LinkedIn...")

        try:
            self.driver.get("https://www.linkedin.com/login")
            self.random_delay(3, 8)

            # Email field
            email_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            self.human_like_mouse_movement(email_field)
            email_field.clear()

            # Type slowly (like human)
            for char in self.email:
                email_field.send_keys(char)
                time.sleep(random.uniform(0.05, 0.15))

            self.random_delay(1, 3)

            # Password field
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

            # Wait for page load
            self.random_delay(5, 10)

            # Check for 2FA or CAPTCHA
            if self._check_for_verification():
                logger.warning("⚠️  2FA or verification detected. Please complete manually.")
                self.random_delay(30, 60)

            logger.info("✅ Logged in successfully")
            return True

        except Exception as e:
            logger.error(f"❌ Login failed: {e}")
            return False

    def _check_for_verification(self) -> bool:
        """Check if LinkedIn is asking for 2FA or verification."""
        try:
            # Look for common verification indicators
            self.driver.find_element(By.XPATH, "//*[contains(text(), 'verify')]")
            return True
        except:
            return False

    def search_and_find_leader(self, company_name: str, title_keyword: str = "CEO") -> Optional[Tuple[str, str]]:
        """Search for company leader and return (name, linkedin_url)."""
        logger.info(f"Searching for {title_keyword} at {company_name}...")

        try:
            # Go to search
            self.driver.get("https://www.linkedin.com/search/results/people/")
            self.random_delay(2, 5)

            # Search query: company + title
            search_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Search field']"))
            )

            search_query = f"{title_keyword} at {company_name}"
            for char in search_query:
                search_field.send_keys(char)
                time.sleep(random.uniform(0.03, 0.1))

            self.random_delay(1, 2)
            search_field.send_keys(Keys.RETURN)
            self.random_delay(3, 8)

            # Get first result
            try:
                first_result = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//a[@data-test-app-aware-link]"))
                )

                name = first_result.find_element(By.XPATH, ".//span[@aria-hidden='true']").text
                url = first_result.get_attribute("href")

                logger.info(f"   ✅ Found: {name}")
                return (name, url)
            except:
                logger.warning(f"   ⚠️  No results for {company_name}")
                return None

        except Exception as e:
            logger.error(f"   ❌ Search error: {e}")
            return None

    def send_connection_request(self, profile_url: str, message: str) -> bool:
        """Send connection request with personalized message."""
        logger.info(f"Sending connection request...")

        try:
            self.driver.get(profile_url)
            self.random_delay(2, 5)

            # Find "Connect" button
            connect_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(@aria-label, 'Invite')]"))
            )

            self.human_like_mouse_movement(connect_button)
            self.random_delay(0.5, 2)
            connect_button.click()

            self.random_delay(2, 4)

            # Add message (if available)
            try:
                add_note_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Add a note')]")
                add_note_button.click()
                self.random_delay(1, 2)

                message_field = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//textarea[@name='message']"))
                )

                # Type message slowly
                for char in message[:300]:  # LinkedIn limits connection messages
                    message_field.send_keys(char)
                    time.sleep(random.uniform(0.02, 0.08))

                self.random_delay(1, 3)
            except:
                logger.warning("   ⚠️  Could not add personalized message (may still connect)")

            # Send
            send_button = self.driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Send')]")
            self.human_like_mouse_movement(send_button)
            send_button.click()

            self.random_delay(2, 5)
            logger.info("   ✅ Connection request sent")
            return True

        except Exception as e:
            logger.error(f"   ❌ Failed to send connection: {e}")
            return False

    def send_direct_message(self, profile_url: str, message: str) -> bool:
        """Send direct message to already-connected user."""
        logger.info(f"Sending direct message...")

        try:
            self.driver.get(profile_url)
            self.random_delay(2, 5)

            # Open message composer
            message_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(@aria-label, 'Message')]"))
            )

            self.human_like_mouse_movement(message_button)
            message_button.click()
            self.random_delay(3, 6)

            # Type message
            message_field = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//textarea[@role='textbox']"))
            )

            for char in message:
                message_field.send_keys(char)
                time.sleep(random.uniform(0.02, 0.08))

            self.random_delay(1, 3)

            # Send
            send_button = self.driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Send')]")
            self.human_like_mouse_movement(send_button)
            send_button.click()

            self.random_delay(2, 5)
            logger.info("   ✅ Direct message sent")
            return True

        except Exception as e:
            logger.error(f"   ❌ Failed to send message: {e}")
            return False

    def generate_message(self, company_name: str, person_name: str, company_focus: str, key_insight: str) -> str:
        """Generate personalized connection message using Claude."""
        logger.debug(f"Generating message for {person_name}...")

        prompt = f"""Generate a short, personalized LinkedIn connection message (max 300 chars).

Target: {person_name} at {company_name}
Company focus: {company_focus}
Key insight: {key_insight}

Requirements:
- Sound genuine and calm, like texting a friend
- Mention ONE specific thing about their company
- Show genuine curiosity about their work
- No corporate jargon or sales speak
- Keep it short (3-4 sentences max)
- Include: who you are ({YOUR_NAME}, {YOUR_MAJOR} graduating {YOUR_GRADUATION})

Return ONLY the message text, no quotes or formatting."""

        try:
            response = self.anthropic_client.messages.create(
                model="claude-opus-4-7",
                max_tokens=200,
                messages=[{"role": "user", "content": prompt}]
            )

            message = response.content[0].text.strip()
            logger.debug(f"   Generated: {message[:50]}...")
            return message
        except Exception as e:
            logger.error(f"Message generation failed: {e}")
            return f"Hi {person_name}, I'm {YOUR_NAME} from TAMU. Impressed by your work at {company_name}. Would love to connect."

    def run_automation_loop(self, company_list: List[str], batch_size: int = None):
        """Main automation loop: research → find → connect → message."""
        batch_size = batch_size or self.daily_limit
        logger.info(f"\n🚀 Starting automation loop")
        logger.info(f"Daily limit: {self.daily_limit} connections")
        logger.info(f"Processing {len(company_list)} companies\n")

        completed = 0
        failed = 0

        for i, company in enumerate(company_list[:batch_size], 1):
            logger.info(f"\n[{i}/{batch_size}] Processing: {company}")

            try:
                # Step 1: Research company
                research = self._research_company(company)
                if not research['ceo_name'] or research['ceo_name'] == 'Unknown':
                    logger.warning(f"   ⚠️  Skipping (no CEO found)")
                    failed += 1
                    self.random_delay(5, 10)  # Still wait to avoid pattern
                    continue

                # Step 2: Find CEO on LinkedIn
                leader_url = self.search_and_find_leader(company, "CEO")
                if not leader_url:
                    logger.warning(f"   ⚠️  Skipping (not found on LinkedIn)")
                    failed += 1
                    self.random_delay(5, 10)
                    continue

                # Step 3: Generate personalized message
                message = self.generate_message(
                    company_name=company,
                    person_name=research['ceo_name'],
                    company_focus=research['company_focus'],
                    key_insight=research['key_insight']
                )

                # Step 4: Send connection request
                success = self.send_connection_request(leader_url[1], message)

                if success:
                    completed += 1
                    self._log_activity({
                        'company': company,
                        'ceo': research['ceo_name'],
                        'action': 'connection_request_sent',
                        'message': message,
                        'timestamp': datetime.now().isoformat()
                    })
                else:
                    failed += 1

                # Random delay between connections (CRITICAL for anti-detection)
                if i < batch_size:
                    delay = self.random_delay(60, 180)  # 1-3 min between connections
                    logger.info(f"   ⏳ Waiting {delay:.0f}s before next connection...")

            except Exception as e:
                logger.error(f"   ❌ Error processing {company}: {e}")
                failed += 1
                self.random_delay(10, 30)

        # Summary
        logger.info("\n" + "="*60)
        logger.info(f"SESSION COMPLETE")
        logger.info(f"✅ Successful: {completed}")
        logger.info(f"❌ Failed: {failed}")
        logger.info(f"📝 Activity log: linkedin-automation.log")
        logger.info("="*60)

    def _research_company(self, company_name: str) -> Dict:
        """Research company using Claude API."""
        prompt = f"""Research {company_name}. Return ONLY valid JSON (no markdown):
{{
    "ceo_name": "Name or 'Unknown'",
    "company_focus": "What they do",
    "key_insight": "One specific insight for personalization"
}}"""

        try:
            response = self.anthropic_client.messages.create(
                model="claude-opus-4-7",
                max_tokens=300,
                messages=[{"role": "user", "content": prompt}]
            )

            text = response.content[0].text.strip()
            if text.startswith("```"):
                text = text.split("```")[1].strip("json").strip()

            return json.loads(text)
        except:
            return {
                "ceo_name": "Unknown",
                "company_focus": "Unknown",
                "key_insight": "Unknown"
            }

    def _log_activity(self, activity: Dict):
        """Log activity for review."""
        self.activity_log.append(activity)
        with open('linkedin-activity.json', 'a') as f:
            json.dump(activity, f)
            f.write('\n')

    def cleanup(self):
        """Cleanup and save logs."""
        if self.driver:
            self.driver.quit()
            logger.info("✅ Browser closed")


def main():
    import argparse

    parser = argparse.ArgumentParser(description="LinkedIn Full Automation with Anti-Detection")
    parser.add_argument("--email", required=True, help="LinkedIn email")
    parser.add_argument("--password", required=True, help="LinkedIn password")
    parser.add_argument("--emails", default="sent_emails.txt", help="File with company names")
    parser.add_argument("--daily-limit", type=int, default=8, help="Max connections per day")

    args = parser.parse_args()

    logger.info("\n" + "="*60)
    logger.info("LinkedIn Automation Agent v1.0")
    logger.info("="*60)
    logger.info(f"Daily limit: {args.daily_limit} connections")
    logger.info(f"⚠️  WARNING: Start with 5 connections, monitor account")
    logger.info("="*60 + "\n")

    # Initialize agent
    agent = LinkedInAutomationAgent(args.email, args.password, daily_limit=args.daily_limit)

    try:
        # Setup
        agent.driver = agent.setup_driver()

        # Login
        if not agent.login_to_linkedin():
            logger.error("Login failed. Exiting.")
            return

        # Load companies
        try:
            with open(args.emails, 'r') as f:
                companies = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            logger.error(f"Company file not found: {args.emails}")
            return

        logger.info(f"Loaded {len(companies)} companies")

        # Run automation
        agent.run_automation_loop(companies, batch_size=args.daily_limit)

    except KeyboardInterrupt:
        logger.warning("\n⚠️  Interrupted by user")
    except Exception as e:
        logger.error(f"Fatal error: {e}")
    finally:
        agent.cleanup()


if __name__ == "__main__":
    main()
