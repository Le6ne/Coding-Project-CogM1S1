# Coding Project: *The Language of Geometry* — Experiment

This project implements an experiment inspired by  
**“The Language of Geometry: Fast comprehension of geometrical primitives and rules in human adults and preschoolers”**  
by *Marie Amalric, Liping Wang, Pierre Pica, Santiago Figueira, Mariano Sigman, Stanislas Dehaene*  
([DOI: 10.1371/journal.pcbi.1005273](https://doi.org/10.1371/journal.pcbi.1005273))

The experiment is designed to study **sequential memory** and **spatial representation** through geometric sequences.  
It is developed using **Expyriment**, a Python framework for cognitive psychology experiments.

---

## Repository Structure


<img width="650" height="337" alt="image" src="https://github.com/user-attachments/assets/0ed88edf-37c3-49a7-9e83-45b1316b7f2c" />




---

## Experimental Objective

The goal is to study participants’ ability to **reproduce and extend spatial sequences** on an **octagon** (8 points arranged in a circle).

Each sequence is:
- Randomized in order and starting position  
- Potentially rotated or mirrored  
- Built around geometric rules (rotation, symmetry, direction)

Participants must **“repeat +1”** with each trial — that is, reproduce the sequence and then predict the next element.

---

## Trial Procedure

1. The **8 dots of the octagon** are always visible on screen.  
2. A simple **clockwise (CW)** or **counter-clockwise (CCW)** “repeat +1” instruction is displayed.  
3. For each participant, the **order of sequences is randomized**.  
4. The **first two elements** of the sequence are flashed (e.g., starting at position 3).  
5. The participant must **click to guess** the next location.  
6. If the answer is **incorrect**, the sequence (1–3) is replayed including the correct answer,  
   and the participant must then guess the following location (position 4).  
7. Errors are tracked **from the 3rd to the 16th element** of each sequence.  
8. The full experiment consists of **17 sequences** in total.

---

## Technical Notes

- **Language:** Python ≥ 3.8  
- **Framework:** [Expyriment]
- **Data format:** `.xpd` (Expyriment native format)  
- **Quick testing mode:** enable with python


