def create_random_seq(length=8, num_dots=8):
    seq = []
    current = rd.randint(0, num_dots-1)
    seq.append(current)
    for _ in range(length-1):
        next_dot = rd.randint(0, num_dots-1)
        while next_dot == current:
            next_dot = rd.randint(0, num_dots-1)
        seq.append(next_dot)
        current = next_dot
    return seq


