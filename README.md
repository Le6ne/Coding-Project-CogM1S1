# Coding project : Experiment - The language of geometry - 

This project implements an experiment inspired by “The Language of Geometry : Fast comprehension of geometrical primitives and rules in human adults and preschoolers” by By Marie Amalric, Liping Wang, Pierre Pica, Santiago Figueira, Mariano Sigman, Stanislas Dehaene (https://doi.org/10.1371/journal.pcbi.1005273) designed to study sequential memory and spatial representation through geometric sequences.

The experiment is developed with Expyriment, a Python framework for cognitive psychology experiments.


├── Script 
  └── main.py         # Main script for the experiment       
  └── constants.py
  └── functions.py     Functions for generating and randomizing sequences
	└── mouse_function.py     
  └── constants.py            # Global parameters (colors, radius, duration, etc.)
└── Datas                  # Folder where Expyriment saves the results (.xpd)
└── README.md              # This file :)


# Experimental objective

The goal is to study the participant's ability to reproduce and extend spatial sequences on an octagon (8 points arranged in a circle). 
Each sequence is random but follows certain geometric patterns (rotation, symmetry, etc.), and the participant must repeat the sequence +1 with each trial.

# Trial procedure

The 8 dots of the octagon are always visible
First a simple CW or CCW “repeat +1”
For each participant the sequences are in a random order
First two elements of sequence are flashed (location 3)
Participant must guess the next location,
If incorrect, sequence is flashed again (1-3)  with correct answer and participant must guess the following location (location 4)
Errors tracked from 3rd and 16th element of sequence
17 sequences in total

