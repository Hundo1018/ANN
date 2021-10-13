from NN import *

def main():
    nn = NeuralNetwork()
    nn.Add(Layer(2, ReLU,'0'))
    nn.Add(Layer(3, ReLU,'1'))
    nn.Add(Layer(1, ReLU,'2'))
    y = nn.Predict([0,1])
    #nn.PrintStructureParameters(3)
    #print(y)


    pass
main()
