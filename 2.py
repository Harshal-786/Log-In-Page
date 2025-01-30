from PyQt6 import QtCore, QtGui, QtWidgets

class Parameters:
    """Class to store user input values."""
    def __init__(self):
        self.spinbox_value = 0
        self.first_text = 0.0  # Default to float
        self.second_text = 0.0  # Default to float
        self.third_text = 0.0  # Default to float
        self.selected_cam = ""  # Default to empty string for camera selection

    def update(self, spinbox_value, first_text, second_text, third_text, selected_cam):
        """Update parameters with new values."""
        self.spinbox_value = spinbox_value
        self.first_text = first_text
        self.second_text = second_text
        self.third_text = third_text
        self.selected_cam = selected_cam

    def __repr__(self):
        return (f"Parameters(spinbox_value={self.spinbox_value}, "
                f"first_text={self.first_text}, "
                f"second_text={self.second_text}, "
                f"third_text={self.third_text}, "
                f"selected_cam='{self.selected_cam}')")

    def get_all_info(self):
        """Return all gathered information in a formatted string."""
        return f"Spinbox Value: {self.spinbox_value}, First Text: {self.first_text}, Second Text: {self.second_text}, Third Text: {self.third_text}, Selected Camera: {self.selected_cam}"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 412)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # UI Layout (SpinBox + LineEdits)
        self.spinbox_number = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinbox_number.setGeometry(QtCore.QRect(60, 90, 100, 30))
        
        self.txt_first = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txt_first.setGeometry(QtCore.QRect(60, 130, 200, 30))

        self.txt_second = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txt_second.setGeometry(QtCore.QRect(60, 170, 200, 30))

        self.txt_third = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txt_third.setGeometry(QtCore.QRect(60, 210, 200, 30))

        # ComboBox for camera selection
        self.select_cam = QtWidgets.QComboBox(parent=self.centralwidget)
        self.select_cam.setGeometry(QtCore.QRect(60, 250, 200, 30))
        self.select_cam.addItem("Camera 1")
        self.select_cam.addItem("Camera 2")
        self.select_cam.addItem("Camera 3")

        # Button to Save Values
        self.btn_save = QtWidgets.QPushButton("Save", parent=self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(60, 290, 100, 30))
        self.btn_save.clicked.connect(self.save_values)  # Connect button to function

        MainWindow.setCentralWidget(self.centralwidget)

        # Create an instance of Parameters to store values
        self.params = Parameters()

    def save_values(self):
        """Retrieve values from UI and store them in Parameters class."""
        spinbox_value = self.spinbox_number.value()  # Get integer from spinbox
        
        # Convert text input to float, handle invalid input gracefully
        try:
            first_text = float(self.txt_first.text())  # Convert to float
        except ValueError:
            first_text = 0.0  # Default to 0.0 if conversion fails
        
        try:
            second_text = float(self.txt_second.text())  # Convert to float
        except ValueError:
            second_text = 0.0  # Default to 0.0 if conversion fails
        
        try:
            third_text = float(self.txt_third.text())  # Convert to float
        except ValueError:
            third_text = 0.0  # Default to 0.0 if conversion fails
        
        # Get selected camera from ComboBox
        selected_cam = self.select_cam.currentText()

        # Update the Parameters instance with the gathered values
        self.params.update(spinbox_value, first_text, second_text, third_text, selected_cam)

        # Print to console (for testing)
        print(self.params.get_all_info())  # Call the function in Parameters class to get all info

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
