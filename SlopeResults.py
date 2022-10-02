# fit a fifth degree polynomial to the economic data
from pandas import read_csv
import numpy as np
from matplotlib import pyplot
import csv

exercises=["BC1","BC2","BC3","BC4","BC5","BP1","BP2","BP3","BP4","BP5","DL1","DL2","DL3","DL4","DL5","LR1","LR2","LR3","LR4","LR5","SP1","SP2","SP3","SP4","SP5","SQ1","SQ2","SQ3","SQ4","SQ5"]

headerset=False

with open('GymPoseResults.csv',"w", encoding="UTF8", newline='') as f:
    writer = csv.writer(f)
    for selectedexercise in exercises:
        url = 'ExerciseAnalysis/'+selectedexercise+ '.csv'
        dataframe = read_csv(url)

        header=[]
        data=[]

        for key in dataframe:
            x, y = list(range(0,len(dataframe[key]))), dataframe[key]
            # curve fit
            a, b, c, d ,e , f , g = np.polyfit(x, y, 6)
            data.extend([min(dataframe[key]), max(dataframe[key]), dataframe[key][0], a,b,c,d,e,f,g])
            header.extend(["min" + key ,"max" + key ,key, key+"_a",key+"_b",key+"_c",key+"_d",key+"_e",key+"_f",key+"_g"])

        header.append("result")
        data.append(selectedexercise[:-1])

        if headerset==False:
            writer.writerow(header)
            headerset=True
        writer.writerow(data)


