from pynput.mouse import Controller, Button
import time

mouse = Controller()

print("Auto-clicker started. Press Ctrl+C to stop.")
try:
    while True:
        # Get current mouse position
        position = mouse.position
        
        # Click at the current position
        mouse.click(Button.left, 1)
        
        # Wait for 3 seconds
        time.sleep(3)
except KeyboardInterrupt:
    print("\nAuto-clicker stopped.")