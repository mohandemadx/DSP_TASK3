# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGraphicsView, QGridLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1227, 858)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_6 = QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.Options_frame = QFrame(self.centralwidget)
        self.Options_frame.setObjectName(u"Options_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Options_frame.sizePolicy().hasHeightForWidth())
        self.Options_frame.setSizePolicy(sizePolicy)
        self.Options_frame.setMaximumSize(QSize(281, 523))
        self.Options_frame.setFrameShape(QFrame.StyledPanel)
        self.Options_frame.setFrameShadow(QFrame.Sunken)
        self.gridLayout_3 = QGridLayout(self.Options_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(10)
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 6, 0, 1, 1)

        self.HideFrame = QFrame(self.Options_frame)
        self.HideFrame.setObjectName(u"HideFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.HideFrame.sizePolicy().hasHeightForWidth())
        self.HideFrame.setSizePolicy(sizePolicy1)
        self.HideFrame.setFrameShape(QFrame.StyledPanel)
        self.HideFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.HideFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.showCheckBox = QCheckBox(self.HideFrame)
        self.showCheckBox.setObjectName(u"showCheckBox")

        self.verticalLayout_2.addWidget(self.showCheckBox)


        self.gridLayout_3.addWidget(self.HideFrame, 9, 0, 1, 1)

        self.label = QLabel(self.Options_frame)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.AudioPlayerFrame = QFrame(self.Options_frame)
        self.AudioPlayerFrame.setObjectName(u"AudioPlayerFrame")
        sizePolicy1.setHeightForWidth(self.AudioPlayerFrame.sizePolicy().hasHeightForWidth())
        self.AudioPlayerFrame.setSizePolicy(sizePolicy1)
        self.AudioPlayerFrame.setMinimumSize(QSize(0, 124))
        self.AudioPlayerFrame.setFrameShape(QFrame.StyledPanel)
        self.AudioPlayerFrame.setFrameShadow(QFrame.Plain)
        self.gridLayout_2 = QGridLayout(self.AudioPlayerFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(self.AudioPlayerFrame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 2)

        self.playButton1 = QPushButton(self.AudioPlayerFrame)
        self.playButton1.setObjectName(u"playButton1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.playButton1.sizePolicy().hasHeightForWidth())
        self.playButton1.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.playButton1, 1, 0, 1, 1)

        self.label_4 = QLabel(self.AudioPlayerFrame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 2)

        self.audioSlider1 = QSlider(self.AudioPlayerFrame)
        self.audioSlider1.setObjectName(u"audioSlider1")
        self.audioSlider1.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.audioSlider1, 1, 1, 1, 1)

        self.audioSlider2 = QSlider(self.AudioPlayerFrame)
        self.audioSlider2.setObjectName(u"audioSlider2")
        self.audioSlider2.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.audioSlider2, 3, 1, 1, 1)

        self.muteButton2 = QPushButton(self.AudioPlayerFrame)
        self.muteButton2.setObjectName(u"muteButton2")
        sizePolicy3.setHeightForWidth(self.muteButton2.sizePolicy().hasHeightForWidth())
        self.muteButton2.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.muteButton2, 3, 2, 1, 1)

        self.playButton2 = QPushButton(self.AudioPlayerFrame)
        self.playButton2.setObjectName(u"playButton2")
        sizePolicy3.setHeightForWidth(self.playButton2.sizePolicy().hasHeightForWidth())
        self.playButton2.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.playButton2, 3, 0, 1, 1)

        self.muteButton1 = QPushButton(self.AudioPlayerFrame)
        self.muteButton1.setObjectName(u"muteButton1")
        sizePolicy3.setHeightForWidth(self.muteButton1.sizePolicy().hasHeightForWidth())
        self.muteButton1.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.muteButton1, 1, 2, 1, 1)


        self.gridLayout_3.addWidget(self.AudioPlayerFrame, 7, 0, 1, 1)

        self.mode_comboBox = QComboBox(self.Options_frame)
        self.mode_comboBox.addItem("")
        self.mode_comboBox.addItem("")
        self.mode_comboBox.addItem("")
        self.mode_comboBox.addItem("")
        self.mode_comboBox.setObjectName(u"mode_comboBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(30)
        sizePolicy4.setHeightForWidth(self.mode_comboBox.sizePolicy().hasHeightForWidth())
        self.mode_comboBox.setSizePolicy(sizePolicy4)
        self.mode_comboBox.setMinimumSize(QSize(0, 30))

        self.gridLayout_3.addWidget(self.mode_comboBox, 1, 0, 1, 1)

        self.ImportFrame = QFrame(self.Options_frame)
        self.ImportFrame.setObjectName(u"ImportFrame")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.ImportFrame.sizePolicy().hasHeightForWidth())
        self.ImportFrame.setSizePolicy(sizePolicy5)
        self.ImportFrame.setMinimumSize(QSize(0, 107))
        self.ImportFrame.setFrameShape(QFrame.StyledPanel)
        self.ImportFrame.setFrameShadow(QFrame.Plain)
        self.gridLayout = QGridLayout(self.ImportFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.ImportFrame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.importButton = QPushButton(self.ImportFrame)
        self.importButton.setObjectName(u"importButton")

        self.gridLayout.addWidget(self.importButton, 1, 0, 1, 3)

        self.label_5 = QLabel(self.ImportFrame)
        self.label_5.setObjectName(u"label_5")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(5)
        sizePolicy6.setVerticalStretch(5)
        sizePolicy6.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy6)
        self.label_5.setMinimumSize(QSize(5, 5))
        self.label_5.setMaximumSize(QSize(31, 31))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setWordWrap(False)

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.musicfileName = QLabel(self.ImportFrame)
        self.musicfileName.setObjectName(u"musicfileName")

        self.gridLayout.addWidget(self.musicfileName, 2, 1, 1, 1, Qt.AlignLeft)


        self.gridLayout_3.addWidget(self.ImportFrame, 3, 0, 3, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 8, 0, 1, 1)


        self.gridLayout_6.addWidget(self.Options_frame, 0, 0, 1, 1)

        self.Graph_frame = QFrame(self.centralwidget)
        self.Graph_frame.setObjectName(u"Graph_frame")
        self.Graph_frame.setMinimumSize(QSize(881, 521))
        self.Graph_frame.setFrameShape(QFrame.StyledPanel)
        self.Graph_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.Graph_frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(6)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.OutputGraph = QGraphicsView(self.Graph_frame)
        self.OutputGraph.setObjectName(u"OutputGraph")

        self.gridLayout_4.addWidget(self.OutputGraph, 0, 1, 1, 1)

        self.SpectoGraph1 = QGraphicsView(self.Graph_frame)
        self.SpectoGraph1.setObjectName(u"SpectoGraph1")

        self.gridLayout_4.addWidget(self.SpectoGraph1, 1, 0, 1, 1)

        self.InputGraph = QGraphicsView(self.Graph_frame)
        self.InputGraph.setObjectName(u"InputGraph")

        self.gridLayout_4.addWidget(self.InputGraph, 0, 0, 1, 1)

        self.SpectoGraph2 = QGraphicsView(self.Graph_frame)
        self.SpectoGraph2.setObjectName(u"SpectoGraph2")

        self.gridLayout_4.addWidget(self.SpectoGraph2, 1, 1, 1, 1)


        self.gridLayout_6.addWidget(self.Graph_frame, 0, 1, 1, 1)

        self.SliderFrame = QFrame(self.centralwidget)
        self.SliderFrame.setObjectName(u"SliderFrame")
        self.SliderFrame.setFrameShape(QFrame.StyledPanel)
        self.SliderFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.SliderFrame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalSlider_3 = QSlider(self.SliderFrame)
        self.verticalSlider_3.setObjectName(u"verticalSlider_3")
        self.verticalSlider_3.setOrientation(Qt.Vertical)

        self.gridLayout_5.addWidget(self.verticalSlider_3, 0, 1, 1, 1, Qt.AlignHCenter)

        self.label_14 = QLabel(self.SliderFrame)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_5.addWidget(self.label_14, 2, 2, 1, 1, Qt.AlignHCenter)

        self.verticalSlider_4 = QSlider(self.SliderFrame)
        self.verticalSlider_4.setObjectName(u"verticalSlider_4")
        self.verticalSlider_4.setOrientation(Qt.Vertical)

        self.gridLayout_5.addWidget(self.verticalSlider_4, 0, 2, 1, 1, Qt.AlignHCenter)

        self.label_control1 = QLabel(self.SliderFrame)
        self.label_control1.setObjectName(u"label_control1")

        self.gridLayout_5.addWidget(self.label_control1, 2, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSlider_2 = QSlider(self.SliderFrame)
        self.verticalSlider_2.setObjectName(u"verticalSlider_2")
        self.verticalSlider_2.setOrientation(Qt.Vertical)

        self.gridLayout_5.addWidget(self.verticalSlider_2, 0, 0, 1, 1, Qt.AlignHCenter)

        self.label_11 = QLabel(self.SliderFrame)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_5.addWidget(self.label_11, 1, 3, 1, 1, Qt.AlignHCenter)

        self.label_9 = QLabel(self.SliderFrame)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_5.addWidget(self.label_9, 1, 1, 1, 1, Qt.AlignHCenter)

        self.label_10 = QLabel(self.SliderFrame)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_5.addWidget(self.label_10, 1, 2, 1, 1, Qt.AlignHCenter)

        self.verticalSlider = QSlider(self.SliderFrame)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_5.addWidget(self.verticalSlider, 0, 3, 1, 1, Qt.AlignHCenter)

        self.label_13 = QLabel(self.SliderFrame)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_5.addWidget(self.label_13, 2, 1, 1, 1, Qt.AlignHCenter)

        self.label_15 = QLabel(self.SliderFrame)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_5.addWidget(self.label_15, 2, 3, 1, 1, Qt.AlignHCenter)

        self.label1 = QLabel(self.SliderFrame)
        self.label1.setObjectName(u"label1")

        self.gridLayout_5.addWidget(self.label1, 1, 0, 1, 1, Qt.AlignHCenter)


        self.gridLayout_6.addWidget(self.SliderFrame, 1, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1227, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.verticalSlider_3.valueChanged.connect(self.label_9.setNum)
        self.verticalSlider_4.valueChanged.connect(self.label_10.setNum)
        self.verticalSlider.valueChanged.connect(self.label_11.setNum)
        self.verticalSlider_2.valueChanged.connect(self.label1.setNum)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.showCheckBox.setText(QCoreApplication.translate("MainWindow", u"Show Spectograms", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Select Mode:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Input (Before Edits):", None))
        self.playButton1.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Output (After Edits):", None))
        self.muteButton2.setText("")
        self.playButton2.setText("")
        self.muteButton1.setText("")
        self.mode_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Default Mode", None))
        self.mode_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"ECG Mode", None))
        self.mode_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Animal Mode", None))
        self.mode_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Music Mode", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Select Audio:", None))
        self.importButton.setText(QCoreApplication.translate("MainWindow", u"Browse Files", None))
        self.label_5.setText("")
        self.musicfileName.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_control1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label1.setText(QCoreApplication.translate("MainWindow", u"0", None))
    # retranslateUi

