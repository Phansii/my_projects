import tkinter as tk
import pyautogui as pag
import keyboard
import os
from PIL import ImageTk, Image, ImageGrab
import pytesseract
import re
import time
from pynput.mouse import Button, Controller as MouseController
import threading


def clickrs():
    def clickrs_thread():
        mysz = MouseController()
        while True:
            if keyboard.is_pressed('r') and in_tfm == True and clickrs_onof == True:
                mysz.press(Button.left)
                time.sleep(0.015)
                mysz.release(Button.left)

    clickrs_thread = threading.Thread(target=clickrs_thread)
    clickrs_thread.daemon = True  # Set the thread as a daemon so it exits when the main program ends
    clickrs_thread.start()


def clickrs_toggle():
    if clickrs_toggle_var.get() == 1:
        clickrs()
        global clickrs_onof
        clickrs_onof = True
    else:
        root.after_cancel(clickrs)
        clickrs_onof = False


def autoshaman_toggle():
    if autoshaman_toggle_var.get() == 1:
        as_on()
        tooltip()
        combos()
    else:
        root.after_cancel(as_on)
        root.after_cancel(tooltip)
        root.after_cancel(combos)


def combos():
    global combo_maker
    combo_maker = False
    mouse = MouseController()
    if keyboard.is_pressed('c') and szukanie_upper == "2526952" and in_tfm == True and combo_maker == False and autoshaman_toggle_var.get() == 1:
        combo_maker = True
        mouse.position = (x1 + 252, y1 + 170)
        keyboard.press('2')
        keyboard.release('2')
        keyboard.press('z')
        keyboard.release('z')
        keyboard.press('z')
        keyboard.release('z')
        keyboard.press('z')
        keyboard.release('z')
        keyboard.press('z')
        keyboard.release('z')
        keyboard.press('z')
        keyboard.release('z')
        keyboard.press('z')
        keyboard.release('z')
        mouse.press(Button.left)
        time.sleep(1.15)
        mouse.release(Button.left)
        mouse.position = (x1 + 208, y1 + 84)
        keyboard.press('2')
        keyboard.release('2')
        mouse.press(Button.left)
        time.sleep(1.15)
        mouse.release(Button.left)
        mouse.position = (x1 + 234, y1 + 158)
        keyboard.press('2')
        keyboard.release('2')
        keyboard.press('z')
        keyboard.release('z')
        keyboard.press('z')
        keyboard.release('z')
        keyboard.press('z')
        keyboard.release('z')
        keyboard.press('z')
        keyboard.release('z')
        mouse.press(Button.left)
        time.sleep(1.15)
        mouse.release(Button.left)
        mouse.position = (x1 + 175, y1 + 205)
        keyboard.press('1')
        keyboard.release('1')
        keyboard.press('x')
        keyboard.release('x')
        keyboard.press('x')
        keyboard.release('x')
        keyboard.press('x')
        keyboard.release('x')
        mouse.press(Button.left)
        time.sleep(1.15)
        mouse.release(Button.left)
        combo_maker = False
    elif keyboard.is_pressed('v') and szukanie_upper == "2526952" and in_tfm == True and combo_maker == False and autoshaman_toggle_var.get() == 1:
        combo_maker = True
        mouse.position = (x1 + 168, y1 + 74)
        keyboard.press('2')
        keyboard.release('2')
        keyboard.press('z')
        keyboard.release('z')
        keyboard.press('z')
        keyboard.release('z')
        keyboard.press('z')
        keyboard.release('z')
        keyboard.press('z')
        keyboard.release('z')
        mouse.press(Button.left)
        time.sleep(1.5)
        mouse.release(Button.left)
        mouse.position = (x1 + 116, y1 + 73)
        keyboard.press('2')
        keyboard.release('2')
        keyboard.press('z')
        keyboard.release('z')
        keyboard.press('z')
        keyboard.release('z')
        keyboard.press('z')
        keyboard.release('z')
        keyboard.press('z')
        keyboard.release('z')
        keyboard.press('z')
        keyboard.release('z')
        keyboard.press('z')
        keyboard.release('z')
        mouse.press(Button.left)
        time.sleep(1.15)
        mouse.release(Button.left)
        mouse.position = (x1 + 158, y1 + 279)
        keyboard.press('1')
        keyboard.release('1')
        keyboard.press('x')
        keyboard.release('x')
        keyboard.press('x')
        keyboard.release('x')
        keyboard.press('x')
        keyboard.release('x')
        keyboard.press('x')
        keyboard.release('x')
        mouse.press(Button.left)
        time.sleep(1.15)
        mouse.release(Button.left)
        mouse.position = (x1 + 150, y1 + 249)
        keyboard.press('1')
        keyboard.release('1')
        keyboard.press('z')
        keyboard.release('z')
        mouse.press(Button.left)
        time.sleep(1.15)
        mouse.release(Button.left)
        combo_maker = False
    elif keyboard.is_pressed('b') and szukanie_upper == "2526952" and in_tfm == True and combo_maker == False and autoshaman_toggle_var.get() == 1:
        combo_maker = True
        mouse.position = (x1 + 455, y1 + 184)
        keyboard.press('2')
        keyboard.release('2')
        keyboard.press('z')
        keyboard.release('z')
        keyboard.press('z')
        keyboard.release('z')
        keyboard.press('z')
        keyboard.release('z')
        keyboard.press('z')
        keyboard.release('z')
        keyboard.press('z')
        keyboard.release('z')
        keyboard.press('z')
        keyboard.release('z')
        mouse.press(Button.left)
        time.sleep(1.15)
        mouse.release(Button.left)
        mouse.position = (x1 + 427, y1 + 261)
        keyboard.press('2')
        keyboard.release('2')
        keyboard.press('x')
        keyboard.release('x')
        keyboard.press('x')
        keyboard.release('x')
        mouse.press(Button.left)
        time.sleep(1.15)
        mouse.release(Button.left)
        mouse.position = (x1 + 477, y1 + 195)
        keyboard.press('3')
        keyboard.release('3')
        keyboard.press('z')
        keyboard.release('z')
        mouse.press(Button.left)
        time.sleep(1.15)
        mouse.release(Button.left)
        combo_maker = False

    if autoshaman_toggle_var.get() == 1:
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
    if event.name == '|':
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
        guiz.withdraw()
    elif x1 + 350 <= xmospos <= x1 + 475 and y1 + 290 <= ymospos <= y1 + 330 and szukanie_upper == "2526952" and autoshaman_toggle_var.get() == 1:
        windowz.geometry("20x20+{}+{}".format(x1 + 350, y1 + 290))
        guiz.geometry("20x20+{}+{}".format(x1 + 200, y1 + 165))
        labelz.config(text="C")
        guiz.deiconify()
        windowz.deiconify()
    elif x1 + 40 <= xmospos <= x1 + 160 and y1 + 360 <= ymospos <= y1 + 395 and szukanie_upper == "2526952" and autoshaman_toggle_var.get() == 1:
        windowz.geometry("20x20+{}+{}".format(x1 + 40, y1 + 360))
        guiz.geometry("20x20+{}+{}".format(x1 + 160, y1 + 165))
        labelz.config(text="V")
        guiz.deiconify()
        windowz.deiconify()
    elif x1 + 600 <= xmospos <= x1 + 760 and y1 + 360 <= ymospos <= y1 + 395 and szukanie_upper == "2526952" and autoshaman_toggle_var.get() == 1:
        windowz.geometry("20x20+{}+{}".format(x1 + 600, y1 + 360))
        guiz.geometry("20x20+{}+{}".format(x1 + 390, y1 + 276))
        labelz.config(text="B")
        guiz.deiconify()
        windowz.deiconify()
    else:
        windowz.withdraw()
        guiz.withdraw()
    root.after(50, tooltip)


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
                                   command=autoshaman_toggle, bg="blue", fg="white", highlightthickness=0)
autoshaman_switch.place(x=23, y=71)

clickrs_toggle_var = tk.IntVar()
clickrs_switch = tk.Checkbutton(root, text="? Cannons", variable=clickrs_toggle_var,
                                command=clickrs_toggle, bg="blue", fg="white", highlightthickness=0)
clickrs_switch.place(x=23, y=90)

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

# gui z2
guiz = tk.Toplevel(root)
guiz.overrideredirect(True)
guiz.geometry("20x20+100+200")
guiz.configure(bg="red")

guiz.withdraw()

root.mainloop()
