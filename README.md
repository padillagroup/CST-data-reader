# CST-data-reader
python-based script for importing CST data files.

CST datas files with multiple curves are a pain because headers are 
added at different points throughout the file. This code imports such 
obnoxious files, and outputs a notes file with parameter information as 
well as a separate .csv file containing the data for each curve.

An example CST data file is included in the repository. Running the 
script on this file should result in four output .csv files, each 
corresponding to a different simulated curve.
