import numpy

def preprocess(input):
    input = input.resize([28,28])
    input = input.convert('L')
    input = convert2np(input)
    input = float(input/255)
    print(input)
    input = input.reshape([1, 784])
    return input

def convert2np(input):
    return numpy.array(input)