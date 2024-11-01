import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.models as models
import torchvision.transforms as transforms
from torch.utils.data import DataLoader, Dataset
from tqdm import tqdm
import matplotlib.pyplot as plt
import pandas as pd

# 定义多个预训练模型
class DLModels:
    @staticmethod
    def resnet18(output_dim):
        model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
        model.fc = nn.Linear(model.fc.in_features, output_dim)
        return model

    @staticmethod
    def resnet50(output_dim):
        model = models.resnet50(weights=models.ResNet50_Weights.DEFAULT)
        model.fc = nn.Linear(model.fc.in_features, output_dim)
        return model

    @staticmethod
    def vgg16(output_dim):
        model = models.vgg16(weights=models.VGG16_Weights.DEFAULT)
        model.avgpool = nn.AdaptiveAvgPool2d((7, 7))  # 修改池化层以适应输入大小
        model.classifier[6] = nn.Linear(model.classifier[6].in_features, output_dim)
        return model

    @staticmethod
    def densenet121(output_dim):
        model = models.densenet121(weights=models.DenseNet121_Weights.DEFAULT)
        model.classifier = nn.Linear(model.classifier.in_features, output_dim)
        return model

    @staticmethod
    def mobilenet_v2(output_dim):
        model = models.mobilenet_v2(weights=models.MobileNet_V2_Weights.DEFAULT)
        model.classifier[1] = nn.Linear(model.classifier[1].in_features, output_dim)
        return model