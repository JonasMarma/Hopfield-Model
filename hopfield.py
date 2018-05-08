# coding: UTF-8

import numpy as np
import matplotlib.pyplot as plt


class Hopfield(object):
    def __init__(self):
        self.__weights = []
        self.__finalWeights = []

    def make_weight_pattern(self, prototype, view, patNo):
        H = np.zeros((prototype.size, prototype.size))

        # Normalize the weights
        # Normalizar os pesos -1 e 1 apenas
        prototype[prototype > 0] = 1
        prototype[prototype <= 0] = -1

        prototype = prototype.flatten()

        # W_ij = P_i * P_j
        for i in range(prototype.size):
            for j in range(prototype.size):
                if view == True:
            	    print('Pattern #{}'.format(patNo))
            	    print('Processing cell: {}/{}'.format(i,j))
                H[i][j] = prototype[i] * prototype[j]

        return H

    def memorize_patterns(self, patterns, view):
        # Create a weight matrix for each prototype
        # Criar uma matriz de peso para cada protótipo
        patNo = 1
        for pattern in patterns:
            weight = self.make_weight_pattern(pattern, view, patNo)
            self.__weights.append(weight)
            patNo += 1

        # Sum all the weights matrices
        # Fazer a soma de todas as matrizes de pesos
        self.__finalWeights = self.__weights[0]
        for weight in self.__weights:
            self.__finalWeights = self.__finalWeights + weight
        self.__finalWeights = self.__finalWeights - self.__weights[0]

    def update(self, inputArray):
        #Reshaping the input a preparing the output...
        #Reformatando o input a preparando o output...
        originalShape = inputArray.shape
        inputArray = inputArray.flatten()
        output = np.zeros(inputArray.shape)
        
        #For each pixel, calculate the total interaction with all the other pixels and decide a new value
        #Em cada pixel, calcular a interação total com todos os outros pixels e decidir o novo valor
        for i in range(len(inputArray)):
            interactions = 0
            for j in range(len(inputArray)):
                interactions += self.__finalWeights[i][j]*inputArray[j]
            if interactions > 0:
                output[i] = +1
            else:
                output[i] = -1
        
        output = output.reshape(originalShape)
        return output

    def show_patterns(self):
        count = 1
        for w in self.__weights:
            plt.imshow(w,
                       cmap=plt.cm.BuPu_r,
                       interpolation='none')
            plt.title('Weight matrix for pattern #{}:'.format(count))
            plt.show()
            count += 1

        plt.imshow(self.__finalWeights,
                   cmap=plt.cm.BuPu_r,
                   interpolation='none')
        plt.title('Final weights matrix:')

        plt.show()


