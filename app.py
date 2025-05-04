import asyncio
from playwright.async_api import async_playwright
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_from = '+15089805514'               
twilio_to = '+905456461027'                

def send_sms(message):
    client = Client(account_sid, auth_token)
    client.messages.create(
        body=message,
        from_=twilio_from,
        to=twilio_to
    )

async def check_stock():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        await page.goto('https://www.tesla.com/tr_TR/modely/design#overview')
        try:
            close_button = await page.wait_for_selector('button[aria-label="Close Modal"]', timeout=5000)
            await close_button.click()
            await page.wait_for_timeout(1000)  
            print("Modal kapatıldı.")
        except:
            print("Modal görünmedi veya kapatma butonu bulunamadı.")

        await page.click('label[for="$MTY47-Long Range Dört Çeker"]')
        await page.wait_for_timeout(3000)  
        try:
            await page.wait_for_selector('button.tds-btn.aside-footer--button', timeout=5000)
            print("Stoklarda yok: 'Güncellemeleri Al' butonu mevcut.")

        except:
            print("Stoklarda var: 'Güncellemeleri Al' butonu bulunmuyor.")
            send_sms("🚗 Tesla Model Y Long Range Dört Çeker stokta!")

        await browser.close()

asyncio.run(check_stock())
