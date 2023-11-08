from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

def create_sliders(sliders_number, labels_list, frame):
    clear(frame)
    sliders_list = []
    indicators = []
    
    layout = frame.layout()
    for i in range(sliders_number):
        
        # create sliders and store them
        vertical_slider = QSlider()
        vertical_slider.setRange(0, 10)
        vertical_slider.setValue(5)
        vertical_slider.setOrientation(2)  # 2 corresponds to vertical orientation
        
        # creating labels
        label = QLabel(labels_list[i])
        label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        # creating value indicators
        indicator = QLabel('0')
        indicator.setAlignment(Qt.AlignLeft | Qt.AlignBottom)
        
        layout.addWidget(label)
        layout.addWidget(vertical_slider)
        layout.addWidget(indicator)
        
        sliders_list.append(vertical_slider)
        indicators.append(indicator)
        
    frame.setLayout(layout)
    return sliders_list, indicators


def clear(frame):
    layout = frame.layout()
    if layout is not None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
                

