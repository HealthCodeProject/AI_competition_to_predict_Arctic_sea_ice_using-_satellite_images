import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import gc
import os

%matplotlib inline

train = pd.read_csv("D:/R_data/train.csv")
submission = pd.read_csv('D:/R_data/sample_submission.csv')

data = []
for filename in range(len(train)):
    data.append(np.load("D:/R_data/train/{0}".format(train['file_nm'][filename])))

data = np.array(data)
np.shape(data)

fig = plt.figure(figsize=(20,50))

for i in range(len(data)):
    for iter in range(5):
        fig.add_subplot(1, 5, iter+1)
        plt.imshow(data[i,:,:,iter])
        



#해빙/북극점/해안/지면/결측치 데이터 분리
thaw = pd.DataFrame()
thaw_pluse_pole = pd.DataFrame()

total_data=[]
for iter in range(0, train.shape[0]):
    data = np.load("D:/R_data/train/{0}".format(train['file_nm'][iter]))
    total_data.append(data)
    thaw = pd.concat([thaw, pd.DataFrame(data[:,:,0].reshape(1,-1))], ignore_index = True)
    thaw_pluse_pole = pd.concat([thaw_pluse_pole, pd.DataFrame(data[:,:,1].reshape(1,-1))], ignore_index = True)
 
total_data = np.array(total_data)


#월별 해빙농도의 합 계산
thaw_sum = []
thaw_sum = np.array(thaw.sum(axis=1))


# 해빙농도 합의 변화
plt.figure(figsize = (20,10))
plt.title('Thaw Changes over time (from 1979-01 to 2018-12)')
plt.plot(train['month'], thaw_sum)

def moving_average_forecast(series, window_size):
    """Forecasts the mean of the last few values.
    If window_size=1, then this is equivalent to naive forecast"""
    forecast = []
    for time in range(len(series)-window_size):
        forecast.append(series[time:time + window_size].mean())
    return np.array(forecast)

# 계절성 제거 후 변화 추이 확인
moving_avg = moving_average_forecast(thaw_sum, 12)

plt.figure(figsize=(20,10))
plt.title('Thaw Moving Average over time (from 1978-11 to 2018-12)')
plt.plot(train['month'][12:], moving_avg)

total_data = np.array(total_data)
total_data.shape

# 빙하의 감소추세가 잘 보이지 않는 이유
fig = plt.figure(figsize = (20,50))
for iter in range(0, total_data.shape[0]):
    fig.add_subplot(41,12,iter+1)
    plt.imshow(total_data[iter,:,:,1])



# 북극점 미관측지역을 결빙도 250으로 채워서 해빙데이터에 더해준다.
thaw_pluse_pole =  total_data[:,:,:,0] + total_data[:,:,:,1]*250

plt.figure(figsize=(10,10))
plt.imshow(thaw_pluse_pole[0,:,:])

thaw_pluse_pole = thaw_pluse_pole.reshape(thaw_pluse_pole.shape[0], thaw_pluse_pole.shape[1]*thaw_pluse_pole.shape[2])
thaw_pluse_pole.shape
thaw_pluse_pole_sum = []
thaw_pluse_pole_sum = np.array(thaw_pluse_pole.sum(axis=1))

## 미관측 영역을 결빙도 250으로 전부 채운 후 그린 결빙도 합의 그래프
plt.figure(figsize = (20,10))
plt.title('Thaw plus pole Changes over time(from 1978-11 to 2018-12)')
plt.plot(train['month'], thaw_pluse_pole_sum)
plt.show()
