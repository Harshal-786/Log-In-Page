import multiprocessing
import numpy as np

# Constants
rows, cols = 2048, 2048  # Adjusted size
al = 1  # Some constant value

# Sample array (not shared memory)
y = np.zeros((rows, cols))  

# Function to process the first loop
def process_scan_1():
    for scan in range(1022, -1, -1):
        for pix in range(1023, -1, -1):
            y[scan, pix] = y[scan + 1, pix] + al
        for pix in range(1024, 2048, 1):
            y[scan, pix] = y[scan + 1, pix] + al
    print("First loop completed")

# Function to process the second loop
def process_scan_2():
    for scan in range(1024, 2048, 1):
        for pix in range(1023, -1, -1):
            y[scan, pix] = y[scan + 1, pix] - al
        for pix in range(1024, 2048, 1):
            y[scan, pix] = y[scan + 1, pix] - al
    print("Second loop completed")

if __name__ == "__main__":
    # Create two processes
    p1 = multiprocessing.Process(target=process_scan_1)
    p2 = multiprocessing.Process(target=process_scan_2)

    # Start both processes
    p1.start()
    p2.start()

    # Wait for both to finish
    p1.join()
    p2.join()

    print("Processing complete!")
