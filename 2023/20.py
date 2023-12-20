import re

BROADCASTER = "broadcaster"
FLIP_FLOP = "flip_flop"
CONJONCTION = "conjonction"
OUTPUT = "output"
STATE_ON = "on"
STATE_OFF = "off"
PULSE_LOW = "low"
PULSE_HIGH = "high"

parts = {}
total_low = 0
total_high = 0

class Signal:

    def __init__(self, origin, destination, pulse):
        self.origin = origin
        self.destination = destination
        self.pulse = pulse

    def __repr__(self):
        return f"({self.origin}, {self.pulse}, {self.destination})"


class Part:

    def __init__(self, content):
        origin, destinations = content.split(" -> ")
        self.state = None
        self.pulse = None
        self.origins = {}

        if origin == BROADCASTER:
            self.type = BROADCASTER
            self.name = BROADCASTER
        elif origin[0] == "%":
            self.type = FLIP_FLOP
            self.state = STATE_OFF
            self.name = origin[1:]
        elif origin[0] == "&":
            self.type = CONJONCTION
            self.name = origin[1:]
        else:
            self.type = OUTPUT
            self.name = OUTPUT

        self.destinations = destinations.split(", ")

    def __str__(self):
        return f"Type :{self.type}, name: {self.name}, state: {self.state}, destinations: {self.destinations}"

    def __repr__(self):
        return f"({self.type}, {self.name}, {self.state}, {self.destinations}, {self.origins})"

    def compute_origins(self, parts):
        for name, part in parts.items():
            if self.name in part.destinations:
                self.origins[part.name] = PULSE_LOW

    def send_signal(self, signal):
        signals = []
        sending = None
        if self.type == BROADCASTER:
            sending = signal.pulse
        elif self.type == FLIP_FLOP:
            if signal.pulse == PULSE_LOW:
                if self.state == STATE_OFF:
                    sending = PULSE_HIGH
                    self.state = STATE_ON
                else:
                    sending = PULSE_LOW
                    self.state = STATE_OFF
        elif self.type == CONJONCTION:
            self.origins[signal.origin] = signal.pulse
            if all(x == PULSE_HIGH for x in list(self.origins.values())):
                sending = PULSE_LOW
            else:
                sending = PULSE_HIGH

        for destination in self.destinations:
            if sending:
                print(f" -- {self.name} -{sending}-> {destination}")
                signals.append(Signal(part.name, destination, sending))

        return signals


if __name__ == '__main__':
    file = open('20.txt', 'r')
    result = 0
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    changed_parts = []
    for line in lines:
        part = Part(line)
        parts[part.name] = part

    parts[OUTPUT] = Part("output -> ")
    for name, part in parts.items():
        part.compute_origins(parts)
    print(f"Total part list : {parts}")

    for i in range(1000):
        print(f"Smash button {i}")
        signals = [Signal("button", BROADCASTER, PULSE_LOW)]
        total_low += 1
        while signals:
            new_signals = []
            for signal in signals:
                if signal.destination in parts:
                    part = parts[signal.destination]
                    new_signals += part.send_signal(signal)
            signals = new_signals
            # print(f" - current signals to compute {signals}")
            for signal in signals:
                if signal.pulse == PULSE_LOW:
                    total_low += 1
                else:
                    total_high += 1
        print(f" -  {total_low * total_high} ({total_low},{total_high})")

    print(f"Result { total_low * total_high} ({total_low},{total_high})")
