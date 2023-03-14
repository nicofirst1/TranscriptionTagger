from PySide6 import QtWidgets, QtCore, QtGui

from src.common import GeneralWindow, Memory, create_input


class Settings(GeneralWindow):
    settingsChanged = QtCore.Signal()

    def __init__(self, mem: Memory):
        super().__init__(mem, "Settings")

    def create_widgets(self):
        form_layout = QtWidgets.QFormLayout()
        form_layout.setAlignment(QtCore.Qt.AlignCenter)

        for group, members in self.mem.setting_groups.items():
            group_label = QtWidgets.QLabel(group)
            group_label.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))
            form_layout.addRow(group_label)
            for name in members:
                input_, lay = create_input(self, name, self.mem)
                form_layout.addRow(lay)

        layout = QtWidgets.QVBoxLayout()
        layout.setAlignment(QtCore.Qt.AlignCenter)
        layout.addLayout(form_layout)

        self.ok = QtWidgets.QPushButton("Save")
        self.ok.clicked.connect(self.accept_settings)
        layout.addWidget(self.ok)

        self.setLayout(layout)

    def accept_settings(self):
        self.close()
