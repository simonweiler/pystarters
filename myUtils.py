import os
import matplotlib.pyplot as plt

def mySavefig(filename):
    try:
        plt.savefig(filename)
    except FileNotFoundError
