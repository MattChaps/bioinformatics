#!/usr/bin/python
import time
import sys

# YOUR FUNCTIONS GO HERE -------------------------------------
# 1. Populate the scoring matrix and the backtracking matrix

def PopulateMatrices(seq1,seq2):

    ScoreLst = [0]
    BackLst = ['END']

    for col in range(1,LenSeq2+1):
        ScoreLst.append(-2*col)
        BackLst.append('L')

    ScoreMat.append(ScoreLst)
    BackMat.append(BackLst)
            
    row = 1
    
    for Base1 in seq1:
        PrevScoreLst = ScoreLst
        PrevBackLst = BackLst
        ScoreLst = [-2*row]
        BackLst = ['U']
        col = 1
        
        for Base2 in seq2:
            if Base1 == Base2:
                if Base1 == 'A':
                    AlignmentScore = 4
                elif Base1 == 'C':
                    AlignmentScore = 3
                elif Base1 == 'G':
                    AlignmentScore = 2
                elif Base1 == 'T':
                    AlignmentScore = 1
            else:
                AlignmentScore = -3
                
            Scores = [\
                PrevScoreLst[col-1] + AlignmentScore, \
                PrevScoreLst[col] - 2, \
                ScoreLst[col-1] - 2 \
                ]

            MaxScore = max(Scores)
        
            ScoreIndex = Scores.index(MaxScore) 
        
            BackLetters = ['D','U','L']
            BackEntry = BackLetters[ScoreIndex]

            ScoreLst.append(MaxScore)
            BackLst.append(BackEntry)    
            
            col += 1

        ScoreMat.append(ScoreLst)
        BackMat.append(BackLst)

        row += 1

    return MaxScore 

# ------------------------------------------------------------

            

# DO NOT EDIT ------------------------------------------------
# Given an alignment, which is two strings, display it

def displayAlignment(alignment):
    string1 = alignment[0]
    string2 = alignment[1]
    string3 = ''
    for i in range(min(len(string1),len(string2))):
        if string1[i]==string2[i]:
            string3=string3+"|"
        else:
            string3=string3+" "
    print('Alignment ')
    print('String1: '+string1)
    print('         '+string3)
    print('String2: '+string2+'\n\n')

# ------------------------------------------------------------


# DO NOT EDIT ------------------------------------------------
# This opens the files, loads the sequences and starts the timer
file1 = open(sys.argv[1], 'r')
seq1=file1.read()
file1.close()
file2 = open(sys.argv[2], 'r')
seq2=file2.read()
file2.close()
start = time.time()

#-------------------------------------------------------------


# YOUR CODE GOES HERE ----------------------------------------
# The sequences are contained in the variables seq1 and seq2 from the code above.
# Intialise the scoring matrix and backtracking matrix and call the function to populate them
# Use the backtracking matrix to find the optimal alignment 
# To work with the printing functions below the best alignment should be called best_alignment and its score should be called best_score. 

#Initialise scoring matrix and backtracking matrix
BackMat = []
ScoreMat = []

#Populate matrices and calculate best score
LenSeq1 = len(seq1)
LenSeq2 = len(seq2)

best_score = PopulateMatrices(seq1,seq2)

#Use backtracking matrix to determine an optimal alignment
Alignment1 = ''
Alignment2 = ''

row = LenSeq1
col = LenSeq2
CurEntry = BackMat[row][col]

while CurEntry != 'END':
    CurBase1 = seq1[row-1]
    CurBase2 = seq2[col-1]
    if CurEntry == 'D':
        Alignment1 = CurBase1 + Alignment1
        Alignment2 = CurBase2 + Alignment2
        row += -1
        col += -1
    elif CurEntry == 'L':
        Alignment1 = '-' + Alignment1
        Alignment2 = CurBase2 + Alignment2
        col += -1
    elif CurEntry == 'U':
        Alignment1 = CurBase1 + Alignment1
        Alignment2 = '-' + Alignment2
        row += -1
    CurEntry = BackMat[row][col]
    
best_alignment = [Alignment1, Alignment2]

#-------------------------------------------------------------


# DO NOT EDIT (unless you want to turn off displaying alignments for large sequences)------------------
# This calculates the time taken and will print out useful information 
stop = time.time()
time_taken=stop-start

# Print out the best
print('Time taken: '+str(time_taken))
print('Best (score '+str(best_score)+'):')
displayAlignment(best_alignment)

#-------------------------------------------------------------

