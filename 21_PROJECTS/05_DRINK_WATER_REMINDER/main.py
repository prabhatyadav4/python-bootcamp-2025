import time
from plyer import notification

# Infinite loop to continuously send notifications
while True:
    print("Drink Water Notification Started")  # Log message to indicate notification process has started
    # Display a notification to remind the user to drink water
    notification.notify(title="Please drink some", message="You need to drink some water!")
    time.sleep(5)  # Wait for 5 seconds before sending the next notification