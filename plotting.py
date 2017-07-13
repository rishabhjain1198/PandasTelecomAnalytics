"""
    Created by Rishabh Jain, 7/8/2017
    Python script to display a passed pre-parsed dataset
"""

import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter

def plotthis(mydata):
    letter_counts = Counter(mydata)
    df = pd.DataFrame.from_dict(letter_counts, orient='index')
    df.plot(kind='bar')
    plt.show()


if __name__ == '__main__':
    print("Please call this script from another function to provide the data set, copyright RJ")
