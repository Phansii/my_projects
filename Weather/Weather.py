import tkinter as tk
import pyautogui as pag
import keyboard
import os
from PIL import ImageTk, Image, ImageGrab
import pytesseract
import re
import time
from pynput.mouse import Button, Controller as MouseController


def autoshaman_toggle():
    if autoshaman_toggle_var.get() == 1:
        as_on()
        tooltip()
        combos()
    else:
        print("OFF")
        print(szukanie_upper)

def combos():
    global combo_maker
    combo_maker = False
    mouse = MouseController()
    if keyboard.is_pressed('c') and szukanie_upper == "2526952" and in_tfm == True and combo_maker == False and autoshaman_toggle_var.get() == 1:
        combo_maker = True
        mouse.position = (x1+250, y1+170)
        keyboard.press('1')
        keyboard.release('1')
        keyboard.press('z')
        keyboard.release('z')
        mouse.press(Button.left)
        time.sleep(1.2)
        mouse.release(Button.left)
        mouse.position = (x1+175,y1+205)
        keyboard.press('1')
        keyboard.release('1')
        keyboard.press('x')
        keyboard.release('x')
        keyboard.press('x')
        keyboard.release('x')
        keyboard.press('x')
        keyboard.release('x')
        mouse.press(Button.left)
        time.sleep(1.2)
        mouse.release(Button.left)
        combo_maker = False
    root.after(1, combos)


def as_on():
    global szukanie_upper
    if autoshaman_toggle_var.get() == 1:
        screenshot_upper = ImageGrab.grab(bbox=(x1, y1, x1 + 220, y1 + 25))
        screenshot_upper = screenshot_upper.convert("RGBA")
        text_upper = pytesseract.image_to_string(screenshot_upper)
        screen_text_upper = text_upper.strip()
        match = re.search(r'@(\d+)', screen_text_upper)
        if match:
            szukanie_upper = match.group(1)
        root.after(500, as_on)


def toggle_visibility(event):
    global shift_click
    if event.name == 'shift':
        shift_click = root.state() == 'normal'


def in_tfm_fun():
    global in_tfm, x1, y1
    result = pag.locateCenterOnScreen(base_path)
    if result is not None:
        x1, y1 = result
        x1, y1 = x1 - 568, y1 - 432
        in_tfm = True
    else:
        in_tfm = False
    root.after(250, in_tfm_fun)


def tooltip():
    xmospos, ymospos = pag.position()
    if in_tfm == False:
        windowz.withdraw()
    elif x1+350 <= xmospos <= x1+475 and y1+290 <= ymospos <= y1+330 and szukanie_upper == "2526952" and autoshaman_toggle_var.get() == 1:
        windowz.geometry("20x20+{}+{}".format(x1+350,y1+290))
        labelz.config(text="C")
        windowz.deiconify()
    elif x1+40 <= xmospos <= x1+160 and y1+360 <= ymospos <= y1+395 and szukanie_upper == "2526952" and autoshaman_toggle_var.get() == 1:
        windowz.geometry("20x20+{}+{}".format(x1+40,y1+360))
        labelz.config(text="V")
        windowz.deiconify()
    elif x1+600 <= xmospos <= x1+760 and y1+360 <= ymospos <= y1+395 and szukanie_upper == "2526952" and autoshaman_toggle_var.get() == 1:
        windowz.geometry("20x20+{}+{}".format(x1+600,y1+360))
        labelz.config(text="B")
        windowz.deiconify()
###
    else:
        windowz.withdraw()
    root.after(20, tooltip)


def gui_visible():
    if in_tfm and shift_click:
        root.withdraw()
    elif in_tfm and not shift_click:
        root.deiconify()
        root.geometry(f"140x200+{x1 + 800}+{y1 + 400}")
    elif not in_tfm:
        root.withdraw()
    root.after(250, gui_visible)


def exit_program():
    root.destroy()


root = tk.Tk()

folder_path = os.path.dirname(os.path.abspath(__file__))
base_path = os.path.join(folder_path, 'base.png')
weather_gui_path = os.path.join(folder_path, 'weather_gui.png')
close_button_path = os.path.join(folder_path, 'close.png')

baseimage = Image.open(weather_gui_path)
basephoto = ImageTk.PhotoImage(baseimage)

base_image = tk.Label(root, image=basephoto)
base_image.pack()

close_image = Image.open(close_button_path)
close_photo = ImageTk.PhotoImage(close_image)

close_button = tk.Button(root, image=close_photo, command=exit_program, bd=0, highlightthickness=0)
close_button.place(x=115, y=175)

root.geometry("140x200")
root.overrideredirect(True)

keyboard.on_press(toggle_visibility)

autoshaman_toggle_var = tk.IntVar()
autoshaman_switch = tk.Checkbutton(root, text="AutoShaman", variable=autoshaman_toggle_var,
                                   command=autoshaman_toggle, bg="black", fg="white", highlightthickness=0)
autoshaman_switch.place(x=23, y=71)

in_tfm = False
shift_click = False

in_tfm_fun()
gui_visible()

# gui z
windowz = tk.Toplevel(root)
windowz.overrideredirect(True)
windowz.geometry("20x20+100+200")
windowz.configure(bg="black")

labelz = tk.Label(windowz, text="Z", font=("Arial", 12), fg="white", bg="black")
labelz.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
windowz.withdraw()

root.mainloop()
