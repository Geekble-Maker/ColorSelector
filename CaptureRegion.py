import cv2
import numpy as np
import pyautogui

def capture_screen_with_rectangle(region):
    # 전체 스크린샷을 캡처합니다.
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)
    screenshot_np = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)
    
    # 지정된 영역에 사각형을 그립니다.
    x, y, w, h = region
    cv2.rectangle(screenshot_np, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    return screenshot_np

# 원하는 영역을 지정합니다: (x, y, width, height)
region = (630, 265, 640, 640)

# 캡처하고 사각형을 그린 스크린샷을 얻습니다.
screenshot_with_rectangle = capture_screen_with_rectangle(region)

# 결과를 화면에 표시합니다.
cv2.imshow("Screenshot with Rectangle", screenshot_with_rectangle)
cv2.waitKey(0)
cv2.destroyAllWindows()