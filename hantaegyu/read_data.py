# -*- coding: utf-8 -*-

"""
    Dacon Competitions
    위성 영상을 활용한 북극 해빙 예측 AI 경진대회
    작성일 : 2021년 3월 12일
    email : gksxorb147@gmail.com
    
"""

# 모듈 불러오기
from pathlib import Path


class DATA():
    
    def __init__(self):

        self.PROJECT_PATH = Path( "C:\\Users\\gksxo\\Desktop\\Project\\Dacon"
                                + "\\AI_competition_to_predict_Arctic_sea_ice_using-_satellite_images")
        
        self.FD_PATH      = self.PROJECT_PATH / Path("data")
        
        self.TRAIN_FD     = self.FD_PATH / Path("train")
        
        self.SAMPLE_CSV   = self.FD_PATH / Path("sample_submission.csv")
        
        self.TRAIN_CSV    = self.FD_PATH / Path("train.csv")
        
        



DATA = DATA()


print(DATA.SAMPLE_CSV)

