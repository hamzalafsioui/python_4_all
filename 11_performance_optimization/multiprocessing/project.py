"""
PROJECT: The Image Filter Simulator

Goal: Prove the power of Multiprocessing by simulating heavy image processing.

Requirements:

1. Setup:
   - Imagine we have 20 high-resolution images to process.
   - We will represent them as a list of integers: 'images = list(range(1, 21))'

2. The Task:
   - Create a function 'apply_filter(image_id)':
     - Simulate a heavy CPU task by doing a loop of 5,000,000 iterations doing math.
     - Return a string: f"Image {image_id} processed."

3. Execution 1: The Old Way
   - Process all 20 images using a standard 'for' loop.
   - Time the operation.

4. Execution 2: The Future
   - Process all 20 images using 'multiprocessing.Pool'.
   - Time the operation.

Real-World Logic:
- This is exactly how tools like Adobe Lightroom export hundreds of photos quickly. They don't process them one by one; they assign a photo to every available CPU core in your machine to export them in parallel.
"""



import time
import multiprocessing
# TODO: Implement the Image Filter Simulator



def apply_filter(image_id):

    result = 0

    for i in range(10_000_000):
        result += i * image_id

    return f"Image {image_id} processed."


def run_serial(images):

    start = time.time()

    results = []

    for image in images:
        results.append(apply_filter(image))

    end = time.time()

    print(f"Serial Time: {end - start:.2f} seconds")


def run_parallel(images):

    start = time.time()

    with multiprocessing.Pool() as pool:
        results = pool.map(apply_filter, images)

    end = time.time()

    print(f"Parallel Time: {end - start:.2f} seconds")


if __name__ == "__main__":

    images = list(range(1, 21))

    run_serial(images)

    run_parallel(images)


    
