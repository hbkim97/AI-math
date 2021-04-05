import numpy as np

a = [1,2,3] #list
b = [4,5,6] #list -> 배열이 아니다!

# 배열 -> 1+4 / 2+5 / 3+6
# 리스트 -> 1,2,3,4,5,6
print(a + b) #a,b는 배열 x

c = np.array([1,2,3])
d = np.array([4,5,6])

print(c+d) #c,d는 배열 o

# 1차원 배열
arr = np.array([0,2,3,4,5,6,7,8,9])
print(type(arr))

# 2차원 배열
arr2 = np.array([[0,1,2],[3,4,5]])
print(len(arr2)) #low : 행
print(len(arr2[0])) #colume : 열
print(arr2.shape) #2x3

# 3차원 배열
arr3 = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],            #arr3[0]
                [[11,12,13,14],[15,16,17,18],[19,20,21,22]]])   #arr3[1]
print(len(arr3)) #row : 행
print(len(arr3[0])) #column : 열
print(len(arr3[0][0])) #depth : 깊이
print(arr3.shape) #shape

# 디버깅이랑 친해지면 위처럼 print하지 않아도 이해하기 좋다.


arr4 = np.array([[0,1,2,3], [4,5,6,7]])
print(arr4[:,0:2])