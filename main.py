import sys
import cv2
import numpy as np
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel
from PySide6.QtCore import Qt
from src.k24138 import lecture05_01


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("画像処理アプリ")
        self.result_image = None  # 処理結果の画像を保持

        # 画像表示用のラベル
        self.image_label = QLabel("画像がここに表示されます")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setMinimumSize(640, 480)
        self.image_label.setStyleSheet("border: 2px solid gray;")

        # 3つのボタンを作成して横に並べる
        self.left_button = QPushButton("撮影")
        self.mid_button = QPushButton("画像合成")
        self.right_button = QPushButton("保存")

        # 保存ボタンは最初は非表示
        self.right_button.setVisible(False)

        # ボタンのレイアウト
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.left_button)
        button_layout.addWidget(self.mid_button)
        button_layout.addWidget(self.right_button)

        # 全体のレイアウト（縦に配置）
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.image_label)
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWidget()
    w.show()
    sys.exit(app.exec())
