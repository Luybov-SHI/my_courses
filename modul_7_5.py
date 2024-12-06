import os
import time

directory = os.getcwd ()
for root, dirs, files in os.walk (directory):
    files = [f for f in os.listdir () if os.path.isfile (f)]
    for file in files:
        filepath = os.path.join (file)
        filetime = os.path.getmtime (file)
        formatted_time = time.strftime ("%d.%m.%Y %H:%M", time.localtime (filetime))
        filesize = os.path.getsize (file)
        parent_dir = os.path.dirname (directory)
        print (
            f'Обнаружен файл: {file}, Путь: {filepath},\n '
            f'Размер: {filesize} байт, Время изменения: {formatted_time},\n '
            f'Родительская директория: {parent_dir}\n'
            f'{'_' * 40}')