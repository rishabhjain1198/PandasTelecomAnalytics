""" 
    Created by Rishabh Jain, 7/8/2017
    Python script to parse the specific client data and
    infer/plot information.
"""
import json
import pandas as pd
import matplotlib as plt
import numpy as np

df = pd.read_csv("sdtaa.csv")
df.head(10)
df.describe()
df['Component'].value_counts(sort=True)

df['Component'].value_counts(sort=True).plot(kind='bar')

"""
    Adjusting of the matplot graph display is required to
    get comprehensible information from the data representation.
"""

#plt.pyplot.show() //commented out to speed up manual analyzation


"""
    Repeating the same procedure on the Object of Reference field
    in order to organize data for sites with high problem frequencies.
"""

print(df['ObjectOfReferenceSubNetwork,SubNetwork,ManagedElement,BssFunction,BtsSiteMgr'].value_counts(sort=True))

df['ObjectOfReferenceSubNetwork,SubNetwork,ManagedElement,BssFunction,BtsSiteMgr'].value_counts(sort=True).plot(kind='bar')

#plt.pyplot.show()  //commented out to speed up manual analyzation

timeData = {'testProblem' : 0}

for problem in df.Component.unique():
    times = []
    erroneousTimes = 0
    for index, row in df.iterrows():
        if row['Component'] == problem:
            if row['TimeDelta'] > 0:

                """ This if block is necessary to discard erroneous
                    alarm times. It can also be slightly modified to 
                    count the errors to help with the predictive model.
                """

                times.append(row['TimeDelta'])
            else:
                erroneousTimes = erroneousTimes + 1

    sumTimes = 0
    for time in times:
        sumTimes = sumTimes + time

    meanTimes = 0

    numberTimes = len(times)

    if numberTimes != 0:
        meanTimes = sumTimes/numberTimes

    """ The above code block finds out the mean of the collected 
        delta time values.
    """
    
    # We add our calculations to our new dictionary data set

    timeData[problem] = meanTimes


"""
    The previous code block does calculations of exponential 
    complexity. Hence, we do it once and then save the results
    to a json file for future use (plotting).
"""

print(timeData)

with open('output.txt', 'w') as file:
    file.write(json.dumps(timeData))
    

