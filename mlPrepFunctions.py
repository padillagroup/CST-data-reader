import os
import numpy as np
import pandas as pd

# takes in a .csv from CST's parameter sweep table plus a list of curves formatted via importExportScript.py and exports
# a nicely formatted table of the input geometric parameters + the CST simulated curves
def dataFormat(paramFilePath, curveFilePath):

    # import data from each file
    with open(paramFilePath) as paramFile:
        paramData = pd.read_csv(paramFile)

    with open(curveFilePath) as curveFile:
        curveData = pd.read_csv(curveFile)
    assert len(curveData[1:]) == len(paramData[1:]), "number of parameter sets does not match number of curves"



if __name__ == '__main__':
    dataFormat(os.path.join('.', 'tests', 'bp_2_params.csv'),
               os.path.join('.', 'tests', 'bp_2.txt'))
