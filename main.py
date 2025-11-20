import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout
from src.k24138 import lecture05_01


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Three Buttons")

        # 3つのボタンを作成して横に並べる
        self.left_button = QPushButton("Left")
        self.mid_button = QPushButton("Middle")
        self.right_button = QPushButton("Right")

        # ボタンが押されたら lecture05_01 を実行
        self.left_button.clicked.connect(lecture05_01)

        layout = QHBoxLayout()
        layout.addWidget(self.left_button)
        layout.addWidget(self.mid_button)
        layout.addWidget(self.right_button)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWidget()
    w.show()
    sys.exit(app.exec())
