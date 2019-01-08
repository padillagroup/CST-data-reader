import os
import pandas as pd

# takes in a .csv from CST's parameter sweep table plus a list of curves formatted via importExportScript.py and exports
# a nicely formatted table of the input geometric parameters + the CST simulated curves
def dataFormat(paramFilePath, curveFilePath, outputFileName):

    # import data from each file
    with open(paramFilePath, 'r') as paramFile:
        paramData = pd.read_csv(paramFile)

    with open(curveFilePath, 'r') as curveFile:
        curveData = pd.read_csv(curveFile)
    print(len(curveData[1:]))
    print(len(paramData[1:]))
    assert len(curveData[1:]) == len(paramData[1:]), "number of parameter sets does not match number of curves; CST is " \
                                                     "dumb and can insert a row with '0' at the end " \
                                                     "of a parameter table export"

    combDF = pd.concat([paramData, curveData], axis=1)
    with open(os.path.join('.', 'tests', str(outputFileName) + '.csv'), 'w') as outFile:
        combDF.to_csv(path_or_buf=outFile)


if __name__ == '__main__':
    dataFormat(os.path.join('.', 'tests', 'bp_2_params.csv'),
               os.path.join('.', 'tests', 'bp_2re.csv'),
               'bp2_Out')
