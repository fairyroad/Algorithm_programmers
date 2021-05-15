#(yellow의 가로 + yellow의 세로) * 2 + 4 == brown의 block개수
#yellow의 약수들이 가로와 세로의 후보들이 됨
def solution(brown, yellow):
    width = 1
    height = 1
    while height*height <= yellow:
        if yellow % height == 0:
            width = yellow/height
            if (width+height)*2 + 4 == brown:
                return [width+2, height+2]
        height+=1
