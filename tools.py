import json
import matplotlib.pyplot as plt
def save_json(data, filename):
    """
    将字典保存为JSON文件。
    
    参数:
        data (dict): 需要保存的字典。
        filename (str): 保存的文件名。
    """
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)  # 使用indent进行美化输出

def load_json(filename):
    """
    从JSON文件读取数据到字典。
    
    参数:
        filename (str): 要读取的文件名。
        
    返回:
        dict: 从JSON文件中读取的字典。
    """
    with open(filename, 'r') as f:
        data = json.load(f)
    return data



# 可视化训练和验证结果
def plot_metrics(epochs, train_losses, val_losses, val_accuracies):
    plt.figure(figsize=(12, 5))

    # 绘制训练和验证损失
    plt.subplot(1, 2, 1)
    plt.plot(range(1, epochs + 1), train_losses, label='Train Loss')
    plt.plot(range(1, epochs + 1), val_losses, label='Validation Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.title('Train and Validation Loss')
    plt.legend()

    # 绘制验证准确率
    plt.subplot(1, 2, 2)
    plt.plot(range(1, epochs + 1), val_accuracies, label='Validation Accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.title('Validation Accuracy')
    plt.legend()

    plt.show()