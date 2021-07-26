# WellLog-Check
This repository is inspired by my very first python code I wrote back in my scripting and data handling class during my MSc study. I used the glob library to access multiple files under folders and subfolders.

In this repository, I will use the glob library to access the .LAS files and check the log availability on my files. Based on my experiences, sometimes the new well logs given were not accompanied with the availability checklist. I hope this repository could be useful for the your future needs.

Please check the jupyter notebook file titled logCheck.ipynb to see how I use the glob library on reviewing the log availability of my dataset. You can also check the report exported to xlsx files under the report sub-folder.

## Try it on your own
For you who hasn't work with python enough, I compiled my codes and you can easily use the code and apply to your directory by your own.
All you need is to do is download the lasCheck.py and alias.json under the files sub-folder, put the files at the same folder of your jupyter-notebook ipynb file.
And then you can do this on your jupyter notebook:

1.) install the lasio library as follow
```
pip install lasio
```
2.) import the lasCheck.py on your notebook
```
from lasCheck import *
```
3.) use the functions
```
#define the logs that we are interested in our las files, select based on the alias name on the JSON file
logs_selected= ['CAL', 'RXO', 'GR', 'POR', 'DRES', 'DT', 'DENS', 'DRHO'] 
filepath=r'C:\Users\Henky\JUPYTER\logChecker\**\*.las'

#call the functions
logcheck=lasCheck(filepath)
logs_checked=logcheck.report(logs_selected)
```

For step-by-step instruction you can follow this [Try on your own](https://github.com/panjoel4/WellLog-Check/blob/main/Jupyter-Notebook/Try%20it%20on%20your%20own.ipynb) notebook.

Feel free to fork or pull this repository to improve the codes. 
