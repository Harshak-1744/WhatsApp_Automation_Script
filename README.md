# WhatsApp Message Automation Script

## Overview

This Python script automates the process of sending messages to multiple WhatsApp contacts using the WhatsApp Web interface. It utilizes the Selenium library to control a web browser and perform the necessary actions to send messages.

## Prerequisites

Before using the script, make sure you have the following installed:

- Python (version 3.6 or later)
- Chrome web browser

You also need to install the required Python packages using the following command:

```bash
pip install selenium webdriver_manager
```

## Usage

1. Clone this repository or download the script to your local machine.

2. Create two text files in the same directory as the script:

   - `numbers.txt`: List of phone numbers, one per line, without the country code or any special characters.
   - `message.txt`: The message you want to send. This can be a plain text file.

3. Update the script's configuration section to set the desired time intervals, country code, and file names.

4. Run the script:

   ```bash
   python script_name.py
   ```

   Replace `script_name.py` with the actual name of your script file.

5. The script will open a browser window to the WhatsApp Web interface. You will need to scan the QR code to log in to your WhatsApp account.

6. Once logged in, the script will start sending messages to the phone numbers listed in `numbers.txt`.

## Configuration

You can configure the following parameters in the script:

- `login_time`: Time (in seconds) to allow for logging in to WhatsApp Web.
- `new_msg_time`: Time (in seconds) to wait for a new message to be created before sending.
- `send_msg_time`: Time (in seconds) to wait after sending a message.
- `country_code`: Your country code for phone numbers.
- `message.txt`: Replace this file's content with the message you want to send.

## Note

- Use this script responsibly and respect WhatsApp's terms of use.
- This script may require adjustments if WhatsApp Web's layout changes.
- Internet connectivity is required for the script to work.

## Disclaimer

This script is provided for educational purposes only. I am  not responsible for any misuse or violations of terms of service resulting from its usage.
