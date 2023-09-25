import cv2
import time

# 打开摄像头
cap = cv2.VideoCapture(0)

# 检查摄像头是否成功打开
if not cap.isOpened():
    print("无法打开摄像头")
    exit()

# 设定时间间隔（秒）
interval = 5

# 循环拍摄照片
while True:
    # 读取一帧画面
    ret, frame = cap.read()

    # 检查是否成功读取画面
    if not ret:
        print("无法读取摄像头画面")
        break

    # 生成照片文件名
    # timestamp = int(time.time())
    filename = f"photo_.jpg"

    # 保存照片
    cv2.imwrite(filename, frame)
    print(f"照片 {filename} 已保存")

    # 等待指定时间间隔
    time.sleep(interval)

# 释放摄像头
cap.release()