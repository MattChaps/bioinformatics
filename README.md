# Bioinformatics

## Objective 1: Python Programming to align two DNA sequences

Develop a Python program that uses Dynamic Programming to compute the optimal alignment of two sequences.

It should meet the following conditions:

- The algorithm should read in two sequences (may be of different lengths) from text files.

- Initialise the scoring matrix and the backtracking matrix.

- Score each alignment using the following scores:

  - +4 for a matching pair of ’A’ bases,
  - +3 for a matching pair of ’C’ bases,
  - +2 for a matching pair of ’G’ bases,
  - +1 for a matching pair of ’T’ bases,
  - -3 for a mismatching pair of bases,
  - -2 for a gap.

- Use the backtracking matrix to determine an optimal alignment.

- The program should print out the following:

  - The optimal alignment and its score.

  - Execution times.

## Objective 2: Constructing a Phylogenetic Tree by hand

Using the following matrix of inter-species distances, construct a phylogenetic tree using the UPGMA algorithm.

|       | __a__ | __b__ | __c__ | __d__ | __e__ | __f__ |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| __a__ | 0  | 15 | 24 | 29 | 25 | 37 |
| __b__ | 15 | 0  | 32 | 31 | 23 | 43 |
| __c__ | 24 | 32 | 0  | 30 | 43 | 49 |
| __d__ | 29 | 31 | 30 | 0  | 45 | 57 |
| __e__ | 25 | 23 | 43 | 45 | 0  | 55 |
| __f__ | 37 | 43 | 49 | 57 | 55 | 0  |

## Objective 3: Python Programming to calculate and draw phylogenetic trees

Develop a Python program that uses the WPGMA algorithm to draw a phylogenetic tree from an input matrix of inter-species distances.

It should meet the following conditions:

- Your code should have a function called WPGMA which takes as its input the name of a text file.

- The algorithm should read in an inter-species distance matrix from this text file, and print this matrix to the screen.

- Follow the WPGMA algorithm, and print out to the screen every reduced distance matrix.

- After fully reducing the matrix, the code should draw the phylogentic tree obtained to a file. This tree does not need to contain edge weights.

- The program should print out the execution time to the screen.
