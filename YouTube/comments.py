from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Set up the Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open WhatsApp Web
driver.get("https://web.whatsapp.com")

# Wait for manual login (scan the QR code)
print("Please scan the QR code for WhatsApp Web login.")
WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//span[@title="Chats"]')))

# Define the contact and message
contact_name = "Haseeb"  # Replace with the contact's name exactly as it appears on WhatsApp
message_text = "Hello from Selenium!"  # Replace with the message you want to send

# Search for the contact in the search bar
search_box = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//*[@title="Search or start new chat"]'))
)
search_box.click()
search_box.send_keys(contact_name)

# Wait for the contact to appear and select it
contact = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, f'//span[@title="{contact_name}"]'))
)
contact.click()

# Find the message box and send the message
message_box = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//div[@title="Type a message"]'))
)
message_box.click()
message_box.send_keys(message_text)
message_box.send_keys(Keys.ENTER)

# Wait for a few seconds before closing
WebDriverWait(driver, 5)

# Close the browser
driver.quit()
