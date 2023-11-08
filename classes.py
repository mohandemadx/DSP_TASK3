class Mode:
    def __init__(self, labels, frq_range, num_sliders):
        self.labels = labels
        self.frq_range = frq_range
        self.num_sliders = num_sliders
    
    def __str__(self):
        return f"labels: {self.labels}, frq_range: {self.frq_range}, num_sliders: {self.num_sliders}"


default = Mode(['0 to 1 kHz', '1 to 2 kHz', '2 to 3 kHz', '3 to 4 kHz', '4 to 5 kHz', '5 to 6 kHz',
                '6 to 7 kHz', '7 to 8 kHz', '8 to 9 kHz', '9 to 10 kHz'], #labels
               [1000*i for i in range(10)], #factors
               10) #sliders

ecg = Mode(['A1', 'A2', 'A3'], [1 for _ in range(3)], 3)

animals = Mode(['Duck', 'Dog', 'Horse', 'Cow'], [1 for _ in range(4)], 4)
    
musical = Mode(['Guitar', 'Piano', 'Drums', 'Saxphone'], [1 for _ in range(4)], 4)

