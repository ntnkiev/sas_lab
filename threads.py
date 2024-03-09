import threading
import time

# Define the first function to run in a separate thread


def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(1)


# Define the second function to run in a separate thread
def print_letters():
    for letter in ["A", "B", "C", "D", "E"]:
        print(f"Letter: {letter}")
        time.sleep(1.5)


# Create Thread instances for each function


thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start the threads
thread1.start()
thread2.start()

# Optionally, wait for the threads to complete before proceeding
thread1.join()
thread2.join()

print("Both threads have completed their execution.")
