from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Create a WebDriver instance
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

# Wait for the user to scan the QR code
input('Enter anything after scanning QR code')

# Your custom configuration
filepath = r'F:\W_auto\demo1\O.jpg'

# Read message from message.txt
with open('message.txt', 'r') as message_file:
    message = message_file.read()

# Read phone numbers from numbers.txt
with open('numbers.txt', 'r') as numbers_file:
    phone_numbers = numbers_file.read().splitlines()

# Loop through each phone number
for number in phone_numbers:
    try:
        # Find the user/group by phone number
        driver.get(f'https://web.whatsapp.com/send?phone={number}')

        # Wait for the chat to load
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"]')))
    
        # Attach the image
        attachment_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@title="Attach"]')))
        attachment_box.click()

        image_box = driver.find_element(By.XPATH,
            '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        image_box.send_keys(filepath)

        # Wait for image to upload and type the message as image caption
        sleep(10)  # Adjust this timing if needed
        text_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"]')))
        text_input.click()
        text_input.send_keys(message)

        # Send the image with caption
        send_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//span[@data-testid="send"]')))
        send_button.click()

        # Wait for the message to be sent
        WebDriverWait(driver, 20).until(
            EC.invisibility_of_element_located((By.XPATH, '//span[@data-testid="send"]')))
        print(f"Message sent to {number}.")

        sleep(2)
        # Refresh the page to ensure a clean state for the next interaction
        driver.refresh()

    except TimeoutException:
        print(" ")
        continue

# Quit the WebDriver
driver.quit()
