# -*- coding: utf-8 -*-
"""

    URL : https://dacon.io/competitions/official/235706/codeshare/2410?page=1&dtype=recent
    

"""


#-----------------------------------------------------------------------------------#
## module import

import os, glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tqdm
from tqdm import tqdm

def sorted_list(path):
    tmplist = glob.glob(path)
    tmplist.sort()
    return tmplist

def show_data(npy):
    num_channel = npy.shape[-1]
    plt.figure(figsize=(3*num_channel, 5))
    for channel in range(num_channel):
        tmpimg = npy[:, :, channel]
        ax = plt.subplot(1, num_channel, channel+1)
        if channel == 0:
          ax.title.set_text("Ice Concentration(0~250)")
        elif channel == 1:
          ax.title.set_text('North Pole')
        elif channel == 2:
          ax.title.set_text('Coastline Mask')
        elif channel == 3:
          ax.title.set_text('Land Mask')
        else:
          ax.title.set_text('NULL VALUE')
        ax.imshow(tmpimg)
    plt.tight_layout()
    plt.show()
    plt.close()
    
    
    
    
PATH = 'C:/Users/gksxo/Desktop/Project/Dacon/AI_competition_to_predict_Arctic_sea_ice_using-_satellite_images/data'

train = pd.read_csv(PATH+'/train.csv')

print(train)


# sub = pd.read_csv(PATH+'/sample_submission.csv')

# sub = sub.drop(columns = "136193")

# list_train = sorted_list(os.path.join('/content/drive/MyDrive/dacon/artic_ice/train/', '*'))

# train.head(2)
    
    
    
    
# data=[]
# for files in tqdm(list_train):
#     data.append(np.load(files))
# data = np.array(data)
    
    
# tmpnpy = np.load(PATH+'/train/197811.npy')
# tmpnpy.shape
    
# print()
# for idx in range(train.shape[0]):
#     name_npy = train['file_nm'].iloc[idx]
#     tmpnpy = np.load(os.path.join(PATH+'/train', name_npy))
#     show_data(npy=tmpnpy)
#     if(idx == 1): break
    
    