"""
PROJECT: Advanced Image Processor (Simulator)

Goal: Create a CLI tool that simulates an image processing application.

Requirements:

1. Arguments:
   - 'input' (Positional): The path to the input image file.
   - 'output' (Positional): The path to save the result.
   - '--mode' (Optional): Choices are "blur", "grayscale", "resize". Default is "grayscale".
   - '--quality' (Optional): An integer between 1 and 100. Default is 90.
   - '--verbose' (Flag): If set, print extra details.

2. Simulation Logic:
   - Print: "Processing [input] using [mode] mode..."
   - If verbose is set, print: "Setting quality to [quality]%..."
   - Print: "Saving result to [output]... Done!"

3. Help:
   - Ensure the script has a clear description: "Simulate an image processing tool."

Real-World Logic:
- This is exactly how tools like ImageMagick, FFmpeg, or custom data processing scripts are built.
"""

# TODO: Implement the Image Processor
import argparse

def process_image():
    parser = argparse.ArgumentParser(description="Simulate an image processing tool.")
    parser.add_argument("input", help="Path to the input image file")
    parser.add_argument("output", help="Path to save the result")
    parser.add_argument("--mode", choices=["blur", "grayscale", "resize"], default="grayscale", help="Mode of processing")
    parser.add_argument("--quality", type=int, default=90, help="Quality of processing")
    parser.add_argument("--verbose", action="store_true", help="Verbose output")
    args = parser.parse_args()
    print(f"Processing {args.input} using {args.mode} mode...")
    if args.verbose:
        print(f"Setting quality to {args.quality}%")
    print(f"Saving result to {args.output}... Done!")


if __name__ == "__main__":
    process_image()
