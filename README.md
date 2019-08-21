# CST-data-reader
python script for importing and exporting CST data files.

CST datas files with multiple curves are a pain because headers are 
added at different points throughout the file. This code imports such 
annoying files, and produces a separate .csv file containing the data for each curve.
Can also produce a single file in a more amenable format, without obnoxious interspersed headers. 

An example CST data file is included in the repository. Running the 
script on this file should result in four output .csv files, each 
corresponding to a different simulated curve.

Also included is mlPrepFunctions.py, which is for preparing CST data to be pulled into TF or similar. The idea is to combine a param table file that has been exported from CST MWS with a file of spectra which has been processed by importExportScript.py. This results in a single csv file with matched parameters and spectra. 
