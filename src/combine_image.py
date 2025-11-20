import numpy as np
import cv2


def combine_images(capture_img: np.ndarray) -> np.ndarray:
    google_img = cv2.imread("images/google.png")
    if google_img is None:
        raise FileNotFoundError(
            "images/google.png が見つかりません。パスを確認してください。"
        )

    g_h, g_w, g_c = google_img.shape
    c_h, c_w, c_c = capture_img.shape
    print(f"google: {google_img.shape}, capture: {capture_img.shape}")

    # capture_img をタイル状に並べた同サイズ画像を作る
    tiled = np.zeros_like(google_img)
    for y in range(0, g_h, c_h):
        for x in range(0, g_w, c_w):
            # コピー可能な領域サイズを計算（端で切れるのを許容する）
            h = min(c_h, g_h - y)
            w = min(c_w, g_w - x)
            tiled[y : y + h, x : x + w] = capture_img[0:h, 0:w]

    # 白色(255,255,255)の部分を tiled の画素で置換（BGR順）
    # 白色の定義は完全一致とする
    white_mask = np.all(google_img == [255, 255, 255], axis=2)
    # マスクが True の場所を tiled で置換
    result = google_img.copy()
    result[white_mask] = tiled[white_mask]

    return result


if __name__ == "__main__":
    capture_img = cv2.imread("images/camera_capture.png")
    result = combine_images(capture_img)

    out_filename = "output_images/combined_image.png"
    ok = cv2.imwrite(out_filename, result)
    if not ok:
        raise IOError(f"画像の保存に失敗しました: {out_filename}")
    print(f"保存しました: {out_filename}")
