import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(2)


# test


position1 = pt.locateOnScreen("smiley_paperclip.png", confidence=.6)
x = position1[0]
y = position1[1]


def get_message():
    global x, y

    position = pt.locateOnScreen("../whatsapp/smiley_paperclip.png", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y, duration=.05)
    pt.moveTo(x + 70, y - 40, duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12, 15)
    pt.click()
    whatsapp_msg = pyperclip.paste()
    pt.click()
    print("Message received !" + whatsapp_msg)

    return whatsapp_msg


def post_response(message):
    global x, y

    position = pt.locateOnScreen("../whatsapp/smiley_paperclip.png", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x + 200, y + 20, duration=.5)
    pt.click()
    pt.typewrite(message, interval=.01)

    pt.typewrite("\n", interval=.01)


def process_response(message):
    random_no = random.randrange(3)

    if "?" in str(message).lower():
        return "Dont ask me such questions "
    else:
        if random_no == 0:
            return "Nice "
        elif random_no == 1:
            return "Hello"
        else:
            return "Bye"


def check_for_new_messages():
    pt.moveTo(x + 50, y - 35, duration=.5)

    while True:

        try:
            position = pt.locateOnScreen("../whatsapp/green_circle.png", confidence=.7)

            if position is not None:
                pt.moveTo(position)
                pt.moveTo(-100, 0)
                pt.click()
                sleep(.5)
        except (Exception):
            print("No new notifications ! ")

        if pt.pixelMatchesColor(int(x + 50), int(y - 35), (255, 255, 255), tolerance=10):
            print("is_white")
            post_response(process_response(get_message()))
        else:
            print("No new messages !")
        sleep(5)


check_for_new_messages()

# post_response(process_response(get_message()))
