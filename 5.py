import multiprocessing
import numpy as np

# Constants
rows, cols = 2048, 2048  # Adjusted size
al = 1  # Some constant value

# Sample array (not shared memory)
y = np.zeros((rows, cols))  

# Compute resolution function
def compute_resolution(start, end, pix_start1, pix_end1, pix_start2, pix_end2):
    scans = abs(end - start)  # Number of scans
    pixels = (abs(pix_end1 - pix_start1) + abs(pix_end2 - pix_start2))  # Total pixels per scan
    total_operations = scans * pixels
    return total_operations

# Function to process the first loop with arguments
def process_scan_1(start, end, al_value):
    resolution = compute_resolution(start, end, 1023, -1, 1024, 2048)
    print(f"First loop resolution: {resolution} operations")

    for scan in range(start, end, -1):
        for pix in range(1023, -1, -1):
            y[scan, pix] = y[scan + 1, pix] + al_value
        for pix in range(1024, 2048, 1):
            y[scan, pix] = y[scan + 1, pix] + al_value
    print(f"First loop completed with al={al_value}")

# Function to process the second loop with arguments
def process_scan_2(start, end, al_value):
    resolution = compute_resolution(start, end, 1023, -1, 1024, 2048)
    print(f"Second loop resolution: {resolution} operations")

    for scan in range(start, end, 1):
        for pix in range(1023, -1, -1):
            y[scan, pix] = y[scan + 1, pix] - al_value
        for pix in range(1024, 2048, 1):
            y[scan, pix] = y[scan + 1, pix] - al_value
    print(f"Second loop completed with al={al_value}")

if __name__ == "__main__":
    # Arguments for the functions
    args_1 = (1022, -1, al)  # Arguments for process_scan_1
    args_2 = (1024, 2048, al)  # Arguments for process_scan_2

    # Create two processes with arguments
    p1 = multiprocessing.Process(target=process_scan_1, args=args_1)
    p2 = multiprocessing.Process(target=process_scan_2, args=args_2)

    # Start both processes
    p1.start()
    p2.start()

    # Wait for both to finish
    p1.join()
    p2.join()

    print("Processing complete!")
