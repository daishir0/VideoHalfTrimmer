import cv2
import sys

if len(sys.argv) != 2:
    print("Usage: python trim_half.py <path_to_video>")
    sys.exit(1)

input_path = sys.argv[1]
output_path = "output.mp4"

# 動画の読み込み
cap = cv2.VideoCapture(input_path)

# 動画の基本情報を取得
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

# 出力動画の設定
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height // 2))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 上半分を取得
    cropped_frame = frame[height // 2:, :]

    # 書き込む
    out.write(cropped_frame)

# リソースの解放
cap.release()
out.release()
