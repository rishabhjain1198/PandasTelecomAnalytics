"""
    Created by Rishabh Jain, 7/8/2017
    Python script to load json data and use plotting.py 
    to represent the final results
"""

import pandas as pd
import numpy as np
import plotting as plt
import json

def main():
    with open('output.txt', 'r') as file:
        dataset = json.load(file)

    import operator

    sorted_dataset = sorted(dataset.items(), key=lambda x:x[1])

    print(sorted_dataset)

"""
    Now we can use the sorted list of tuples to write to file for plotting of sorted 
    data in excel, or we can simply use text data and output orderless dict
    using plotting.py
"""

    with open('sorted_output.txt', 'w') as ff:
        ff.write('\n'.join('%s %s' % x for x in sorted_dataset))

    plt.plotthis(dataset)

if __name__ == '__main__':
    main()
