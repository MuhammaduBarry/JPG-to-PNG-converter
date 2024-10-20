from PIL import Image
import sys
import os
# JPG to PNG converter

# Folder that contains files
jpg_folder = sys.argv[1]
new_folder = sys.argv[2]

# Check to see if new_folder exist
try:
    if not os.path.exists(new_folder):
        os.mkdir(new_folder)

        # Loop through jpg folder
        files = os.listdir(jpg_folder)
        for file in files:
            img = Image.open(f'./{jpg_folder}/{file}')
            png_file_name = f'{file.split('.')[0]}.png' # New file name
            img.save(f'./{new_folder}/{png_file_name}', 'png')
except Exception  as err:
    print(f'An error has occurred: {err}')