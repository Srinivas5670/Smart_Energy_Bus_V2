"""
Smart Energy Bus V2
Utility Functions
"""

import os
import time


# =====================================================
# Console Helpers
# =====================================================

def print_header(title):
    """
    Print a formatted header.
    """

    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def print_subheader(title):
    """
    Print a formatted sub-header.
    """

    print("\n" + "-" * 60)
    print(title)
    print("-" * 60)


# =====================================================
# Timer
# =====================================================

class Timer:
    """
    Simple timer utility.
    """

    def __init__(self):

        self.start_time = None

    def start(self):

        self.start_time = time.time()

    def stop(self):

        if self.start_time is None:
            return 0

        return time.time() - self.start_time


# =====================================================
# Folder Helper
# =====================================================

def create_folder(folder_path):
    """
    Create folder if it doesn't exist.
    """

    os.makedirs(
        folder_path,
        exist_ok=True
    )


# =====================================================
# Time Formatter
# =====================================================

def format_time(seconds):
    """
    Convert seconds to readable format.
    """

    if seconds < 60:

        return f"{seconds:.2f} sec"

    minutes = int(seconds // 60)

    seconds = seconds % 60

    return f"{minutes} min {seconds:.2f} sec"