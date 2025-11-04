import numpy as np

NUM_OF_DOT = 8

"""
Experiment type
"""
sequences_ez = np.array([[i for i in range(NUM_OF_DOT)], 
                         [NUM_OF_DOT-i-1 for i in range(NUM_OF_DOT)]])
print(sequences_ez)

sequences_cw = np.asarray([[0,2,4,6,1,3,5,7], #2squares cw
                           [0,6,4,2,1,7,5,3], #2squares ccw
                           [0,2,1,3,2,4,3,5,4,6,5,7,6,0,7,1], #alternate cw
                           [0,6,7,5,6,4,5,3,4,2,3,1,2,0,1,6], #alternate ccw
                           [0,4,1,5,2,6,3,7], #4diagonales cw
                           [0,4,7,3,6,2,5,1], #4diagonales ccw
                           [1,2,3,4,0,7,6,5], #2arcs cw
                           [0,7,6,5,1,2,3,4], #2arcs ccw
                           [0,1,7,2,6,3,5,4], #
                           ])

