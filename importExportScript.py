import sys
import os
print(sys.executable)
print(sys.version)
import numpy as np
import re
import pandas as pd

def impExp(inputFilename, # name of CST exported file to be re-organized
           outputFilename, # name for exported file
           multOut: bool=True # toggle whether to separate into multiple output files or use a single file
           ):
    #import the file
    dataIn = pd.read_csv(inputFilename, sep='                   ', names=['Frequency', 'Value'])

    # search the first row for the frequency unit; assume all curves use the same frequency unit
    freqUnit = re.findall(r'\/ [a-zA-Z]*', str(dataIn.iloc[0]))
    if len(freqUnit)!=0:
        freqUnit= freqUnit[0][2:]
    else:
        print("Warning: frequency unit could not be located, probably CST was too dumb to figure out the unit during"
              " template based post-processing")
        freqUnit="N/A"
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

    if(multOut==True):
        # export the curves to separate csv files
        for counter, exportRowIndex in enumerate(exportRowIndices):
            dataToExport = dataIn.iloc[exportRowIndex[0]:exportRowIndex[1]]
            dataToExport.to_csv(path_or_buf=os.path.join(".", outputFilename + str(counter) + ".csv"),
                                index=False)
    else:
        # export the curves to the same csv file

        # get just the curve data
        justCurves = []
        for exportRowIndex in exportRowIndices:
            newCurve= dataIn.iloc[exportRowIndex[0]:exportRowIndex[1], 1].values
            print(np.shape(newCurve))
            justCurves.append(newCurve)

        # since CST is dumb and sometimes exports curves of different lengths even for the same param sweep, we have to
        # double check our output and pare down the curves that are longer
        # this introduces slight error since the frequencies for each point no longer necessarily match up nicely
        curveLengths = [len(curve) for curve in justCurves]
        minCurveLength = np.min(curveLengths)
        justCurvesPared = []
        for curve in justCurves:
            justCurvesPared.append(curve[:minCurveLength])
        justCurvesPared = np.array(justCurvesPared)

        # get just the frequencies
        freqs = dataIn.iloc[exportRowIndices[0][0]:exportRowIndices[0][1], :1].values
        # flatten the list since pandas is dumb, also take only enough frequencies to match the number of points in the
        # curves
        freqs = [item for sublist in freqs for item in sublist][:minCurveLength]

        # construct a df from the frequencies and data
        dataToExport = pd.DataFrame(
            data=justCurvesPared,
            columns=freqs)
        dataToExport.to_csv(path_or_buf=os.path.join(".", outputFilename + ".csv"), index=False)


# test the function
if __name__ =='__main__':
    # print("file called as main, running test for multOut=False...")
    # impExp(inputFilename='ARmodBuffScaleCurves.txt',
    #        outputFilename="allCurves",
    #        multOut=False)
    # print("file called as main, running test for multOut=True...")
    # impExp(inputFilename='ARmodBuffScaleCurves.txt',
    #        outputFilename="curve",
    #        multOut=True)
    print("done")
    impExp(inputFilename=os.path.join('.', 'tests', 'bp_2.txt'),
           outputFilename=os.path.join('.', 'tests', 'bp_2re'),
           multOut=False)
