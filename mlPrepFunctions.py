import os
import pandas as pd

# takes in a .csv from CST's parameter sweep table plus a list of curves formatted via importExportScript.py and exports
# a nicely formatted table of the input geometric parameters + the CST simulated curves
def dataFormat(paramFilePath, curveFilePath, outputFilepath):

    # import data from each file
    with open(paramFilePath, 'r') as paramFile:
        paramData = pd.read_csv(paramFile)
        finalVal = paramData.tail(1).values[0]
        # some versions of CST tack a row of just 0 on the end of a param table export
        # if present, remove this useless row
        if len(finalVal) == 1:
            paramData.drop(paramData.tail(1).index, inplace=True)

    with open(curveFilePath, 'r') as curveFile:
        curveData = pd.read_csv(curveFile)
    print(len(paramData[1:]))
    print(len(curveData[1:]))
    assert len(curveData[1:]) == len(paramData[1:]), "number of parameter sets does not match number of curves; " \
                                                     "CST is dumb and can insert a row with '0' at the end " \
                                                     "of a parameter table export; also, CST can export the entire" \
                                                     "table of stored parameters even if only a subset is selected"

    comb_df = pd.concat([paramData, curveData], axis=1)
    comb_df.to_csv(path_or_buf=outputFilepath, sep=',',  header=None)

if __name__ == '__main__':
    print(os.path.dirname(os.path.realpath(__file__)))

    dataFormat(paramFilePath=os.path.join('.', 'tests', 'bp_2_params.csv'),
               curveFilePath=os.path.join('.', 'tests', 'bp_2re.csv'),
               outputFilepath='bp2_Out')
