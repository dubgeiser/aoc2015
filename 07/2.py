#!/usr/bin/env python3


OPERATIONS = {
        'OR': lambda x, y: x | y,
        'AND': lambda x, y: x & y,
        'LSHIFT': lambda x, y: x << y,
        'RSHIFT': lambda x, y: x >> y,
        }


def load_signals(wiring_instructions: list, signals: dict) -> None:
    """ Find all the known signals in the wiring instructions and store them.
    Also remove them from the instructions, so we don't have to deal with them
    later on.
    """
    to_delete = []
    for sig_or_gate, wire in wiring_instructions:
        if wire == 'b':
            signals['b'] = 956
            to_delete.append((sig_or_gate, wire))
        elif sig_or_gate.isnumeric():
            to_delete.append((sig_or_gate, wire))
            signals[wire] = int(sig_or_gate)
    while len(to_delete) > 0:
        wiring_instructions.remove(to_delete.pop())


def process_gates(gates: list[tuple[str, str]], signals: dict[str, int]) -> None:
    """ Process gates.
    Process as many as possible and delete those that have been processed.
    Since signals are integers; use the int version of the bitwise operations.
    """
    to_delete = []
    for gate, wire in gates:
        gparts = gate.split()
        if len(gparts) == 1: # Just 2 wires connected: a signal that's not int
            w = gparts[0]
            if w in signals:
                signals[wire] = signals[w]
                to_delete.append((gate, wire))
            continue
        if len(gparts) == 2: # NOT
            w = gparts[1]
            if w in signals:
                signals[wire] = ~ signals[w]
                to_delete.append((gate, wire))
            continue
        w1, op, w2 = gparts
        if w1 in signals and w2 in signals:
            signals[wire] = OPERATIONS[op](signals[w1], signals[w2])
            to_delete.append((gate, wire))
        elif w1 in signals and w2.isnumeric():
            signals[wire] = OPERATIONS[op](signals[w1], int(w2))
            to_delete.append((gate, wire))
        elif w1.isnumeric() and w2 in signals:
            signals[wire] = OPERATIONS[op](int(w1), signals[w2])
            to_delete.append((gate, wire))
    while len(to_delete) > 0:
        gates.remove(to_delete.pop())


with open("input") as data:
    wiring_instructions = [tuple(l.strip().split(" -> ")) for l in data]
signals = {}
load_signals(wiring_instructions, signals)
while len(wiring_instructions) > 0:
    process_gates(wiring_instructions, signals)
print("\n", signals["a"])
