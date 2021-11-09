from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg19 import VGG19, preprocess_input
from tensorflow.keras.models import Model
import numpy as np

class FeatureExtractor:
    def __init__(self):
        """
        VGG19模型的初始化
        """
        self.base_model = VGG19(weights="imagenet")  # 使用了转移学习
        self.model = Model(inputs=self.base_model.input, outputs=self.base_model.get_layer("fc1").output)  # fc1层输出

    def extract(self, img):
        """
        从图片中提取出特征向量
        :param img:使用PILLOW读取的图片
        :return:特征向量
        """
        height = 224
        width = 224
        img = img.resize((height, width)).convert("RGB")
        x = image.img_to_array(img)  # 转为np.array
        # print(np.shape(x))
        x = np.expand_dims(x, axis=0)  # (H, W, C) -> (1, H, W, C)
        # print(np.shape(x))
        # print(self.model.predict(x))
        feature = self.model.predict(x)[0]  # (1, 4096) -> (4096)
        return feature/np.linalg.norm(feature)  # 标准化