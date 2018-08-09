import numpy as np
import re
import pandas as pd

#import the file
filename = 'ARmodBuffScaleCurves.txt'
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
for i in range(len(starts)):
    exportRowIndices.append([starts[i], ends[i]])

# export the curves to separate csv files
for i in range(len(exportRowIndices)):
    dataToExport = dataIn.iloc[exportRowIndices[i][0]:exportRowIndices[i][1]]
    dataToExport.to_csv(path_or_buf='.\curve' + str(i) + '.csv', index=False)
