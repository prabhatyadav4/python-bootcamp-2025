import threading
import time

# Define the worker function to be executed by each thread
def worker(num):
    print(f"Thread {num}: Starting")
    time.sleep(2)  # Simulate some work with a 2-second delay
    print(f"Thread {num}: Finished")

threads = []  # List to hold all thread objects
for i in range(3):  # Create 3 threads
    thread = threading.Thread(target=worker, args=(i,))  # Initialize thread with target function and arguments
    threads.append(thread)  # Add thread to the list
    thread.start()  # Start the thread

for thread in threads:  # Wait for all threads to complete
    thread.join()

print("All threads are finished.")  # Print when all threads are done