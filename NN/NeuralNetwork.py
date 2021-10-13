from NN.Layer import Layer
from functools import reduce

class NeuralNetwork:
    
    __layers = []
    
    #通過目前的資料計算數值
    def Predict(self, x):
        if self.__layers[0].GetNeuronNum() != len(x):
            raise ValueError("輸入向量維度錯誤")

        y = reduce(lambda lastResult,
                   nextLayer: nextLayer.Forward(lastResult), self.__layers[1:], x)
        return y

    #新增全連接層
    def Add(self,layer):
        #層數大於0時，加入後連接在一起
        if len(self.__layers):
            #設定新加入的層 的 每個神經元權重數 為 前一層神經元數量
            layer.Set(self.__layers[-1].GetNeuronNum())
        else:
            layer.Set(0)
        self.__layers.append(layer)
    
    #顯示結構與參數
    def PrintStructureParameters(self,roundNum):
        for l in self.__layers:
            l.PrintParameters(roundNum)

    def __init__(self):
        pass
