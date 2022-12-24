import mouse
import pyperclip
import time
import keyboard
import pyautogui
import os


def write_console(string):
    pyperclip.copy(string)
    mouse.move(1400, 600)
    mouse.click()
    keyboard.press("ctrl")
    keyboard.press("v")
    keyboard.release("v")
    keyboard.release("ctrl")
    keyboard.press("enter")
    keyboard.press("enter")


def yellow_light():
    global text, start_time
    start_time = time.perf_counter()
    write_console(query)

    cords = pyautogui.locateCenterOnScreen("end3.png", confidence=0.95)
    if cords is None:
        cords = pyautogui.locateCenterOnScreen("end.png", confidence=0.95)
        if cords is None:
            cords = pyautogui.locateCenterOnScreen("end2.png", confidence=0.95)
    mouse.move(cords[0] - 100, cords[1])
    mouse.click()

    while True:
        if os.path.exists("C:\\Users\\Artem\\Downloads\\klava.txt"):
            with open("C:\\Users\\Artem\\Downloads\\klava.txt", "r", encoding="utf-8") as f:
                text = f.read()
            break
        else:
            time.sleep(0.1)
    text.replace('\n', ' ')
    for key, value in words.items():
        text = text.replace(key, value)


def slow():
    global k_speed
    for i in range(len(text)):
        if keyboard.is_pressed('shift'):
            k_speed += 0.1
        if keyboard.is_pressed('CAPSLOCK'):
            k_speed -= 0.1
        keyboard.write(text[i])
        print(text[i], end='')
        time.sleep(60 / max(speed * k_speed, 1))
    return True


def fast():
    keyboard.write(text)
    return True


words = {
    'o': 'о',
    'c': 'с',
    'e': 'е',
    'y': 'у',
    'a': 'а',
    'x': 'х',
    'O': 'О',
    'C': 'С',
    'E': 'Е',
    'Y': 'У',
    'A': 'А',
    'X': 'Х'
}
query = '''let stroka = document.getElementById("typefocus").innerText + document.getElementById("afterfocus").innerText;
let blob = new Blob([stroka], {type: "text/plain"});
let link = document.createElement("a");
link.setAttribute("href", URL.createObjectURL(blob));
link.setAttribute("download", "klava.txt");
link.click();'''
clear = 'clear();'
text = ''
start_time = 0
speed = 500
k_speed = 1


def main():
    if os.path.exists("C:\\Users\\Artem\\Downloads\\klava.txt"):
        os.remove("C:\\Users\\Artem\\Downloads\\klava.txt")

    red, yellow = True, True
    while True:
        if red and pyautogui.locateOnScreen('red.png', confidence=0.99) is not None:
            print('Красный')
            red = False
        elif yellow and pyautogui.locateOnScreen('ready.png', confidence=0.99) is not None:
            print('желтый')
            yellow_light()
            yellow, red = False, False
        elif (not yellow and time.perf_counter() - start_time > 3) or pyautogui.locateOnScreen('go.png', confidence=0.99) is not None:
            print('Зеленый')
            if yellow:
                yellow_light()
            if slow():
                break
        else:
            print('Ищу..')
        time.sleep(0.5)

    write_console(clear)
    os.remove("C:\\Users\\Artem\\Downloads\\klava.txt")


if __name__ == "__main__":
    main()
