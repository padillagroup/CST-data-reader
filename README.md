# CST-data-reader
python-based script for importing CST data files.

CST datas files with multiple curves are a pain because headers are 
added at different points throughout the file. This code imports such 
obnoxious files, and outputs a notes file with parameter information as 
well as a separate .csv file containing the data for each curve.

An example .txt file from CST is included. Running the script with the 
.txt as input should produce 4 separate .csv files, each one containing 
the data of a simulated curve from CST.
