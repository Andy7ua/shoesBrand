import shutil
import os

data_dir = 'resized_img'  # Catalog with the initial data set
train_dir = 'resized_img/train'
val_dir = 'resized_img/valid'
test_dir = 'resized_img/test'

val_data_portion = 0.15
test_data_portion = 0.15
classes = os.listdir(data_dir)

if __name__ == '__main__':
    def create_directory(dir_name):
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
        os.makedirs(dir_name)
        for name in classes:
            os.makedirs(os.path.join(dir_name, name))

    create_directory(train_dir)
    create_directory(val_dir)
    create_directory(test_dir)


    def copy_images(start_indexes, end_indexes, source_dir, dest_dir):
        k = 0
        for name in classes:
            curr_dir = source_dir + '/' + name
            files = os.listdir(curr_dir)

            for i, file in enumerate(files):
                if start_indexes[k] <= i < end_indexes[k]:
                    shutil.copy2(os.path.join(curr_dir, file),
                                 os.path.join(dest_dir, name))
            k += 1


    def create_dataset(source_dir, dest_dir, subset):
        start_val_data_idxs = []
        start_test_data_idxs = []
        end_data_idxs = []

        if subset == 'train':
            for name in classes:
                nb_of_images = int(len(os.listdir(source_dir + '/' + name)))
                start_val_data_idxs.append(nb_of_images * (1 - val_data_portion - test_data_portion))

            copy_images([0] * len(classes), start_val_data_idxs, source_dir, dest_dir)

        elif subset == 'val':
            for name in classes:
                nb_of_images = int(len(os.listdir(source_dir + '/' + name)))
                start_val_data_idxs.append(int(nb_of_images * (1 - val_data_portion - test_data_portion)))
                start_test_data_idxs.append(int(nb_of_images * (1 - test_data_portion)))

            copy_images(start_val_data_idxs, start_test_data_idxs, source_dir, dest_dir)

        elif subset == 'test':
            for name in classes:
                nb_of_images = int(len(os.listdir(source_dir + '/' + name)))
                start_test_data_idxs.append(int(nb_of_images * (1 - test_data_portion)))
                end_data_idxs.append(nb_of_images)

            copy_images(start_test_data_idxs, end_data_idxs, source_dir, dest_dir)

        else:
            print('Subset must be: "train", "val" or "test"!')

    create_dataset(data_dir, train_dir, 'train')
    create_dataset(data_dir, val_dir, 'val')
    create_dataset(data_dir, test_dir, 'test')
