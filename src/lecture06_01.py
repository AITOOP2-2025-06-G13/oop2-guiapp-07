import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PySide6 import QtGui

class GameButton(QPushButton):
    """
    フォント変更とクリック時の挙動を伴うボタン
    ゲームの状態をself.statusとして保持する
    """

    def __init__(self, status):
        super().__init__()
        self.status = status
        self.setFont(QtGui.QFont('Arial', 40))
        self.clicked.connect(self.__click)

    def set_buttons(self, buttons : list['GameButton']) -> None:
        self.buttons = buttons

    def __click(self):
        # マス目にマークがあるなら更新しない
        if self.text() != "":
            return
        # マス目に入れるマークはself.status["next"]から読み取る
        self.setText(self.status["marks"][self.status["next"]])
        # マス目にマークを入れたら勝敗判定(勝敗が決まってもゲームは続く)
        self.__check_win()
        # 次のターンのためにマークを更新
        # ○ならself.status["next"]が0なので1-0 -> 1となる
        # ×ならself.status["next"]が1なので1-1 -> 0となる
        self.status["next"] = 1 - self.status["next"]

    def __check_win(self):
        # 勝敗判定は以下の8パターンで行う
        patterns = [
            [0,1,2], # 1行目の3マス
            [3,4,5], # 2行目の3マス
            [6,7,8], # 3行目の3マス
            [0,3,6], # 1列目の3マス
            [1,4,7], # 2列目の3マス
            [2,5,8], # 3列目の3マス
            [0,4,8], # スラッシュ列の3マス
            [2,4,6]  # バックスラッシュ列の3マス
        ]
        # 全部のパターンを確かめるには判定を関数にしておく
        [self.__check_a_line(pattern) for pattern in patterns]

    def __check_a_line(self, pattern : list[int]):
        btns : list[GameButton] = [self.buttons[i] for i in pattern]
        result = [btn.text() for btn in btns]
        # 3マスのマークが全て○なら○の勝利
        if result[0] == result[1] == result[2] == self.status["marks"][0]:
            print(f"{self.status['marks'][0]}の勝ち")
            # 対象の3マスの色を赤色(#RRGGBB)に変更
            [btn.setStyleSheet("color : #ff0000;") for btn in btns]
        # 3マスのマークが全て×なら×の勝利
        if result[0] == result[1] == result[2] == self.status["marks"][1]:
            print(f"{self.status['marks'][1]}の勝ち")
            # 対象の3マスの色を赤色(#RRGGBB)に変更
            [btn.setStyleSheet("color : #ff0000;") for btn in btns]

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        # ゲームに関する初期化
        self.__game_init()

        # GUIに関する初期化
        # ボタンを9個作成
        self.buttons = [GameButton(self.game_status) for _ in range(9)]
        # ボタンが押されたときに他のボタンの状態を知りたいのでボタンリストを各ボタンに通知
        [btn.set_buttons(self.buttons) for btn in self.buttons]
        # 3x3マスのグリッド状にボタンを並べる
        layout = QGridLayout()
        for i in range(3):
            for j in range(3):
                layout.addWidget(self.buttons[i*3+j], i, j)
        self.setLayout(layout)

    def __game_init(self):
        """
        ゲームに関する初期化
        """
        # game_status["marks"]でマークを定義
        # game_status["next"]で次のターンを記憶
        self.game_status={}
        self.game_status["marks"]=["○","×"]
        self.game_status["next"]=0 # ○を初期値としてセット

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWidget()
    mw.show()
    app.exec()
