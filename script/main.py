from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK

exp = design.Experiment(name="test", background_colour=C_WHITE, foreground_colour=C_BLACK)
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

def present_for(*stims, t=1000):
    dt = timed_draw(*stims)
    exp.clock.wait(t - dt)

def present_instructions(text):
    instructions = stimuli.TextScreen(text=text, text_justification=0, heading="Instructions")
    instructions.present()
    exp.keyboard.wait()


""" Experiment """


control.initialize(exp)
control.start(subject_id=1)