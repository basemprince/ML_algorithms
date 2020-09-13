from __future__ import print_function
import monkdata as m
import dtree as tree
import drawtree_qt5 as draw
from tabulate import tabulate
import random
import numpy as np
import matplotlib.pyplot as plt
from time import sleep
import sys

iterations = 200
fractions = [0.3,0.4,0.5,0.6,0.7,0.8]

def partition(data, fraction):
	ldata = list(data)
	random.shuffle(ldata)
	breakPoint = int(len(ldata)*fraction)
	return ldata[:breakPoint], ldata[breakPoint:]

def assignment1():
    monk1 = ['MONK1']
    monk1.append(round(tree.entropy(m.monk1),5))
    monk2 = ['MONK2']
    monk2.append(round(tree.entropy(m.monk2),5))   
    monk3 = ['MONK3']
    monk3.append(round(tree.entropy(m.monk3),5))
    print(tabulate([monk1, monk2,monk3], headers=['Dataset', 'Entropy'], tablefmt='orgtbl'),'\n')
 
def assignment3():
    monk1 = ['monk1']
    monk2 = ['monk2']
    monk3 = ['monk3']
    for j in range (0,6):
        monk1.append(round(tree.averageGain(m.monk1,m.attributes[j]),5))
        monk2.append(round(tree.averageGain(m.monk2,m.attributes[j]),5))
        monk3.append(round(tree.averageGain(m.monk3,m.attributes[j]),5))
    print(tabulate([monk1, monk2,monk3], headers=['Dataset', 'a1','a2','a3','a4','a5','a6'], tablefmt='orgtbl'))

def assignment5(t,data,test):
    #check calculates the accuracy, 1-accuracy to get the error
    monk1 = ['MONK1',1-tree.check(t[0], data[0]),round(1-tree.check(t[0], test[0]),4)]
    monk2 = ['MONK2',1-tree.check(t[1], data[1]),round(1-tree.check(t[1], test[1]),4)]
    monk3 = ['MONK3',1-tree.check(t[2], data[2]),round(1-tree.check(t[2], test[2]),4)]
    print(tabulate([monk1, monk2,monk3], headers=['Dataset', 'Error-train','Error-test'], tablefmt='orgtbl'),'\n')
    #draw.drawTree(t[0])
    #draw.drawTree(t[1])
    draw.drawTree(t[2])

def assignment7(t,data,test):
    #prune MONK
    classError1B= []
    classError3B= []
    classError1A= []
    classError3A= []
    for fraction in fractions:
        #prunning and getting class error for MONK1 set   
        errorB,errorA=prune(t[0],data[0],test[0],fraction,1)
        classError1B.append(errorB)
        classError1A.append(errorA)
        errorB,errorA=prune(t[2],data[2],test[2],fraction,3)
        classError3B.append(errorB)
        classError3A.append(errorA)
    plt.style.use('ggplot')
    fig1= plt.figure(1,figsize=(10,15))
    MONK1 = fig1.add_subplot(211)
    MONK3 = fig1.add_subplot(212)
    MONK1.plot(fractions,classError1B,marker='o',label='Before Pruning')
    MONK1.plot(fractions,classError1A,marker='o',label='After Pruning')
    MONK1.set_title('MONK1 - Classification Error Vs Fraction')
    MONK1.set(xlabel='Fractions', ylabel='Classification Error')
    MONK1.legend()
    MONK3.plot(fractions,classError3B,color= 'red',marker='o',label='Before Pruning')
    MONK3.plot(fractions,classError3A,color= 'black',marker='o',label='After Pruning')
    MONK3.set_title('MONK3 - Classification Error Vs Fraction')
    MONK3.set(xlabel='Fractions', ylabel='Classification Error')
    MONK3.legend()
    plt.savefig('plot.png')
    plt.show()

    
def prune(t,data,test,fraction,monk):
    errorArrayA = []
    errorArrayB = []
    for iteration in range (iterations):
        sys.stdout.write('\r')
        sys.stdout.write("Pruning MONK-%d with partition %.2f: iteration %d out of %d" % (monk,fraction,iteration, iterations))
        sys.stdout.flush()
        resultBuffer = 0
        ttrain,tvalidate= partition(data,fraction)
        newTree = tree.buildTree(ttrain, m.attributes)
        errorB = 1-tree.check(newTree,test)
        errorArrayB.append(errorB)
        newPrunedTrees = tree.allPruned(newTree)
        for newPrunedTree in newPrunedTrees:
            #Check performance on validation dataset
            checkResult=tree.check(newPrunedTree, tvalidate)
            if checkResult > resultBuffer:
                resultBuffer = checkResult
                bestTree = newPrunedTree
        errorA = 1-tree.check(bestTree,test)
        errorArrayA.append(errorA)
    sys.stdout.write('\n')
    return np.mean(errorArrayB),np.mean(errorArrayA)

def main():
    t = [tree.buildTree(m.monk1, m.attributes),tree.buildTree(m.monk2, m.attributes),tree.buildTree(m.monk3, m.attributes)]
    data = [m.monk1,m.monk2,m.monk3]
    test = [m.monk1test,m.monk2test,m.monk3test]
    assignment1()
    assignment3()
    assignment5(t,data,test)
    assignment7(t,data,test)

main()