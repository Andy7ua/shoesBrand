from PIL import Image
import os

# The path to the folder with the source images
source_root = 'images/'

# The path to the folder where the resized images will be saved
output_root = 'resized_img/'

new_size = (104, 104)  # set new img size

# Iterate through all subdirectories in the source folder
for root, dirs, files in os.walk(source_root):
    for dir in dirs:
        source_folder = os.path.join(root, dir)
        output_folder = os.path.join(output_root, dir)

        # Ensure the output folder exists, create it if it doesn't
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Process images in the current source folder
        for filename in os.listdir(source_folder):
            if filename.endswith('.jpg') or filename.endswith('.png'):
                img = Image.open(os.path.join(source_folder, filename))
                img = img.resize(new_size, Image.BILINEAR)
                img.save(os.path.join(output_folder, filename))

print("The images from source_folder were successfully resized and saved to output_folder!")
