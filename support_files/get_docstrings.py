import os

curr_directory = os.getcwd()

print(curr_directory)


directory = os.path.join(
    curr_directory, 'Ben Stivenson. Python exercises\chapter 1')

files = os.listdir(directory)

open(f'{directory}/files_describes.txt', 'w', encoding='utf8').close()

for file in files:
    if file != 'files_describes.txt':
        with open(f'{directory}/{file}', 'r', encoding='utf8') as curr_file:
            with open(f'{directory}/files_describes.txt', 'a', encoding='utf8') as outp_file:
                outp_file.write(curr_file.readline())
