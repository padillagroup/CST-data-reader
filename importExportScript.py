import sys
print(sys.executable)
print(sys.version)
import numpy as np
import re
import pandas as pd


def impExp(filename, # name of CST exported file to be re-organized
           multToggle # toggle whether to separate into multiple output files or use a single file
           ):
    #import the file
    dataIn = pd.read_csv(filename, sep='                   ', names=['Frequency', 'Value'])

    # search the first row for the frequency unit; assume all curves use the same frequency unit
    freqUnit = re.findall(r'\/ [a-zA-Z]*', str(dataIn.iloc[0]))[0][2:]
    # update stored dataframe to have frequency unit in its header
    dataIn.columns = ['Frequency (' + freqUnit + ')', 'Value']
    # note the separator argument may be different in a different version of CST

    # store all rows where the value entry is null (or NaN), as it will be for rows that have strings (i.e, header rows)
    headerData = dataIn[dataIn.isnull().any(axis=1)]

    # define the beginnings and endings of row sets to export
    starts = np.array(headerData.index.values)[1::2] + 1
    ends = np.append(
        np.array(headerData.index.values)[2::2],
        dataIn.shape[0])

    # put the starts and ends together
    exportRowIndices = []
    for start, end in zip(starts, ends):
        exportRowIndices.append([start, end])

    # export the curves to separate csv files
    for counter, exportRowIndex in enumerate(exportRowIndices):
        dataToExport = dataIn.iloc[exportRowIndex[0]:exportRowIndex[1]]
        dataToExport.to_csv(path_or_buf='.\curve' + str(counter) + '.csv', index=False)

# test the function
if __name__ =='__main__':
    print("file called as main, running test for multToggle=False...")
    impExp(filename='ARmodBuffScaleCurves.txt', multToggle=False)
    print("file called as main, running test for multToggle=True...")
    impExp(filename='ARmodBuffScaleCurves.txt', multToggle=True)
    print("done")