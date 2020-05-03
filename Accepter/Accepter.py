import pyautogui
from python_imagesearch.imagesearch import imagesearch
import time

pyautogui.FAILSAFE = False
TIMELAPSE = 1

acceptButtonImg = './sample.png'
acceptedButtonImg = './sample-accepted.png'
championSelectionImg_flash = './flash-icon.png'
championSelectionImg_emote = './emote-icon.png'
playButtonImg = './play-button.png'


def checkQueuePop():
    while True:
        pos = imagesearch(acceptButtonImg)
        if pos[0] != -1:
            pyautogui.click(pos[0], pos[1])
            # send notification to phone
            print("Game accepted")
            break
        time.sleep(TIMELAPSE)


def checkChampSelect():
    flash = imagesearch(championSelectionImg_flash)
    emote = imagesearch(championSelectionImg_emote)

    if emote[0] != -1 or flash[0] != -1:
        return True
    else:
        return False


def checkDodge():
    accepted = imagesearch(acceptedButtonImg)
    play = imagesearch(playButtonImg)

    if accepted[0] == -1 and play[0] != -1:
        return True
    else:
        return False


def main():
    run = True

    while run:
        checkQueuePop()
        time.sleep(TIMELAPSE)

        while True:
            cancelled = checkDodge()

            if cancelled is True:
                print("A bitch dodged")
                break

            csresult = checkChampSelect()

            if csresult is True:
                print("Don't int idiot")
                time.sleep(TIMELAPSE)
                run = False
                break

            time.sleep(TIMELAPSE)


if __name__ == '__main__':
    main()
