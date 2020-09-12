from __future__ import print_function
import monkdata as m
import dtree as tree
import drawtree_qt5 as draw
from tabulate import tabulate

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

def assignment5():
    t1= tree.buildTree(m.monk1, m.attributes)
    t2= tree.buildTree(m.monk2, m.attributes)
    t3= tree.buildTree(m.monk3, m.attributes)
    monk1 = ['MONK1',1-tree.check(t1, m.monk1),round(1-tree.check(t1, m.monk1test),4)]
    monk2 = ['MONK2',1-tree.check(t2, m.monk2),round(1-tree.check(t2, m.monk2test),4)]
    monk3 = ['MONK3',1-tree.check(t3, m.monk3),round(1-tree.check(t3, m.monk3test),4)]
    print(tabulate([monk1, monk2,monk3], headers=['Dataset', 'Error-train','Error-test'], tablefmt='orgtbl'),'\n')
    draw.drawTree(t1)
    draw.drawTree(t2)
    draw.drawTree(t3)
#print(tree.select(m.monk1,m.attributes[1],2))
# print(tree.mostCommon(m.monk1))

#assignment1()
#assignment3()
assignment5()