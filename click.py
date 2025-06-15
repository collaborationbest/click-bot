from pynput.mouse import Controller, Button
import time

mouse = Controller()
click_count = 0  # Initialize click counter

print("Auto-clicker will start in 10 seconds. Press Ctrl+C to stop.")
time.sleep(10)  # Initial delay

print("Auto-clicker started. Clicking every 3 seconds...")
try:
    while True:
        mouse.click(Button.left, 1)  # Perform a left-click
        click_count += 1  # Increment counter
        print(f"Clicks: {click_count}", end="\r")  # Overwrite previous count
        time.sleep(3)  # Wait 3 seconds between clicks
except KeyboardInterrupt:
    print(f"\nAuto-clicker stopped. Total clicks: {click_count}")