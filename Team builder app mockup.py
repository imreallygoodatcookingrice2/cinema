from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame
from PyQt6.QtGui import QFont, QColor, QPalette
from PyQt6.QtCore import Qt
import sys

class TeamBuilderMockup(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("StratMon - Team Builder")
        self.setGeometry(200, 200, 800, 600)
        self.setStyleSheet("background-color: #121212; color: white;")

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Title
        title = QLabel("Team Builder")
        title.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        # Pokémon Slots
        slots_layout = QHBoxLayout()
        for i in range(6):
            slot = QFrame()
            slot.setFixedSize(100, 120)
            slot.setStyleSheet("""
                background-color: #1E1E1E;
                border: 2px dashed #555;
                border-radius: 10px;
            """)
            slot_label = QLabel(f"Slot {i+1}")
            slot_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            slot_label.setFont(QFont("Arial", 10))
            slot_layout = QVBoxLayout()
            slot_layout.addWidget(slot_label)
            slot.setLayout(slot_layout)
            slots_layout.addWidget(slot)
        layout.addLayout(slots_layout)

        # Type Coverage Wheel Placeholder
        type_wheel = QFrame()
        type_wheel.setFixedHeight(200)
        type_wheel.setStyleSheet("""
            background-color: #1E1E1E;
            border-radius: 15px;
            border: 2px solid #555;
        """)
        type_label = QLabel("Type Coverage Wheel")
        type_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        type_label.setFont(QFont("Arial", 14))
        wheel_layout = QVBoxLayout()
        wheel_layout.addWidget(type_label)
        type_wheel.setLayout(wheel_layout)
        layout.addWidget(type_wheel)

        # Action Buttons
        btn_layout = QHBoxLayout()
        save_btn = QPushButton("Save Team")
        save_btn.setStyleSheet("""
            background-color: #FFCB05;
            color: black;
            border-radius: 10px;
            padding: 10px;
        """)
        clear_btn = QPushButton("Clear Team")
        clear_btn.setStyleSheet("""
            background-color: #DB1F1F;
            color: white;
            border-radius: 10px;
            padding: 10px;
        """)
        btn_layout.addWidget(save_btn)
        btn_layout.addWidget(clear_btn)
        layout.addLayout(btn_layout)

        self.setLayout(layout)

# Run App
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TeamBuilderMockup()
    window.show()
    sys.exit(app.exec())
