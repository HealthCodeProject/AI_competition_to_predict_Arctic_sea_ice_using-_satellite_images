import numpy as np
import os
import pandas as pd
from tqdm import tqdm
import seaborn as sns
import matplotlib.pyplot as plt

data_dir = 'D:\R_data'
os.listdir(data_dir)

## train과 submission 부르기
train_csv = pd.read_csv(data_dir + '/train.csv')
submission = pd.read_csv(data_dir + '/sample_submission.csv')

filenames = os.listdir(data_dir + '/train')
filenames.sort()

data=[]

for filename in tqdm(filenames):
    data.append(
        np.load("{0}/train/{1}".format(data_dir, filename))
        )
data = np.array(data)


## EDA시작
## Missing Value
print("There are {0} missing pixels".format(data[:,:,:,-1].sum()))

## Coastline, Land Shape
a = np.zeros(shape=data[0][:,:,3].shape)
for i in tqdm(range(data.shape[0])):
    a += data[i][:,:,3]
    
a = (a/data.shape[0]).astype(int)

(a-data[i][:,:,3]).sum()

a=np.zeros(shape=data[0][:,:,2].shape)

for i in tqdm(range(data.shape[0])):
    a += data[i][:,:,2]
    
a = (a/data.shape[0]).astype(int)
(a-data[i][:,:,2]).sum()

## Pole Area
figure, ((ax1,ax2),(ax3,ax4)) = plt.subplots(nrows=2, ncols=2)
figure.set_size_inches(15,15)
plt.subplot(sns.heatmap(data[105][:,:,0]+(data[105][:,:,2])*250, ax=ax1))
sns.heatmap(data[106][:,:,0]+(data[106][:,:,2])*250, ax=ax2)
sns.heatmap(data[349][:,:,0]+(data[349][:,:,2])*250, ax=ax3)
sns.heatmap(data[350][:,:,0]+(data[350][:,:,2])*250, ax=ax4)


## Coastline vs Land
figure, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
figure.set_size_inches(14,6)
sns.heatmap(data[0][:,:,2], ax=ax1)
sns.heatmap(data[0][:,:,3],ax=ax2)
