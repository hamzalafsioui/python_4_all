"""
PROJECT: The Image Pipeline Optimizer

Goal:
- Profile a slow pipeline with cProfile
- Find the bottleneck using cumulative time (cumtime)
- Optimize the slow function
- Compare performance before and after

Real-world lesson:
Most performance problems come from a tiny portion of the code.
Profilers help us find the exact bottleneck instead of guessing.
"""

import time
import cProfile
import pstats


# =========================================================
# BROKEN VERSION
# =========================================================

def load_image():
    """Simulate disk/network image loading."""
    time.sleep(0.1)


def transform_pixels_broken():
    """
    Intentional bottleneck:
    Very slow manual loop.
    """
    total = 0

    for i in range(5_000_000):
        total += i

    return total


def save_image():
    """Simulate saving image."""
    time.sleep(0.1)


def run_pipeline_broken():
    load_image()
    transform_pixels_broken()
    save_image()


# =========================================================
# OPTIMIZED VERSION
# =========================================================

def transform_pixels_optimized():
    """
    Optimized version:
    Use Python's built-in sum(), implemented in C internally
    and much faster than a Python loop.
    """
    return sum(range(5_000_000))


def run_pipeline_optimized():
    load_image()
    transform_pixels_optimized()
    save_image()


# =========================================================
# PROFILING HELPERS
# =========================================================

def profile_function(func, label):
    print(f"\n{'=' * 60}")
    print(f"Profiling: {label}")
    print(f"{'=' * 60}")

    profiler = cProfile.Profile()

    start = time.perf_counter()

    profiler.enable()
    func()
    profiler.disable()

    end = time.perf_counter()

    stats = pstats.Stats(profiler)
    stats.sort_stats("cumtime")

    # Show top functions by cumulative time
    stats.print_stats(10)

    print(f"\nTotal execution time: {end - start:.4f} seconds")


# =========================================================
# MAIN
# =========================================================

if __name__ == "__main__":

    # BEFORE optimization
    profile_function(
        run_pipeline_broken,
        "BROKEN PIPELINE"
    )

    # AFTER optimization
    profile_function(
        run_pipeline_optimized,
        "OPTIMIZED PIPELINE"
    )