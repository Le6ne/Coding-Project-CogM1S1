import numpy as np
import math as m
from expyriment.misc.constants import C_WHITE, C_BLACK

"""
General constants
"""

NUM_OF_DOT = 8

EXP_RADIUS = 150

DOT_RADIUS = 10
DOT_COLOR = "grey"

TRIGGERED_DOT_RADIUS = 15
TRIGGERED_DOT_COLOR = "yellow"

"""
INSTRUCTIONS
"""
EXPLANATION_INSTRUCTION = " A simple sequence will be presented. This is just a trial sequence to help you visualize. This is not part of the trial, please just observe."
FIRST_INSTRUCTION = "A sequence will be presented. The first two elements will be displayed, please click on the dot that you think will follow."
INSTRUCTION_CORRECT = " You correctly identified the following location. Please click on the next location you believe will follow."
INSTRUCTION_INCORRECT = " You incorrectly guessed the following location. The sequence will replay with the correct answer. please click on the dot that you think will follow."
END_INSTRUCTION_SEQUENCE = "This sequence is finished."
INBETWEEN_INSTRUCTION = "This is sequence","out of 16."
FINISH_INSTRUCTION = "All the sequences have been done. You are done with the experiment. Thank you for participating"
"""
Sequences
"""
C_sequences_ez = [(np.asarray([i for i in range(NUM_OF_DOT)]), "repeat cw"),
                (np.asarray([NUM_OF_DOT-i-1 for i in range(NUM_OF_DOT)]), "repeat ccw")]

C_sequences = [(np.asarray([0,2,4,6,1,3,5,7]), "2squares cw"), 
                (np.asarray([0,6,4,2,1,7,5,3]), "2squares ccw"), 
                (np.asarray([0,2,1,3,2,4,3,5,4,6,5,7,6,0,7,1]), "alternate cw"), 
                (np.asarray([0,6,7,5,6,4,5,3,4,2,3,1,2,0,1,6]), "alternate ccw"), 
                (np.asarray([0,4,1,5,2,6,3,7]), "4diagonales cw"), 
                (np.asarray([0,4,7,3,6,2,5,1]), "4diagonales ccw"), 
                (np.asarray([1,2,3,4,0,7,6,5]), "2arcs cw"), 
                (np.asarray([0,7,6,5,1,2,3,4]), "2arcs ccw"), 
                (np.asarray([0,1,7,2,6,3,5,4]), "4segments cw"), 
                (np.asarray([1,0,2,7,3,6,4,5]), "4segment ccw"), #TODO: 2 autres symetries
                (np.asarray([0,5,4,1,6,3,2,7]), "2rectangles"), 
                (np.asarray([0,4,5,1,2,6,7,3]), "2crosses") 
                ]


"""
Generated constants (from previous constants)
"""

dot_positions = [(EXP_RADIUS * m.cos((t*2*m.pi/NUM_OF_DOT)+(m.pi/NUM_OF_DOT)), EXP_RADIUS * m.sin((t*2*m.pi/NUM_OF_DOT)+(m.pi/NUM_OF_DOT))) for t in range(NUM_OF_DOT)]
