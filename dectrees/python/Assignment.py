import monkdata as m
import dtree as tree
import drawtree_qt5 as draw

#draw.drawTree(m.monk1)
# print(tree.entropy(m.monk1) ) 
# print(tree.entropy(m.monk2) )
# print(tree.entropy(m.monk3) ) 
# for j in range (1,6):
#     print("monk1", tree.averageGain(m.monk1,m.attributes[j]), "attribute a", j )
#     print("monk2", tree.averageGain(m.monk2,m.attributes[j]), "attribute a", j )
#     print("monk3", tree.averageGain(m.monk3,m.attributes[j]), "attribute a", j )

t1= tree.buildTree(m.monk1, m.attributes)
t2= tree.buildTree(m.monk2, m.attributes)
t3= tree.buildTree(m.monk3, m.attributes)

print(tree.select(m.monk1,m.attributes[1],2))
# print(tree.mostCommon(m.monk1))
# print(tree.check(t1, m.monk1test))
# print(tree.check(t2, m.monk2test))
# print(tree.check(t3, m.monk3test))
