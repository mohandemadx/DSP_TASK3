from collections import namedtuple

r = namedtuple('Range', ['min', 'max'])


class WindowType:
    def __init__(self, labels, num_sliders):
        self.labels = labels
        self.num_sliders = num_sliders
    
    def __str__(self):
        return f"labels: {self.labels}, num_sliders: {self.num_sliders}"

hamming = WindowType(['α'], 1)

hanning = WindowType(['α'], 1)

gaussian = WindowType(['Mean', 'Std'], 2)

rectangle = WindowType(['constant'], 1)

class Mode:
    def __init__(self, labels, frq_range, num_sliders):
        self.labels = labels
        self.frq_range = frq_range
        self.num_sliders = num_sliders
    
    def __str__(self):
        return f"labels: {self.labels}, frq_range: {self.frq_range}, num_sliders: {self.num_sliders}"


default = Mode([f'{i} to {i+1} KHz' for i in range(10)], [r(i*1000+1, (i+1)*1000) for i in range(10)], 10)

ecg = Mode(['A1', 'A2', 'A3'], [1 for _ in range(3)], 3)

animals = Mode(['Duck', 'Dog', 'Monkey', 'Owl'], [1 for _ in range(4)], 4)
    
musical = Mode(['Drums', 'Trumpet', 'Flute', 'Piano'], [1 for _ in range(4)], 4)
