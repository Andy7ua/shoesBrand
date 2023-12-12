# Shoes Brand pipeline

## Model training
This is ML solution for shoes brand checker

### Instal requirements
1. Install Python requirements
```bash
pip install -r requirements.txt
```
2. Specify parameters (path to images, weight and training parameters) in **config.py**

### Inference
1. Ask for trained weight [here](https://t.me/ya_andy_ua)
2. Set img_path in main.py and run:
```bash
python main.py
```

### Training your own model 
1. Upload your own images and specify path to them or use the default (which you ask [here](https://t.me/ya_andy_ua))

2. Resize images if it necessary by using img_resizer.py

3. Specify variables like: data_dir, gpu_config, img_width, batch_size, img_path, model and other if necessary

4. Run files in such order: img_resizer, config, model_config, model_compile, tuned_model_compile, main

### Do laboratory work
1. Find and download images dataset of at least 3 classes (preferably at least 300 images per class)

2. Make sure that the images are in separate appropriate folders and in one common folder (let's say the "images" folder)

3. Open file img_resizer.py, specify the path to your images folder and also the desired img resize parameters and run the file

4. Open file config.py and run it

5. Open file model_config.py:
5.1 Sets the size of the image to which they were previously resized
5.2 Specify batch_size parameter
5.3 Uncomment vgg16_net and model summary if you need for report

6. Open file model_compile.py, specify number of epochs and run it (make screenshot of training history if you need for report)

7. Open file model_compile.py, uncomment model summary if you need for report, specify number of epochs and run it

8. Open file main.py. Specify model (0 or 1), specify img_path to img which you want to test (uncomment plt.savefig if you want to save result) and run the file

More information [here](https://t.me/ya_andy_ua)

# shoesBrand
