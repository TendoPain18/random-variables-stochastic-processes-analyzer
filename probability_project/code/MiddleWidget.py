from PyQt5.QtWidgets import QWidget, QVBoxLayout
from RandomVariable import RandomVariableWindow
from RandomProcess import RandomProcessWindow
from OutputWidget import OutputWidget


class MiddleWidget(QWidget):
    def __init__(self, window):
        super().__init__()
        self.Main_Window = window
        self.mode = 1

        self.Middle_Widget = QWidget()
        self.Middle_Widget_layout = QVBoxLayout(self.Middle_Widget)

        self.RandomVariable = RandomVariableWindow(window)
        self.RandomProcess = RandomProcessWindow(window)
        self.Output = OutputWidget(window)

    def set_properties(self):
        self.Middle_Widget.setObjectName("Middle_Widget")
        self.Middle_Widget_layout.addWidget(self.RandomVariable.get(), 2)
        self.Middle_Widget_layout.addWidget(self.RandomProcess.get(), 2)
        self.Middle_Widget_layout.addWidget(self.Output.get(), 1)
        self.RandomProcess.get().hide()
        self.RandomVariable.set_properties()
        self.RandomProcess.set_properties()
        self.Output.set_properties()

    def set_stylesheets(self):
        self.Middle_Widget.setStyleSheet("QWidget#Middle_Widget {background-color: #D9D9D9; border-radius: 10px;}")
        self.RandomVariable.set_stylesheets()
        self.RandomProcess.set_stylesheets()
        self.Output.set_stylesheets()

    def update_(self):
        self.Middle_Widget.setFixedWidth(self.Main_Window.dimensions.sw(230))
        self.Middle_Widget_layout.setContentsMargins(10, 10, 10, 10)
        self.Output.update_()
        self.RandomVariable.update_()
        self.RandomProcess.update_()

    def get(self):
        return self.Middle_Widget

    def set_mode(self, num):
        if num == 1:
            self.RandomVariable.get().show()
            self.RandomProcess.get().hide()
        else:
            self.RandomVariable.get().hide()
            self.RandomProcess.get().show()
        self.mode = num
