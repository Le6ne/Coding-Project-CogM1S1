from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK
from constants import *
from mouse_function import *
import random as rd

exp = design.Experiment(name="test", background_colour=C_BLACK, foreground_colour=C_WHITE)
exp.add_data_variable_names(['seq_type','start_point','number_of_error'])

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


def present_for(*stims, t=1000):
    dt = timed_draw(*stims)
    exp.clock.wait(t - dt)

def present_instructions(text):
    instructions = stimuli.TextScreen(text=text, text_justification=0, heading="Instructions")
    instructions.present()
    exp.keyboard.wait()

def randomize_order(sequences):
    rd.shuffle(sequences)
    return sequences

def randomize_start(sequences):
    seq_out = [((a[0] + rd.randint(0,7)) % NUM_OF_DOT, a[1]) for a in sequences]
    return seq_out

def create_random_seq(length=16, num_dots=8):
    seq = []
    current = rd.randint(0, num_dots-1)
    seq.append(current)
    for _ in range(length-1):
        next_dot = rd.randint(0, num_dots-1)
        while next_dot == current:
            next_dot = rd.randint(0, num_dots-1)
        seq.append(next_dot)
        current = next_dot
    return np.asarray(seq)

def run_trial(sequence_name, sequence):
    present_instructions(FIRST_INSTRUCTION)
    
    present_for(*dots)
    present_for(*dots + [triggered_dots[sequence[0]]])
    present_for(*dots + [triggered_dots[sequence[1]]])
    timed_draw(*dots)
    good_dot = wait_for_dot_click(sequence[2], dot_positions)
    i = 2
    while good_dot and i <= MAX_SEQ_SIZE :
        timed_draw(*dots + [clicked_dots[sequence[i%NUM_OF_DOT]]])
        i+=1
        good_dot = wait_for_dot_click(sequence[i%NUM_OF_DOT], dot_positions)
    i+=1

    while not(good_dot) and i <= MAX_SEQ_SIZE/2 :
        present_for(*dots)
        for j in range(i):
            present_for(*dots + [triggered_dots[sequence[j%NUM_OF_DOT]]])
        timed_draw(*dots)
        good_dot = wait_for_dot_click(sequence[i%NUM_OF_DOT], dot_positions)
        while good_dot and i <= MAX_SEQ_SIZE :
            timed_draw(*dots + [clicked_dots[sequence[i%NUM_OF_DOT]]])
            i+=1
            good_dot = wait_for_dot_click(sequence[i%NUM_OF_DOT], dot_positions)
        i += 1
    # exp.data.add([sequence_name,sequence[0], i - 3])
    present_instructions(END_INSTRUCTION_SEQUENCE)



def init_exp():
    sequences_ez = randomize_start(C_sequences_ez)
    sequences = randomize_start(C_sequences)
    # sequences.append(create_random_seq()) #DEMO !
    # sequences.append(create_random_seq())
    sequences = randomize_order(sequences)
    return sequences_ez, sequences

""" Global settings """
control.initialize(exp)
control.start(subject_id=1)

control.set_develop_mode()

""" Stimuli """

dots = [stimuli.Circle(radius = DOT_RADIUS, colour = DOT_COLOR, position = p) for p in dot_positions]
load(dots)

triggered_dots = [stimuli.Circle(radius = TRIGGERED_DOT_RADIUS, colour = TRIGGERED_DOT_COLOR, position = p) for p in dot_positions]
load(triggered_dots)

clicked_dots = [stimuli.Circle(radius = TRIGGERED_DOT_RADIUS, colour = CLICKED_DOT_COLOR, position = p) for p in dot_positions]
load(clicked_dots)

""" Experiment """

sequences_ez, sequences = init_exp()

present_instructions(INBETWEEN_INSTRUCTION[0] + str(1) + "/" + str(len(sequences) + 2))
run_trial(sequences_ez[0][1], sequences_ez[0][0])
for i in range(2):
    present_instructions(INBETWEEN_INSTRUCTION[0] + str(i+2) + "/" + str(len(sequences) + 2))
    run_trial(sequences[i][1], sequences[i][0])
exp.keyboard.wait()
present_instructions(FINISH_INSTRUCTION)
control.end()
