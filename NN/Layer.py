from NN.Neuron import Neuron
from functools import reduce 
from NN.Activation import * 
import random

class Layer:
    __name = ''
    __bias = .0
    __activation = None
    __neurons = []
    __neuronNum = 0

    
    #資料正向傳遞進入此層
    def Forward(self, x):
        ys = []
        if self.__activation is SoftMax:#softMax 為多輸入函數
            for neuron in self.__neurons:
                ys.append(neuron.Forward(x) + self.__bias)
            return self.__activation(ys)
        else:#其他的單輸入函數 如RELU
            for neuron in self.__neurons:
                ys.append(self.__activation(neuron.Forward(x) + self.__bias))
            return ys
    

    #前一層有幾顆神經元
    def Set(self, num):
        self.__neurons = []
        for i in range(self.__neuronNum):
            self.__neurons.append(Neuron(num))
        pass

    def GetWeights(self):
        return [i.GetWeights() for i in self.__neurons]

    def GetBias(self):
        return self.__bias

    def GetNeuronNum(self):
        return self.__neuronNum

    def GetName(self):
        return self.__name

    def PrintParameters(self, roundNum):
        nl = []
        for n in self.__neurons:
            nl.append( list( map(lambda x: round( x , roundNum), n.GetWeights())))
        print(nl,'bias:',round(self.__bias,roundNum))

    def __init__(self, num, activation,name):
        self.__neuronNum = num
        self.__activation = activation
        self.__name = name        
        self.__bias = random.random()-0.5

        pass
