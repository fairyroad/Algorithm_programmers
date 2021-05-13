#numpy를 사용하기 위해서 np.array로 arr1,arr2를 바꿔주고
#행렬의 곱을 계산해주는 matmul을 이용해서 행렬의 곱셈을 계산한 이후에 
#tolist()를 이용해서 type을 맞추어 줌
import numpy as np
def solution(arr1, arr2):
    return np.matmul(np.array(arr1),np.array(arr2)).tolist()
