import segmentation_models as sm
import numpy as np
import cv2 as cv
from keras.models import load_model
import os
import sys
from PIL import Image

def predict(image_path, out_folder, model):
    #Load images
    SIZE = 256
    image_names = sorted(next(os.walk(image_path))[-1])
    images = np.zeros(shape=(len(image_names),SIZE, SIZE, 3))
    for i in range(len(image_names)):
      path = image_path + image_names[i]
      img = np.asarray(Image.open(path)).astype('float')/255
      img = cv.resize(img, (SIZE,SIZE), cv.INTER_AREA)
      images[i] = img
    print('Número de imágenes:' + str())

    #Load model
    BACKBONE = 'efficientnetb1'
    preprocess_input = sm.get_preprocessing(BACKBONE)
    model = sm.Unet(BACKBONE, encoder_weights='imagenet')

    model.compile(
        'Adam',
        loss=sm.losses.bce_jaccard_loss,
        metrics=[sm.metrics.iou_score, "accuracy", "AUC"],
    )
    model = load_model(model,compile=False)
    # Make predictions
    predictions = model.predict(images)
    i=0
    for p in predictions:
        cv.imwrite(out_folder + image_names[i], p*255)
        i+=1
        
if __name__ == "__main__":
    image_path=sys.argv[1]
    output_folder = sys.argv[2]
    model = sys.argv[3]
    predict(image_path, output_folder, model)
    sys.exit(0)        