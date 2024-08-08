import pyautogui
import time

# List of phone numbers with country code
phone_numbers = [
    "baby",
    "nived",
    "amalettan pg",
    "John"

    
]

message = "Shuba Dhinam "  # Message to be sent

# Function to send message using WhatsApp Desktop
def send_whatsapp_message(phone_number, message):
    # Open WhatsApp Desktop
    pyautogui.hotkey('win', 's')
    time.sleep(1)
    pyautogui.write('WhatsApp')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)  # Wait for WhatsApp Desktop to open

    # Click on the search bar
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(1)
    pyautogui.press('ctrl'+'a')

    # Type the phone number
    pyautogui.write(phone_number)
    time.sleep(2)  # Wait for the contact to appear

    # Click on the first result (assuming it's the correct one)
    # Adjust x and y coordinates based on your screen resolution and layout
    pyautogui.press('tab') 
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)  # Wait for the chat to open

    # Type the message
    pyautogui.write(message)
    time.sleep(1)

    # Press enter to send the message
    pyautogui.press('enter')
    time.sleep(2)  # Wait for the message to be sent

# Loop through the list of phone numbers and send the message
for phone_number in phone_numbers:
    send_whatsapp_message(phone_number, message)
    time.sleep(5)  # Wait before sending the next message

# Close WhatsApp Desktop (optional)
pyautogui.hotkey('alt', 'f4')
