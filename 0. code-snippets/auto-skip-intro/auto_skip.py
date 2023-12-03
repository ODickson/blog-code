import pyautogui
import time
import os

# get all images to match
image_dir = 'images_to_match'
images = os.listdir(image_dir)

# get screen center
screen_width, screen_height = pyautogui.size()

def click_image(image_center):
    # click on image center
    pyautogui.moveTo(image_center)
    pyautogui.click()
    # move mouse back to screen center out of the way of media bar
    pyautogui.moveTo(screen_width / 2, screen_height / 2)

def check_and_click():
    """
    Checks for image presence on screen
    If image is present it then clicks on the center
    Checks again in 250ms time
    """
    for image in images:
        found_img = pyautogui.locateCenterOnScreen(image_dir+'/'+image, confidence=0.8)
        if found_img:
            click_image(found_img)
            print(f'Successfully clicked on {image}')
            break
    time.sleep(0.25)


if __name__ == "__main__":
    while True:
        check_and_click()