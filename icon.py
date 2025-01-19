from PIL import Image
import os

def create_ico():
    img = Image.open('TEAM_P0P0_PRESENTS_CUT.png')
    
    # Расширенный список размеров
    sizes = [(16,16), (20,20), (24,24), (32,32), (40,40), (48,48), 
             (64,64), (96,96), (128,128), (256,256)]
    
    # Создаем временный список для хранения изображений
    icon_sizes = []
    
    # Конвертируем в RGBA если нужно
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    for size in sizes:
        # Создаем копию с сохранением пропорций
        resized_img = img.copy()
        resized_img.thumbnail(size, Image.Resampling.LANCZOS)
        icon_sizes.append(resized_img)
    
    # Сохраняем иконку
    img.save('KEYGEN.ico', 
            format='ICO',
            sizes=sizes,
            append_images=icon_sizes[1:],
            optimize=True)

if __name__ == '__main__':
    create_ico()