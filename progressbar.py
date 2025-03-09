from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal
from PyQt5.QtGui import QPainter, QPen, QColor
import sys
import math

class TaskThread(QThread):
    taskFinished = pyqtSignal()

    def run(self):
        for i in range(1, 100001):  # Printing 0.1 million numbers
            print(i)
        self.taskFinished.emit()

class CircularProgressBar(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Circular Progress Bar")
        self.setFixedSize(100, 100)
        self.rotation_angle = 0  # Track rotation
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateProgress)
        
        self.button = QPushButton("Start Task", self)
        self.button.setGeometry(10, 70, 80, 20)
        self.button.clicked.connect(self.startTask)
        
        self.taskThread = TaskThread()
        self.taskThread.taskFinished.connect(self.taskCompleted)

    def startTask(self):
        self.rotation_angle = 0  # Reset rotation
        self.timer.start(20)  # Slightly slower updates
        self.taskThread.start()

    def taskCompleted(self):
        self.timer.stop()
        self.repaint()

    def updateProgress(self):
        self.rotation_angle += 15  # Moderate speed
        self.repaint()

    def paintEvent(self, event):
        if not self.taskThread.isRunning():
            return  # Don't draw if task isn't running
        
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        size = 80
        center = self.rect().center()
        
        painter.setBrush(QColor("#111111"))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(center.x() - size // 2, center.y() - size // 2, size, size)
        
        # Draw futuristic rotating dashed edge
        pen = QPen(QColor("#00d4ff"), 3)
        painter.setPen(pen)
        radius = size // 2
        num_dashes = 10
        active_dashes = 4
        angle_step = 360 / num_dashes
        start_angle = self.rotation_angle % 360
        
        for i in range(active_dashes):
            angle = start_angle + i * angle_step
            radian = math.radians(angle)
            x1 = center.x() + (radius - 2) * math.cos(radian)
            y1 = center.y() + (radius - 2) * math.sin(radian)
            x2 = center.x() + (radius - 6) * math.cos(radian)
            y2 = center.y() + (radius - 6) * math.sin(radian)
            painter.drawLine(int(x1), int(y1), int(x2), int(y2))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CircularProgressBar()
    window.show()
    sys.exit(app.exec_())
