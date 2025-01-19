import random
import string
import time
from tkinter import Tk, Label, Button, Entry, Frame, LabelFrame
import threading
import pyperclip
from PIL import Image, ImageTk
import base64
import io
import os
import sys

# Определяем путь к файлу
def resource_path(relative_path):
    """ Получаем абсолютный путь к ресурсу """
    try:
        # PyInstaller создает временную папку и хранит путь в _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Читаем закодированное изображение из файла
with open(resource_path("encoded_image.txt"), "r", encoding='utf-8') as file:
    BACKGROUND_IMAGE = file.read().strip()

# Создание интерфейса
root = Tk()
root.title("KEYGEN")
root.geometry("960x540")
root.configure(bg='black')
root.resizable(False, False)

# Центрирование окна на экране
window_width = 960
window_height = 540
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Создаем фоновое изображение
bg_image_data = base64.b64decode(BACKGROUND_IMAGE)
bg_image = Image.open(io.BytesIO(bg_image_data))
bg_image = bg_image.resize((960, 540))
bg_photo = ImageTk.PhotoImage(bg_image)

# Добавляем фоновое изображение
bg_label = Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

def typewriter_effect(entry, text, delay=0.05):
    entry.config(state='normal')
    entry.delete(0, 'end')
    for i in range(len(text)):
        entry.insert('end', text[i])
        entry.update()
        time.sleep(delay)
    entry.config(state='readonly')

def loading_animation():
    loading_texts = ["system breach in progress", "searching database", "bypassing security", "generating access key"]
    dots = [".", "..", "..."]
    
    for text in loading_texts:
        for dot in dots:
            status_label.config(text=f"{text}{dot}")
            time.sleep(0.3)
    
def copy_key():
    key_text = key_label.cget("text")
    if key_text:
        actual_key = key_text.split(": ")[1]
        pyperclip.copy(actual_key)
        status_label.config(text="key copied", fg="#00ff00")
        root.after(2000, lambda: status_label.config(text="waiting for input...", fg="#ff0000"))

def key_generation():
    time.sleep(3)
    typewriter_effect(key_label, "1998-2207-MOMMY-BOSS")
    status_label.config(text="access granted", fg="#00ff00")

def generate_key():
    threading.Thread(target=loading_animation, daemon=True).start()
    status_label.config(fg="#111111")
    threading.Thread(target=key_generation, daemon=True).start()

def close_app():
    status_label.config(text="shutting down...", fg="#ff0000")
    time.sleep(1)
    root.destroy()

# Создаем основную рамку
main_frame = Frame(root, bg='#404040', bd=2, relief='ridge')
main_frame.place(relx=0.3, rely=0.4, anchor='center', width=500, height=280)

# Заголовок Hardware Code
Label(main_frame, text="Hardware Code :", font=("Terminal", 10), 
      bg='#404040', fg="#C0C0C0", anchor='w').pack(padx=20, pady=(15,5), anchor='w')

# Поле для ввода кода
name_entry = Entry(main_frame, font=("Terminal", 12), bg="white", fg="black",
                  justify='center', width=40, borderwidth=1,
                  relief='sunken')
name_entry.pack(padx=20, pady=5)
name_entry.insert(0, "-TEAM 2P20 PRESENTS-")

# Заголовок Log
Label(main_frame, text="Log :", font=("Terminal", 10), 
      bg='#404040', fg="#C0C0C0", anchor='w').pack(padx=20, pady=5, anchor='w')

# Поле для вывода лога/ключа
key_label = Entry(main_frame, font=("Terminal", 12),
                bg="white", fg="black", justify='center',
                readonlybackground="white", state='readonly', width=40,
                relief='sunken')
key_label.pack(padx=20, pady=5)
key_label.insert(0, "-TEAM 2P20 PRESENTS-")

# Рамка для кнопок
button_frame = Frame(main_frame, bg='#404040')
button_frame.pack(pady=15)

# Кнопки
generate_button = Button(button_frame, text="Generate", font=("Terminal", 10),
    command=generate_key, width=18, relief='raised',
    bg='#D0D0D0', activebackground='#E0E0E0')
generate_button.pack(side="left", padx=12)

exit_button = Button(button_frame, text="Exit", font=("Terminal", 10),
    command=close_app, width=18, relief='raised',
    bg='#D0D0D0', activebackground='#E0E0E0')
exit_button.pack(side="left", padx=12)

# Возвращаем статус лейбл
status_label = Label(main_frame, text="waiting for input...", font=("Terminal", 10),
                    bg='#404040', fg="#ff0000")
status_label.pack(pady=10)

root.mainloop()
