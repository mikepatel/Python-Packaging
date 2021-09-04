"""
Michael Patel
September 2021

Project description:

File description:

"""
################################################################################
# Imports
import os
import pstats


################################################################################
# Main
if __name__ == "__main__":
    filepath = os.path.join(os.getcwd(), "stats\\GET.summary.1117ms.1630785050.prof")
    stats = pstats.Stats(filepath)
    stats.strip_dirs()
    stats.sort_stats("time", "calls")
    stats.print_stats()
