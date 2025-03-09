from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit, QFrame, QGraphicsDropShadowEffect)
from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtCore import Qt
import sys

class ModernUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Modern PyQt UI")
        self.setGeometry(100, 100, 800, 500)
        self.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #fdfbfb, stop:1 #ebedee);")
        
        main_layout = QHBoxLayout(self)
        
        # Sidebar
        sidebar = QVBoxLayout()
        sidebar.setContentsMargins(10, 10, 10, 10)
        sidebar.setSpacing(15)
        
        sidebar_widget = QFrame()
        sidebar_widget.setStyleSheet("background-color: rgba(240, 240, 240, 0.8); border-radius: 15px;")
        sidebar_widget.setFixedWidth(200)
        sidebar_layout = QVBoxLayout(sidebar_widget)
        
        buttons = ["Dashboard", "Settings", "Profile", "Logout"]
        for btn_text in buttons:
            btn = QPushButton(btn_text)
            btn.setStyleSheet("background-color: #ffffff; color: black; border: none; padding: 12px; border-radius: 8px; font-size: 12pt;")
            btn.setFont(QFont("Arial", 10))
            btn.setCursor(Qt.PointingHandCursor)
            shadow = QGraphicsDropShadowEffect()
            shadow.setBlurRadius(10)
            shadow.setOffset(2, 2)
            btn.setGraphicsEffect(shadow)
            sidebar_layout.addWidget(btn)
        
        sidebar_layout.addStretch()
        sidebar.addWidget(sidebar_widget)
        
        # Main Content
        content_layout = QVBoxLayout()
        
        title = QLabel("Welcome to Modern PyQt UI")
        title.setFont(QFont("Arial", 18, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        
        input_field = QLineEdit()
        input_field.setPlaceholderText("Enter text here...")
        input_field.setStyleSheet("background-color: #ffffff; border: 1px solid #cccccc; color: black; padding: 10px; border-radius: 10px;")
        
        text_area = QTextEdit()
        text_area.setPlaceholderText("Write something...")
        text_area.setStyleSheet("background-color: #ffffff; border: 1px solid #cccccc; color: black; padding: 10px; border-radius: 10px;")
        
        action_button = QPushButton("Submit")
        action_button.setStyleSheet("background-color: #007ACC; color: white; padding: 12px; border-radius: 10px; font-size: 12pt;")
        action_button.setFont(QFont("Arial", 10, QFont.Bold))
        action_button.setCursor(Qt.PointingHandCursor)
        shadow_btn = QGraphicsDropShadowEffect()
        shadow_btn.setBlurRadius(10)
        shadow_btn.setOffset(2, 2)
        action_button.setGraphicsEffect(shadow_btn)
        
        content_layout.addWidget(title)
        content_layout.addWidget(input_field)
        content_layout.addWidget(text_area)
        content_layout.addWidget(action_button)
        
        main_layout.addLayout(sidebar)
        main_layout.addLayout(content_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModernUI()
    window.show()
    sys.exit(app.exec_())
