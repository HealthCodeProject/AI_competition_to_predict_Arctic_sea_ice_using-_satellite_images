# -*- coding: utf-8 -*-
"""
    data load
    
"""


import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#-----------------------------------------------------------------------------------#
## 폴더경로 지정
import os

PATH = (os.path.dirname(os.path.abspath(os.path.dirname(__file__))) 
        + "\\AI_competition_to_predict_Arctic_sea_ice_using_satellite_images\\data\\")


#-----------------------------------------------------------------------------------#
## train data file list
## 전체 데이터 dict에 담기

# file list
file_list = os.listdir(PATH + "train\\")

train_data_all = {}

for file_name in file_list:
    one_file_data = np.load(PATH + "train\\{}".format(file_name))
    train_data_all[file_name] = one_file_data
#-----------------------------------------------------------------------------------#


#-----------------------------------------------------------------------------------#
## 측청 불가 지점 채워주기
file_name_list = list(train_data_all.keys())

for num in range(len(file_name_list)):
    train_data_all[file_name_list[num]][:,:,1] \
    += train_data_all[file_name_list[num]][:,:,1]*250

#-----------------------------------------------------------------------------------#



#-----------------------------------------------------------------------------------#
## 이미지 출력

fig = plt.figure(figsize =  (20, 50))
for iter in range(5):
    fig.add_subplot(1, 5, iter+1)
    plt.imshow(train_data_month[:,:,iter])
fig.show()

#-----------------------------------------------------------------------------------#

