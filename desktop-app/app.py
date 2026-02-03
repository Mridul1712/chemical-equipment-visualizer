import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QPushButton, QLabel, QFileDialog
)
import matplotlib.pyplot as plt


class DesktopApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chemical Equipment Visualizer")
        self.setGeometry(200, 200, 500, 400)

        layout = QVBoxLayout()

        self.label = QLabel("Upload CSV file")
        layout.addWidget(self.label)

        self.button = QPushButton("Choose CSV File")
        self.button.clicked.connect(self.upload_file)
        layout.addWidget(self.button)

        self.result = QLabel("")
        layout.addWidget(self.result)

        self.setLayout(layout)

    def upload_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select CSV", "", "CSV Files (*.csv)"
        )

        if not file_path:
            return

        files = {"file": open(file_path, "rb")}
        response = requests.post(
            "http://127.0.0.1:8000/api/upload/", files=files
        )

        if response.status_code != 200:
            self.result.setText("Upload failed")
            return

        data = response.json()
        self.result.setText(
            f"""
Total Equipment: {data['total_equipment']}
Avg Flowrate: {data['avg_flowrate']}
Avg Pressure: {data['avg_pressure']}
Avg Temperature: {data['avg_temperature']}
"""
        )

        self.show_chart(data["type_distribution"])

    def show_chart(self, dist):
        plt.figure()
        plt.bar(dist.keys(), dist.values())
        plt.title("Equipment Type Distribution")
        plt.xlabel("Type")
        plt.ylabel("Count")
        plt.show()


app = QApplication(sys.argv)
window = DesktopApp()
window.show()
sys.exit(app.exec_())
