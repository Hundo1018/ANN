import math
import abc

#分類用
def SoftMax(x):
    xExp = list(map(lambda i:math.exp(i),x))
    sumxExp = sum(xExp)
    softMax = list(map(lambda i: round(i / sumxExp, 3), xExp))
    return softMax

#還不會寫，但也是多輸入的一種
def MaxOut(x):
    return x

#就線性
def Identity(x):
    return x

#
def ReLU(x):
    return max(0, x)