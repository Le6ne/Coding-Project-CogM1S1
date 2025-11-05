from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK
from constants import *
import random as rd

exp = design.Experiment(name="test", background_colour=C_BLACK, foreground_colour=C_WHITE)
exp.add_data_variable_names([])

control.set_develop_mode()

""" Helper functions """
def load(stims):
    for stim in stims:
        stim.preload()

def timed_draw(*stims):
    t0 = exp.clock.time
    exp.screen.clear()
    for stim in stims:
        stim.present(clear=False, update=False)
    exp.screen.update()
    t1 = exp.clock.time
    return t1 - t0

def timed_add(*stims): #same as timed draw but without clear
    t0 = exp.clock.time
    for stim in stims:
        stim.present(clear=False, update=False)
    exp.screen.update()
    t1 = exp.clock.time
    return t1 - t0

def present_for(*stims, t=1000):
    dt = timed_draw(*stims)
    exp.clock.wait(t - dt)

def present_instructions(text):
    instructions = stimuli.TextScreen(text=text, text_justification=0, heading="Instructions")
    instructions.present()
    exp.keyboard.wait()

def randomize_order(sequences):
    seq_out = rd.shuffle(sequences)
    return seq_out

def randomize_start(sequences):
    seq_out = [((a[0] + rd.randint(0,7)) % NUM_OF_DOT, a[1]) for a in sequences]
    return seq_out

def create_random_seq():
    return 0 #TODO

def run_trial(trial_id, sequence):
    timed_draw(*dots)


def init_exp():
    sequences_ez = randomize_start(C_sequences_ez)
    sequences = randomize_start(C_sequences)
    sequences = randomize_order(sequences)

""" Global settings """
control.initialize(exp)
control.start(subject_id=1)

control.set_develop_mode()
control.initialize(exp)

""" Stimuli """
dots = [stimuli.Circle(radius = DOT_RADIUS, colour = DOT_COLOR, position = p) for p in dot_positions]
load(dots)

triggered_dots = [stimuli.Circle(radius = TRIGGERED_DOT_RADIUS, colour = TRIGGERED_DOT_COLOR, position = p) for p in dot_positions]
load(triggered_dots)

""" Experiment """

timed_draw(*dots)
exp.keyboard.wait()

control.end()
