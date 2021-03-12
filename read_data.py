# -*- coding: utf-8 -*-

"""
    Dacon Competitions
    위성 영상을 활용한 북극 해빙 예측 AI 경진대회
    작성일 : 2021년 3월 12일
    email : gksxorb147@gmail.com
    
"""

# 모듈 불러오기
import numpy as np
import os
import pandas as pd
from tqdm import tqdm # 루프에 스마트한 진행률 측정기가 즉시 표시되도록 합니다.
import seaborn as sns # 시각화 라이브러리
import matplotlib.pyplot as plt # 시각화 라이브러리
from pyprnt import prnt # 리스트구조 이쁘게 출력하기
import json



#-----------------------------------------------------------------------------------#
## 폴더의 종류별 리스트 출력하기

def list_extensions_dir(dir_path):
    
    """        
        폴더안의 파일들의 이름을 확장자 별로
        딕셔너리를 만들어 출력합니다.
        
        Dependency Module : os
    """

    extensions_list = [] ## 확장자를 담을 리스트
    dict_key_list = [] ## dict key lsit
    folder_list = {}
    
    file_list = os.listdir(dir_path) ## list 불러오기
    
    ## 폴더안의 확장자 추출
    for file_name in file_list:
        if len(file_name.split(".")) > 1:
            extensions_list.append(file_name.split(".")[-1])
        else:
            extensions_list.append("folder")
    
    dict_key_list = set(extensions_list)
    
    ## dict에 키 추가
    for file_extensions in dict_key_list:
        folder_list[file_extensions] = []
    
    
    ## folder_list 
    for num in range(len(extensions_list)):
        folder_list[extensions_list[num]].append(file_list[num])
        
    return folder_list
        
## 함수 호출



#-----------------------------------------------------------------------------------#



def show_json_data(json_dict):
    
    """----------------------------------------------------------------------
		#	   update : 2021-03-05 09:23
    #    contact : gksxorb147@gmail.com
    #    input : json 형식의 값
    #    output : json
    #    dependence module : json
    #    explanation : 일반적인 json 정보를 시각적으로 보기 쉽게 만드느 함수
    ----------------------------------------------------------------------"""

    print(json.dumps(dict(json_dict), indent=4))

    return json.dumps(dict(json_dict), indent=4)





prnt(list_extensions_dir('C:/Users/gksxo/Desktop/Project/Dacon_Data/AI_competition_to_predict_Arctic_sea_ice_using-_satellite_images/data'))



