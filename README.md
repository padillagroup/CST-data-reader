# CST-data-reader
python script for importing and exporting CST data files.

CST datas files with multiple curves are a pain because headers are 
added at different points throughout the file. This code imports such 
obnoxious files, and outputs a separate .csv file containing the data for each curve.
Can also output a single file in a more amenable format, without obnoxious interspersed headers. 

An example CST data file is included in the repository. Running the 
script on this file should result in four output .csv files, each 
corresponding to a different simulated curve.
