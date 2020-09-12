from __future__ import print_function
import monkdata as m
import dtree as tree
import drawtree_qt5 as draw
from tabulate import tabulate
import random
import numpy as np

iterations = 200
fraction = [0.3,0.4,0.5,0.6,0.7,0.8]

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
    monk1 = ['MONK1',1-tree.check(t[0], data[0]),round(1-tree.check(t[0], test[0]),4)]
    monk2 = ['MONK2',1-tree.check(t[1], data[1]),round(1-tree.check(t[1], test[1]),4)]
    monk3 = ['MONK3',1-tree.check(t[2], data[2]),round(1-tree.check(t[2], test[2]),4)]
    print(tabulate([monk1, monk2,monk3], headers=['Dataset', 'Error-train','Error-test'], tablefmt='orgtbl'),'\n')
    draw.drawTree(t[0])
    draw.drawTree(t[1])
    draw.drawTree(t[2])

def assignment7(t,data,test):
    #prune MONK1
    prune(t[0],data[0],test[0])

def prune(t,data,test):
    errorArray = []
    for iteration in range (iterations):
        resultBuffer = 0
        ttrain,tvalidate= partition(data,fraction[0])
        newTree = tree.buildTree(ttrain, m.attributes)
        newPrunedTrees = tree.allPruned(newTree)
        for newPrunedTree in newPrunedTrees:
            #Check performance on validation dataset
            checkResult=tree.check(newPrunedTree, tvalidate)
            
            if checkResult > resultBuffer:
                resultBuffer = checkResult
                bestTree = newPrunedTree

		error = 1-tree.check(bestTree, test)
		errorArray.append(error)
    return np.mean(errorArray), np.var(errorArray)

def main():
    t = [tree.buildTree(m.monk1, m.attributes),tree.buildTree(m.monk2, m.attributes),tree.buildTree(m.monk3, m.attributes)]
    data = [m.monk1,m.monk2,m.monk3]
    test = [m.monk1test,m.monk2test,m.monk3test]
    #assignment1()
    #assignment3()
    assignment5(t,data,test)
    assignment7(t,data,test)

main()