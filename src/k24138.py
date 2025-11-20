import numpy as np
import cv2
from my_module.k24138.lecture05_camera_image_capture import MyVideoCapture
def lecture05_01():
    """課題1の実装

    - カメラを起動してキャプチャ画像を取得する（MyVideoCapture.get_img を使用）
    - 取得したキャプチャ画像を戻り値として返す。

    Returns:
        numpy.ndarray: キャプチャされた画像データ
    """

    # カメラキャプチャ実行
    app = MyVideoCapture()
    app.run()

    # カメラで取得した画像を取得
    capture_img = app.get_img()

    # 画像が取得できなかった場合のエラー処理
    if capture_img is None:
        raise RuntimeError("カメラから画像を取得できませんでした。run() を実行して 'q' キーでキャプチャしてください。")

    # ここで画像を返して終了
    return capture_img
