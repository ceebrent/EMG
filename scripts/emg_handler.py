import csv
import time
from time import gmtime, strftime
import datetime
def proc_emg(emg, moving, times=[]):
        ## print framerate of received data
        times.append(time.time())
        
        date = strftime("%Y-%m-%d", gmtime())
        for vals in emg:
            times.append(vals)

        row = []       
        if len(times) > 8:
            row.append(time.time())
            for vals in emg:
                row.append(vals)
        csv_name = "EMG-DATA {date}.csv".format(date=date)
        with open(csv_name, 'a') as csvfile:
            fieldnames = ['Time', 'C_1', 'C_2', 'C_3', 'C-4', 'C_5', 'C_6',
                          'C_7', 'C_8']
            insert_values = dict(zip(fieldnames, row))
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(insert_values)
            
