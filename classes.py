from collections import namedtuple

r = namedtuple('Range', ['min', 'max'])



class Mode:
    def __init__(self, labels, frq_range, num_sliders):
        self.labels = labels
        self.frq_range = frq_range
        self.num_sliders = num_sliders
    
    def __str__(self):
        return f"labels: {self.labels}, frq_range: {self.frq_range}, num_sliders: {self.num_sliders}"


default = Mode([f'{i} to {i+1} kHz' for i in range(10)], [r(i*1000+1, (i+1)*1000) for i in range(10)], 10) 

ecg = Mode(['A1', 'A2', 'A3'], [1 for _ in range(3)], 3)

animals = Mode(['Duck', 'Dog', 'Horse', 'Cow'], [1 for _ in range(4)], 4)
    
musical = Mode(['Guitar', 'Piano', 'Drums', 'Saxphone'], [1 for _ in range(4)], 4)
