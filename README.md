# WellLog-Check
This repository is inspired by my very first python code I wrote back in my scripting and data handling class during my MSc study. I used the glob library to access multiple files under folders and subfolders.

Based on my experiences, the well logs given  were usually not accompanied with the log availability checklist. So, I decided to write this code to automatically explore through folders and create report on xlsx format. I hope this repository could be useful for the your future needs. In this repository, I will use the glob library to access the .LAS files and check the log availability on my files with [lasio](https://lasio.readthedocs.io/en/latest/installation.html). 

Please check the jupyter notebook file titled logCheck.ipynb to see how I use the glob library on reviewing the log availability of my dataset. You can also check the report exported to xlsx files under the report sub-folder.

### Try it on your own
For you who hasn't work with python enough, I compiled my codes and you can easily use the code and apply to your directory by your own.
All you need is to do is download the lasCheck.py, requirements.txt and alias.json under the files sub-folder, put the files at the same folder of your jupyter-notebook ipynb file.
And then you can do this on your jupyter notebook:

1.) install the all libraries required
```
! pip install -r requirements.txt
```
2.) import the lasCheck.py on your notebook
```
from lasCheck import *
```
3.) use the functions
```
#define the logs that we are interested in our las files, select based on the alias name on the JSON file
logs_selected= ['CAL', 'RXO', 'GR', 'POR', 'DRES', 'DT', 'DENS', 'DRHO'] 
filepath=r'D:\logChecker\**\*.las'

#call the functions
logcheck=lasCheck(filepath)
logs_checked=logcheck.report(logs_selected)
```
4.) Finally, you can export the report to excel file using pandas.
```
logs_checked.to_excel("log checklist.xlsx")
```
![alt text](https://github.com/panjoel4/WellLog-Check/blob/main/Files/report%20in%20xlsx.PNG?raw=true)
For step-by-step instruction you can follow this [Try on your own](https://github.com/panjoel4/WellLog-Check/blob/main/Jupyter-Notebook/Try%20it%20on%20your%20own.ipynb) notebook.

### Dependencies
All these following libraries must be satisfied before running this codes on your laptop.
- [lasio](https://lasio.readthedocs.io/en/latest/installation.html) <br/>
- [pandas](https://pandas.pydata.org/) <br/>
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/) <br/>

Feel free to fork or pull this repository to improve the codes. 
