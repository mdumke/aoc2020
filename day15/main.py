starting_seq = [11,0,1,10,5,19]

memory = {n: [i] for i, n in enumerate(starting_seq)}
memory


last_spoken = starting_seq[-1]

for turn in range(len(starting_seq), 2020):
    history = memory.get(last_spoken)

    if history is None:
        memory[last_spoken] = [turn]
        last_spoken = 0
    elif len(history) == 1:
        last_spoken = 0

        if last_spoken in memory:
            memory[last_spoken].append(turn)
        else:
            memory[last_spoken] = [turn]
    else:
        last_spoken = history[-1] - history[-2]

        if last_spoken in memory:
            memory[last_spoken].append(turn)
        else:
            memory[last_spoken] = [turn]

print('part 1:', last_spoken)
