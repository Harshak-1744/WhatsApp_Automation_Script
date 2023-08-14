# WhatsApp Message Automation Script

This Python script automates sending messages with images and captions to multiple WhatsApp contacts or groups using the Selenium WebDriver. The script interacts with the WhatsApp Web interface, allowing you to send messages to your contacts without manual intervention.

## Prerequisites

- Python 3.x
- Google Chrome browser
- ChromeDriver (WebDriver for Chrome)
- Selenium library (`pip install selenium`)

## Setup

1. Install Python: Make sure you have Python 3.x installed on your system.

2. Install Chrome Browser: If not already installed, download and install the [Google Chrome browser](https://www.google.com/chrome/).

3. Download ChromeDriver: Download the appropriate version of [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) based on your Chrome browser version. Make sure to place the `chromedriver.exe` executable in the same directory as your script.

4. Install Selenium: Install the Selenium library using the following command:
   ```
   pip install selenium
   ```

## Usage

1. Clone or download this repository to your local machine.

2. Prepare your message and phone number lists:
   - Create a text file named `message.txt` and write your desired message or image caption.
   - Create a text file named `numbers.txt` and list the phone numbers of the contacts/groups you want to send messages to, each on a new line.

3. Modify the script:
   - Replace the `filepath` variable with the path to the image you want to send.
   - Adjust the `sleep` timing as needed to ensure proper synchronization with the WhatsApp Web interface.

4. Run the script:
   - Open a terminal in the directory containing the script.
   - Run the script using the following command:
     ```
     python script_name.py
     ```
   - Follow the instructions in the terminal to scan the WhatsApp QR code.

5. Script Execution:
   - The script will loop through each phone number in `numbers.txt`, sending the image with the specified message as a caption.
   - If a TimeoutException occurs during any step, the script will skip that particular contact and continue with the next one.
   - The script will print messages indicating the status of message sending for each contact.

6. Clean Up:
   - After all messages have been sent, the script will automatically close the WebDriver.

## Disclaimer

- This script is for educational and informational purposes only.
- Use this script responsibly and respect WhatsApp's terms of service.
- Automated messaging should be used in accordance with legal and ethical guidelines.

Remember to replace `script_name.py` with the actual name of your Python script. Additionally, make sure to abide by WhatsApp's terms of service and applicable laws while using automated messaging tools.
