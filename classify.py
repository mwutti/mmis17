from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
from PIL import Image
import requests
from io import BytesIO


class Classify:
    imageSize = 224, 224

    def __init__(self):
        self.model = ResNet50(weights='imagenet')

    def classifyImagesByUrls(self, imageUrls, imageUrls_org):
        result = []
        for i, url in enumerate(imageUrls):

            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            if not img.format == 'PNG':
                img = img.resize(self.imageSize)
                x = image.img_to_array(img)
                x = np.expand_dims(x, axis=0)
                x = preprocess_input(x)

                preds = self.model.predict(x)
                decoded_predictions = decode_predictions(preds, top=3)[0]
                result.append((url, decoded_predictions[0][1], decoded_predictions[0][2], decoded_predictions[1][1],
                               decoded_predictions[1][2], decoded_predictions[2][1], decoded_predictions[2][2],
                               imageUrls_org[i]))
        return result
