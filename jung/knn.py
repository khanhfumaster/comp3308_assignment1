import copy
from math import sqrt
from operator import itemgetter
from random import randint

class kNN:
    def __init__(self):
        self.type = 'knn'
        
    def classify(self, new_instance):
        for instance in self.training_data:
            distance = 0.0
            for attr in instance:
                if attr != 'class' and attr != 'distance':
                    distance += (instance[attr] - new_instance[attr])**2
            instance['distance'] = sqrt(distance)

        sorted_list = sorted(self.training_data, key=itemgetter('distance'))
        class0_count = 0
        class1_count = 0

        for neighbour in sorted_list[:self.k]:
            if neighbour['class'] == 'class0':
                class0_count += 1
            if neighbour['class'] == 'class1':
                class1_count += 1

        if class0_count == class1_count:
            rand = randint(0, 1)
            if rand == 0:
                return 'class0'
            if rand == 1:
                return 'class1'
        elif class0_count > class1_count:
            return 'class0'
        elif class1_count > class0_count:
            return 'class1'
