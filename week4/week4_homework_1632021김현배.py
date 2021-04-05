'''
csv 파일은 comma-separated values의 약자로써, 쉼표(,)로 구분된 데이터 파일입니다.
(MS excel에서 파일을 열어볼 수 있습니다.)
해당 파일에는 아래와 같이 1599종의 레드와인에 대해 11가지 특성과, 마지막 열에 1개의 품질점수가 기록되어 있습니다. (1599x12 배열)
첨부된 레드와인 데이터를 파이썬으로 읽어들여
가로축은 와인 1599개(모든 행), 세로축은 각각의 특성 및 품질점수(모든 열)로 하여 그래프를 그리세요.
일례로, 0번 특성인 fixed acidity에 대해 그래프를 그리면 다음과 같겠습니다.
특성이 11개, 품질점수가 1개이므로 총 12개의 그래프가 그려지게 될 것입니다.
- csv 파일을 읽어들이는 법은 인터넷에 많이 나와있으니 참고하시기 바랍니다. (팁, import csv 혹은 import pandas as pd 를 이용)
- 첨부된 csv파일의 맨 첫 행은 string(문자열)임에 주의하세요.
- matplotlib의 subplots/subplot을 잘 활용하세요.
'''

# winequality-red.csv 파일 불러오기
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# csv파일 불러오기
csv_data = pd.read_csv('winequality-red.csv', encoding='euc-kr',sep=',')

name = csv_data.loc[0]

'''
#열데이터 불러오기 1
fixed_ = csv_data['fixed acidity']
print(fixed)
'''

#열데이터 불러오기 2
fixed = csv_data.loc[:, 'fixed acidity']
# print(fixed1)
volatile = csv_data.loc[:, 'volatile acidity']
citric = csv_data.loc[:, 'citric acid']
residual = csv_data.loc[:, 'residual sugar']
chlorides = csv_data.loc[:, 'chlorides']
free = csv_data.loc[:, 'free sulfur dioxide']
total = csv_data.loc[:, 'total sulfur dioxide']
density = csv_data.loc[:, 'density']
ph = csv_data.loc[:, 'pH']
sulphates = csv_data.loc[:, 'sulphates']
alcohol = csv_data.loc[:, 'alcohol']
quality = csv_data.loc[:, 'quality']

#subplots를 이용한 그래프 그리기
fig, axes = plt.subplots(4, 3, figsize = (20, 10))
axes[0, 0].plot(fixed, c='b', marker = 'x', ls = ':', ms=5, mec = 'k')
axes[0, 0].set_title("axes 1.1")
axes[0, 0].set_ylabel("Fixed acidity")
axes[0, 0].set_xlabel("#wine")


axes[0, 1].plot(volatile, c='g', marker = 'o', ls = '--', ms=5, mec = 'k')
axes[0, 1].set_title("axes 1.2")
axes[0, 1].set_ylabel("Volatile acidity")
axes[0, 1].set_xlabel("#wine")

axes[0, 2].plot(citric, c='r', marker='v', ls = '-', ms=5, mec='k')
axes[0, 2].set_title("axes 1.3")
axes[0, 2].set_ylabel("Citric acid")
axes[0, 2].set_xlabel("#wine")

axes[1, 0].plot(residual, c='c', marker='^', ls='-.', ms=5, mec='k')
axes[1, 0].set_title("axes 2.1")
axes[1, 0].set_ylabel("Residual sugar")
axes[1, 0].set_xlabel("#wine")

axes[1, 1].plot(chlorides, c='m', marker='>', ms=5, mec='k')
axes[1, 1].set_title("axes 2.2")
axes[1, 1].set_ylabel("Chlorides")
axes[1, 1].set_xlabel("#wine")

axes[1, 2].plot(free, c='y', marker='1', ms=5, mec='k')
axes[1, 2].set_title("axes 2.3")
axes[1, 2].set_ylabel("Free sulfur dioxide")
axes[1, 2].set_xlabel("#wine")

axes[2, 0].plot(total, c='w', marker='d', ms=5, mec='k')
axes[2, 0].set_title("axes 3.1")
axes[2, 0].set_ylabel("Total sulfur dioxide")
axes[2, 0].set_xlabel("#wine")

axes[2, 1].plot(density, c='g', marker='s', ms=5, mec='k')
axes[2, 1].set_title("axes 3.2")
axes[2, 1].set_ylabel("Density")
axes[2, 1].set_xlabel("#wine")

axes[2, 2].plot(ph, c='y', marker='h', ms=5, mec='k')
axes[2, 2].set_title("axes 3.3")
axes[2, 2].set_ylabel("pH")
axes[2, 2].set_xlabel("#wine")

axes[3, 0].plot(sulphates, c='c', ls='--', marker='+', ms=5, mec='k')
axes[3, 0].set_title("axes 4.1")
axes[3, 0].set_ylabel("Sulphates")
axes[3, 0].set_xlabel("#wine")

axes[3, 1].plot(alcohol, c='m', ls=':', marker='p', ms=5, mec='k')
axes[3, 1].set_title("axes 4.2")
axes[3, 1].set_ylabel("Alcohol")
axes[3, 1].set_xlabel("#wine")

axes[3, 2].plot(quality, c='r', ls='-.', marker='.', ms=5, mec='k')
axes[3, 2].set_title("axes 4.3")
axes[3, 2].set_ylabel("Quality")
axes[3, 2].set_xlabel("#wine")

plt.tight_layout()
plt.show()