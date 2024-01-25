import os
from PIL import Image


def resize_image(image_path, output_path, size=(128, 128)):
    image = Image.open(image_path)
    resized_image = image.resize(size)
    resized_image.save(output_path)


def process_folders(source_folder):
    dataset_folder = os.path.join(os.getcwd(), 'dataset')
    os.makedirs(dataset_folder, exist_ok=True)

    folders = [f for f in os.listdir(source_folder) if os.path.isdir(os.path.join(source_folder, f))]

    min_images_count = float('inf')
    min_images_folder = None

    for folder in folders:
        folder_path = os.path.join(source_folder, folder)
        images_count = len([f for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg'))])

        if images_count < min_images_count:
            min_images_count = images_count
            min_images_folder = folder

    print(f"Copying and resizing images. Total folders: {len(folders)}, Minimum images count: {min_images_count}")

    for folder in folders:
        source_path = os.path.join(source_folder, folder)
        destination_path = os.path.join(dataset_folder, folder)
        os.makedirs(destination_path, exist_ok=True)

        images_to_process = os.listdir(source_path)[:min_images_count]
        for i, image_name in enumerate(images_to_process):
            image_path = os.path.join(source_path, image_name)
            output_path = os.path.join(destination_path, image_name)

            resize_image(image_path, output_path)
            print(f"Processed image {i + 1}/{min_images_count} in folder {folder}")

        # Remove excess files in folders with more images
        if folder != min_images_folder:
            excess_files = os.listdir(source_path)[min_images_count:]
            for excess_file in excess_files:
                excess_file_path = os.path.join(source_path, excess_file)
                os.remove(excess_file_path)
                print(f"Removed excess file: {excess_file} in folder {folder}")


if __name__ == "__main__":
    folder_path = "dataset"
    process_folders(folder_path)
