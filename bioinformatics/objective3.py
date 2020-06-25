import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import time

#Develop a Python program that uses the WPGMA algorithm to draw a phylogenetic
#tree from an input matrix of inter-species distance


def WPGMA(filename):

    start = time.time()

    #Reads inter-species distance matrix from text file, and print matrix to screen
    DisMat = open(filename).read()
    DisMat = [item.split() for item in DisMat.split('\n')]
    print(np.array(DisMat))

    #Create tree
    G = nx.Graph()

    #Follow the WPGMA algorithm, and print out to the screen every reduced distance matrix
    while len(DisMat) > 2:

        #Finds minimum integer (!= 0) in Distance Matrix
        ColSkip = 2
        LenDisMat = len(DisMat)
        MinVal = float('inf')
        RowMinVal, ColMinVal = 0, 0
        for row in range(1,LenDisMat):
            for col in range(ColSkip,LenDisMat):
                CurVal = float(DisMat[row][col])
                if CurVal < MinVal:
                    MinVal = CurVal
                    RowMinVal, ColMinVal = row, col
            ColSkip += 1

        #Create new species
        Spec1 = DisMat[RowMinVal][0]
        Spec2 = DisMat[0][ColMinVal]
        NewSpec = Spec1 + Spec2

        #Add nodes and edges to graph
        LenSpec1 = len(Spec1)
        LenSpec2 = len(Spec2)

        if LenSpec1 == 1:
            G.add_node(Spec1)
        if LenSpec2 == 1:
            G.add_node(Spec2)
        G.add_node(NewSpec)
        G.add_edge(NewSpec, Spec1)
        G.add_edge(NewSpec, Spec2)

        #Creates new distance matrix
        DisMat[ColMinVal][0] = NewSpec
        DisMat[0][ColMinVal] = NewSpec
        for col in range(1,LenDisMat):
            if col == ColMinVal:
                DisMat[ColMinVal][col] = 0
            else:
                NewVal = (float(DisMat[ColMinVal][col]) + float(DisMat[RowMinVal][col]))/2
                NewVal = formatNumber(NewVal)
                DisMat[ColMinVal][col] = NewVal
                DisMat[col][ColMinVal] = NewVal
        del DisMat[RowMinVal]
        for row in DisMat:
            del row[RowMinVal]

        print(np.array(DisMat))

    pos = MakeTree(G,NewSpec)

    #Draw the phylogentic tree obtained to a file
    nx.draw(G, pos, with_labels = True)
    plt.savefig("Objective3_output_dwdj32.png", format="PNG")

    #Print out execution time to screen
    stop = time.time()
    print('Execution time:', stop-start)



#Formats number in matrix so decimal .0 doesn't show in distance matrices
def formatNumber(num):
  if num % 1 == 0:
    return int(num)
  else:
    return num

#Arranges graph into tree
def MakeTree(G, root, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5, pos = {}, parent = None):

    pos[root] = (xcenter, vert_loc)
    children = list(G.neighbors(root))
    if parent is not None:
        children.remove(parent)
    if len(children)!=0:
        dx = width/len(children)
        nextx = xcenter - width/2 - dx/2
        for child in children:
            nextx += dx
            pos = MakeTree(G,child, width = dx, vert_gap = vert_gap,
                                    vert_loc = vert_loc-vert_gap, xcenter=nextx,
                                    pos=pos, parent = root)
    return pos
