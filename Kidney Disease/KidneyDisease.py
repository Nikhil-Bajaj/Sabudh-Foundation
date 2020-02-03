import pandas as pd
import numpy as np
import os
pd.set_option('display.width', 500)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 30)
data=pd.read_csv("C:/Users/AKHIL/PycharmProjects/Ssbudh/Kidney Disease/kidney-disease-dataset/kidney_disease.csv",index_col = False)
'''
col= ['age', 'bp', 'bgr', 'bu', 'sc', 'sod', 'pot', 'hemo', 'pcv', 'wc', 'rc']
for c in col:
    data[c] = pd.to_numeric(data[c], errors="coerce")
'''
data.columns=['Id','Age','Blood Pressure','Specific Gravity','Albumin','Sugar','Red Blood Cells','Pus Cell', 'Pus Cell clumps', 'Bacteria', 'Blood Glucose Random', 'Blood Urea', 'Serum Creatinine', 'Sodium', 'Potassium', 'Hemoglobin',  'Packed Cell Volume', 'White Blood Cell Count', 'Red Blood Cell Count', 'Hypertension', 'Diabetes Mellitus', 'Coronary Artery Disease', 'Appetite', 'Pedal Edema', 'Anemia', 'class']

data.replace('ckd\t','ckd',inplace=True)
data['class'].replace({'notckd':0,'ckd':1}, inplace=True)
#print(data['class'])
#print(data['class'].value_counts())
#print(len(list(data))+1)
#for x in range(1,len(list(data))+1):
    #print(data['{}'.format(list(data)[x])].value_counts())
#print(data["{}".format(list(data)[6])].value_counts())
#print(data['Red Blood Cell Count'].value_counts())

cleanup = {"Red Blood Cells": {"normal": 1, "abnormal": 0},
           "Pus Cell": {"normal": 1, "abnormal": 0},
           "Pus Cell clumps": {"present": 1, "notpresent": 0},
           "Bacteria": {"present": 1, "notpresent": 0},
           "Hypertension": {"yes": 1, "no": 0},
           "Diabetes Mellitus": {"yes": 1, "no": 0},
           "Coronary Artery Disease": {"yes": 1, "no": 0},
           "Appetite": {"good": 1, "poor": 0},
           "Pedal Edema": {"yes": 1, "no": 0},
           "Anemia": {"yes": 1, "no": 0}}
data.replace(cleanup,inplace= True)
data.fillna(round(data.mean(),2), inplace=True)
#data.fillna(method='ffill')
print(data.head(n=10))
print(data['Red Blood Cells'].mean())
try:
    os.remove('processed.csv')
except:
    pass

data.to_csv("C:/Users/AKHIL/PycharmProjects/Ssbudh/Kidney Disease/kidney-disease-dataset/processed.csv", sep=',', index=False)
print("Exported")