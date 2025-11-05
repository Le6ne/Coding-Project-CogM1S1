import numpy as np

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


def randomize_order(sequences):
    seq_out = rd.shuffle(sequences)
    return seq_out

def randomize_start(sequences):
    seq_out = [((a[0] + rd.randint(0,7)) % NUM_OF_DOT, a[1]) for a in sequences]
    return seq_out

