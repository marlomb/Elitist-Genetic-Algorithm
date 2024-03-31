#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 13:19:00 2024

@author: marlombey
"""

import random
from tqdm import tqdm
import matplotlib.pyplot as plt


#---Binary GA for Minimization Problem-----#

def fitness(c):
    
    return sum(c)
    

def population(pSize, dSize):
    
    pop = []
    
    for _ in tqdm(range(pSize)):
        p = []
        for _ in range(dSize):
            p.append(random.randint(0, 1))
        pop.append(p)
    
    return pop

def selection(pop, fValue):
    
    f1 = 100
    f2 = 100
    
    for f in fValue:
        if f < f1:
            f2 = f1
            f1 = f
        if f < f2 and f > f1:
            f2 = f
    
    i1 = fValue.index(f1)
    i2 = fValue.index(f2)
    
    return pop[i1], pop[i2]

def crossover(p1, p2):
    
    c1 = [0 for _ in range(len(p1))]
    c2 = [0 for _ in range(len(p1))]
    
    point = random.randint(0, len(p1))
    
    c1[:point] = p1[:point]
    c1[point+1:len(p1)+1] = p2[point+1:]
    
    c2[:point] = p2[:point]
    c2[point+1:] = p1[point+1:len(p1)]
    
    return c1, c2

def mutation(c1, c2):
    
    point = random.randint(0, len(c1)-1)
    
    if c1[point] == 0:
        #print('Mutating c1 bit 0')
        c1[point] = 1
    elif c1[point] == 1:
        #print('Mutating c2 bit 1')
        c1[point] = 0
    
    if c2[point] == 0:
        #print('Mutating c2 bit 0')
        c2[point] = 1
    elif c2[point] == 1:
        #print('Mutating c2 bit 0')
        c2[point] = 0
    
    return c1, c2
        

if __name__ == '__main__':
    
    pSize = 100
    dSize = 100
    maxIte = 200
    bestFitness = []
    bestSolution = []
    print('---Generating Population---')
    pop = population(pSize, dSize)
    
    '''print('---Calculating Fitness---')
    fValue = []
    for p in tqdm(pop):
        fValue.append(fitness(p))'''
    
    print('---Starting Main Loop---')
    for _ in tqdm(range(maxIte)):
        
        fValue = []
        for p in pop:
            fValue.append(fitness(p))
            
        p1, p2 = selection(pop, fValue)
        
        #print('p1', p1)
        #print('p2', p2)
        
        c1, c2 = crossover(p1, p2)
        #print('c1', c1)
        #print('c2', c2)
        
        m1, m2 = mutation(c1, c2)
        
        #print('m1', m1)
        #print('m2', m2)
        
        #print(pop[pop.index(p1)])
        print(pop[pop.index(p2)])
        
        if fitness(m1) < fitness(p1):
            pop[pop.index(p1)] = m1
        if fitness(m2) < fitness(p2):
            pop[pop.index(p2)] = m2
        
        fValue = []
        for p in pop:
            fValue.append(fitness(p))
        
        minF = min(fValue)
        minFIndex = fValue.index(minF)
        bestC = pop[minFIndex]
        
        bestFitness.append(minF)
        bestSolution.append(bestC)
    
    x = []
    y = []
    fig, ax = plt.subplots()
    
    for i in range(maxIte):
        plt.clf()
        
        x.append(i+1)
        y.append(bestFitness[i])
        
        plt.xlim(1, maxIte)
        plt.ylim(1, dSize)
        plt.title('Visual Representation of GA Fitness')
        plt.xlabel('Generations')
        plt.ylabel('Fitness Value')
        plt.plot(x,y, c='red', linewidth = 2)
        plt.pause(0.01)
    
    plt.show()
    
    print('Best Chromose: {}'.format(bestSolution[len(bestSolution)-1]))
