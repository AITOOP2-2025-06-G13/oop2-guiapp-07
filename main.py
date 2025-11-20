import sys
import cv2
import numpy as np
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import Qt
from src.k24138 import lecture05_01
from src.combine_image import combine_images


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
        self.mid_button = QPushButton("合成！！！！")
        self.right_button = QPushButton("保存")

        # ボタンが押されたときの処理
        self.left_button.clicked.connect(self.on_left_click)
        self.mid_button.clicked.connect(self.on_mid_click)
        self.right_button.clicked.connect(self.on_right_click)

        # 保存ボタンは最初は非表示
        self.right_button.setVisible(False)
        self.mid_button.setVisible(False)

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

    def display_image(self, image_array):
        """OpenCVの画像(numpy配列)をQtのウィジェットに表示する"""
        # BGRからRGBに変換
        rgb_image = cv2.cvtColor(image_array, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w

        # QImageに変換
        qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)

        # QPixmapに変換してラベルに表示
        pixmap = QPixmap.fromImage(qt_image)
        # ラベルのサイズに合わせてスケーリング
        scaled_pixmap = pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_label.setPixmap(scaled_pixmap)

    def on_left_click(self):
        """撮影ボタンがクリックされたときの処理"""
        # カメラで画像を撮影
        self.result_image = lecture05_01()
        # 撮影が完了したら画像を表示して撮影ボタンを非表示
        if self.result_image is not None:
            self.display_image(self.result_image)
            self.left_button.setVisible(False)  # 撮影ボタンを非表示
            self.mid_button.setVisible(True)  # 合成ボタンを表示
            print("画像を撮影しました。合成ボタンを押してください。")

    def on_mid_click(self):
        """midボタンがクリックされたときの処理（合成）"""
        if self.result_image is not None:
            # 撮影した画像とgoogle.pngを合成
            self.result_image = combine_images(self.result_image)
            if self.result_image is not None:
                self.display_image(self.result_image)
                self.right_button.setVisible(True)  # 合成完了後に保存ボタンを表示
                self.mid_button.setVisible(False)  # 合成ボタンを非表示
                print("合成した画像を表示しました。保存ボタンを押して保存できます。")
        else:
            print("合成する画像がありません。先に撮影ボタンを押してください。")

    def on_right_click(self):
        """Rightボタンがクリックされたときの処理（保存）"""
        if self.result_image is not None:
            out_filename = 'output_images/lecture05_01_k24138.png'
            cv2.imwrite(out_filename, self.result_image)
        else:
            print("保存する画像がありません。先にLeftボタンを押してください。")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWidget()
    w.show()
    sys.exit(app.exec())
