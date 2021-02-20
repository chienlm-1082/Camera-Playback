import cv2
#abc
import time
cap = cv2.VideoCapture("/home/yoona/Downloads/torres.mp4")

past_frame = []
print(len(past_frame))

# length of playback video is 20s so length of past_image should be 20*30 = 600 elements
#234

cur_fps = cap.get(cv2.CAP_PROP_FPS)
cur_fps = round(cur_fps)
print(cur_fps)

total_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print(total_frame)

print("video length: ", round(total_frame/cur_fps)/60)

frame_count = 0



# cv2.namedWindow('Main Video', cv2.WINDOW_AUTOSIZE)

time_playback = 20
print("total frame will be saved on past_frame is {}".format(time_playback * cur_fps))
while cap.isOpened():
  _, frame = cap.read()
  if not _:
    break
  frame1 = cv2.resize(frame, (640, 480))
  past_frame.append(frame1)
  if len(past_frame) == time_playback * cur_fps:
    del past_frame[0]
  frame_count += 1
  frame = cv2.resize(frame, (960, 600))
  cv2.imshow("Main video", frame)
  k = cv2.waitKey(int(800/cur_fps))
  if k == 32:
    cv2.destroyWindow("Main video")
    cv2.namedWindow('Playback 10s', cv2.WINDOW_AUTOSIZE)
    for i in range(len(past_frame)):
      cv2.imshow("Playback 10s", past_frame[i])
      print("Playback frame {}".format(i))
      cv2.waitKey(int(800/cur_fps))
    cv2.destroyWindow("Playback 10s")
    cv2.namedWindow("Main video")  
    pass
  elif k == ord('q'):
    break
cv2.destroyAllWindows()
cap.release()
