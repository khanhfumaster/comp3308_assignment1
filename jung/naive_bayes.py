import copy
import numpy
from math import sqrt, exp, pi
from random import randint

class naiveBayes():
    def __init__(self):
        self.type = 'naive bayes'

    # P(class)
    def p_class(self, classifier):
        count = 0.0
        total = float(len(self.training_data))
        for instance in self.training_data:
            if instance['class'] == classifier:
                count += 1
        return count/total

    # P(E = x|class)
    def p_e_class(self, key, val, classifier):
        keys = []
        for instance in self.training_data:
            if instance['class'] == classifier:
                keys.append(instance[key])
        mean = numpy.mean(keys)
        std = numpy.std(keys)
        return 1/(std * sqrt(2*pi)) * exp(-((val-mean)**2)/(2*(std**2)))
    
    def classify(self, new_instance):
        results = {}
        for classifier in ['class0', 'class1']:
            p = self.p_class(classifier)
            for attr in new_instance:
                p *= self.p_e_class(attr, new_instance[attr], classifier)
            results[classifier] = p

        if results['class0'] == results['class1']:
            rand = randint(0, 1)
            if rand == 0:
                return 'class0'
            if rand == 1:
                return 'class1'
        elif results['class0'] > results['class1']:
            return 'class0'
        elif results['class0'] < results['class1']:
            return 'class1'
            
