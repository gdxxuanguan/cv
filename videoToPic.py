import cv2

import os


# 按帧数间隔保存图片，默认为1帧
def video2img(video_path, out_path, interval=1):
    cap = cv2.VideoCapture(video_path)

    i, j = 0, 0
    while cap.isOpened():
        i += 1
        ret, frame = cap.read()

        if i % interval == 0:
            j += 1
            if ret:

                # 按编号保存图片
                filename = out_path + r'\img' + str(j) + '.jpg'
                cv2.imwrite(filename, frame)
            else:
                break

    cap.release()


dir = 'videos'
videos = os.listdir(dir)
for video in videos:
    # print(os.path.abspath(video))
    path_name = video.split('.')[0]
    num = path_name[len(path_name) - 1]
    out_path = 'pic/' + num
    if os.path.exists(out_path):
        pass
    else:
        os.mkdir(out_path)
    video2img(dir + '/' + video, out_path)
