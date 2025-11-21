from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QComboBox, QTableWidget, QTableWidgetItem, \
    QSizePolicy


class RandomVariableWindow(QWidget):
    def __init__(self, window):
        super().__init__()
        self.Main_Window = window

        self.index = -1

        self.User_Widget = QWidget()
        self.User_Widget_layout = QVBoxLayout(self.User_Widget)

        self.User_Input = QWidget()
        self.User_Input_layout = QVBoxLayout(self.User_Input)

        self.Choose_Vector_Widget = QWidget()
        self.Choose_Vector = QHBoxLayout(self.Choose_Vector_Widget)
        self.Choose_Vector_Label = QLabel("Choose Random Variable: ")
        self.combo_box = QComboBox()

        self.Data_Preview = QWidget()
        self.Data_Preview_layout = QVBoxLayout(self.Data_Preview)
        self.table_widget = QTableWidget()

    def set_properties(self):
        self.User_Widget.setObjectName("User_Widget")
        self.User_Input.setObjectName("User_Input")
        self.Data_Preview.setObjectName("Data_Preview")
        self.table_widget.setObjectName("table_widget")
        self.Choose_Vector_Label.setObjectName("Choose_Vector_Label")
        self.Choose_Vector.setAlignment(Qt.AlignCenter)
        self.combo_box.currentIndexChanged.connect(self.on_combo_box_changed)
        self.Choose_Vector.addWidget(self.Choose_Vector_Label)
        self.Choose_Vector.addWidget(self.combo_box)
        self.Data_Preview_layout.addWidget(self.table_widget)
        self.User_Input_layout.addWidget(self.Choose_Vector_Widget)
        self.User_Widget_layout.addWidget(self.User_Input)
        self.User_Widget_layout.addWidget(self.Data_Preview)

    def set_stylesheets(self):
        self.User_Widget.setStyleSheet("QWidget#User_Widget {background-color: #D9D9D9; border-radius: 10px;}")
        self.User_Input.setStyleSheet("QWidget#User_Input {background-color: orange; border-radius: 10px;}")
        self.Data_Preview.setStyleSheet("QWidget#Data_Preview {border-radius: 10px; background-color: white;}")
        self.table_widget.setStyleSheet("QTableWidget#table_widget {background-color: white; border-radius: 10px;}")
        self.combo_box.setStyleSheet("QComboBox {border-radius: 15px;")


    def update_(self):
        self.User_Widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.User_Widget_layout.setContentsMargins(10, 10, 10, 10)
        self.User_Input.setFixedHeight(self.Main_Window.dimensions.sh(67))
        self.combo_box.setFixedWidth(self.Main_Window.dimensions.sw(65))
        self.combo_box.setFixedHeight(self.Main_Window.dimensions.sw(12))
        self.Choose_Vector_Label.setStyleSheet(f"QLabel#Choose_Vector_Label {{font-weight: bold; font-size: {self.Main_Window.dimensions.sh(13)}px; border-radius: 2px;}}")



    def get(self):
        return self.User_Widget

    def update_combo(self):
        self.combo_box.clear()
        for i in self.Main_Window.variables:
            self.combo_box.addItem(i)

    def on_combo_box_changed(self, index):
        self.index = index
        data = self.Main_Window.data[index]
        rows = len(data)
        columns = len(data[0])
        self.table_widget.setRowCount(rows)
        self.table_widget.setColumnCount(columns)
        for i, row in enumerate(data):
            for j, item in enumerate(row):
                self.table_widget.setItem(i, j, QTableWidgetItem(str(item)))
