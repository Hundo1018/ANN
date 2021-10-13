import random 

class Neuron:
    
    __weights = []

    #神經元計算
    def Forward(self, x):
        #輸入向量xi*wi
        #加總=wx
        wx = sum([self.__weights[i] * x[i] for i in range(len(x))])
        return wx

    def GetWeights(self):
        return self.__weights
    
    #前一層的神經元數量
    def __init__(self, num):
        self.__weights = []
        #暫時以0~1作為預設值
        random.seed()
        for i in range(num):
            self.__weights.append(random.random()-0.5)
