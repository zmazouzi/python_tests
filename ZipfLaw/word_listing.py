

/*

Zipf's law 

this code demonstrates the validity of Zipf's law wich is an emprirical law formulated using mathematical statstics that refers to the fact that many types of data  studied in the physical and social sciences can be approximated with a Zipfian distribution .

OUTPUT : 

 plotting the data on a log-log graph, with the axes being log (rank order of the word ) and log (frequency).

*/

from matplotlib import pyplot as ploter
from matplotlib import  style
from math import log

style.use("ggplot")
def test(x):
    a =x.lower()
    if (a >= "a" and a <= "z"):
        return True
    else:
        return False

def test_word(word):

    flag = False
    for i in word:
        if(test(i) == True):
            flag = True
            continue
        else:
            flag = False
            break
    return flag

def healing(word):
    mot = ""
    for i in word:
        if(test(i)):
            mot= mot+i
    return mot

fr = open("sample.txt","r")
x = str(fr.read())
word_list = x.split()
list = []
for i in word_list:
    if(i!="\s"):
        if (test_word(i) == True):
            list.append(i)
        else:
            list.append(healing(i))
    else:
        pass

def occurence(list):
    dico ={}
    for i in list:
        if( i in dico.keys()):
            dico[i]+=1
        else:
            dico[i]=1
    return dico
dico = occurence(list)

x = []
y = []

for j in dico.values():
    y.append(log(j))
x.append(0)
for i in range(1,len(dico)):
    x.append(log(i))
y.sort()
y.reverse()
ploter.plot(x,y,linewidth=2,label="the variation of words")
ploter.show()
print(dico)
ploter.legend()
fr.close()
