import glob
import numpy as np
import lasio
import pandas as pd
import json
from pandas import merge_ordered

class lasCheck:
    def __init__ (self, filepath):
        self.filepath=filepath
        self.filepath
    def report(self, logs_selected):
        self.logs_selected=logs_selected
        with open('alias.json') as file:
            alias = json.load(file) #load the JSON File
        report=pd.DataFrame(columns=self.logs_selected)
        for filename in glob.iglob(self.filepath, recursive=True):
            l = lasio.read(filename)
            data_well = l.df()
            log = list(data_well.columns.values)
            wellname=filename.split('\\')
            wellname=wellname[-1]
            header = [{
                'Well Name': wellname,
                'START':l.well.STRT.value,
                'STOP':l.well.STOP.value,
                'STEP':l.well.STEP.value,
                'Location': filename
            }]
            data_well['WELL'] = filename  
            log_list = pd.DataFrame(header)
            well = data_well['WELL'].unique()
            merged_data = pd.DataFrame()
            for i in range(len(well)):
                data = data_well.where(data_well['WELL']==well[i]).dropna(axis=1, how='all')
                for j in range(len(alias)):
                    welllog_name = list(set(data.columns).intersection(alias.get(list(alias)[j])))
                    samelog = data[welllog_name]
                    count_log = dict(sorted(zip(welllog_name, samelog.count()), key=lambda item: item[1], reverse=True))
                    welllog_name = list(count_log.keys())
                    if (len(welllog_name)!=0):
                        #If more than one log aliases exist, normalize each log to have same data range in the same depth
                        if (len(welllog_name)>1):
                            alias_logs = data[welllog_name].dropna()
                            if (len(alias_logs)!=0):
                                a = []; b = []; c = []
                                for n in range(len(alias_logs.columns)):
                                    q1 = alias_logs[welllog_name[n]].quantile(0.1)
                                    q9 = alias_logs[welllog_name[n]].quantile(0.9)
                                    a.append(q1)
                                    b.append(q9)
                                    c = [b-a for (a,b) in zip(a,b)]
                                    c = list(map(lambda x: x/c[0],c))
                                for n in range(len(welllog_name)):
                                    data.loc[:, welllog_name[n]] *= 1/c[n]
                            for k in range(len(welllog_name)-1):
                                data[welllog_name[0]].fillna(data[welllog_name[k+1]], inplace=True)
                        data[list(alias)[j]] = data[welllog_name[0]]
                merged_data = merged_data.append(data)
                merged_data = merged_data[merged_data['WELL'].notna()]
                new_list=[]
                for x in self.logs_selected:
                    if x in list(merged_data.columns):
                        new_list.append(x)
                merged_data = merged_data[new_list]   
            df=pd.DataFrame([["X"]*(len(list(merged_data.columns)))], columns=list(merged_data.columns))
            df2=pd.concat([df, log_list], axis=1)
            report=report.append(df2, ignore_index=True, sort=False)
        header=(list(log_list.columns) + self.logs_selected)
        report=report[header]
        print (report)
        return report


    def export(self, reportname):
        report.to_excel(str(reportname + ".xlsx"))
        print ("succes")
