import cv2
import numpy as np
import pyautogui
import time
import keyboard

def exclude_specific_color(image, color_to_exclude):
    lower = np.array(color_to_exclude, dtype="uint8")
    upper = np.array(color_to_exclude, dtype="uint8")
    mask = cv2.inRange(image, lower, upper)
    image = cv2.bitwise_and(image, image, mask=~mask)
    return image

def find_least_frequent_color(image):
    pixels = image.reshape((-1, 3))
    unique, counts = np.unique(pixels, axis=0, return_counts=True)
    # 가장 적게 나타나는 색상을 반환, 제외할 색상이 있으면 그 색상은 제외
    least_frequent_color = unique[np.argmin(counts)]
    return least_frequent_color

def click_least_frequent_color_area(full_image, region, color_to_exclude):
    x, y, w, h = region
    cropped_image = full_image[y:y+h, x:x+w]
    # 특정 색상 제외
    cropped_image = exclude_specific_color(cropped_image, color_to_exclude)
    least_frequent_color = find_least_frequent_color(cropped_image)
    ys, xs = np.where(np.all(cropped_image == least_frequent_color, axis=-1))
    if len(ys) > 0 and len(xs) > 0:
        avg_x, avg_y = int(np.mean(xs)), int(np.mean(ys))
        global_x, global_y = avg_x + x, avg_y + y
        pyautogui.click(global_x, global_y)
    
    # if len(ys) > 0 and len(xs) > 0: # 키쿠 mac 맵핑용 코드
    #     avg_x, avg_y = int(np.mean(xs)), int(np.mean(ys))
    #     global_x, global_y = avg_x + x, avg_y + y
    #     height, width, channels = full_image.shape
    #     map_x, map_y = int(global_x * 1199 / width), int(global_y * 834 / height)
    #     pyautogui.click(map_x, map_y)

color_to_exclude = [221, 221, 221]  # DDDDDD
region = (630, 265, 640, 640)  # 특정 영역 설정

while True:
    if keyboard.is_pressed('esc'):  # 'q' 키가 눌리면 루프를 종료
        print("Program terminated by user.")
        break
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)
    screenshot_np = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)
    click_least_frequent_color_area(screenshot_np, region, color_to_exclude)
    # print('Run ColorDetector')
    time.sleep(0.001)
