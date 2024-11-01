from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

class ModelSelector:
    def __init__(self, random_state=3220821):
        self.random_state = random_state

        self.models = {
            'random_forest': RandomForestClassifier(random_state=self.random_state),
            'gradient_boosting': GradientBoostingClassifier(random_state=self.random_state),
            'decision_tree': DecisionTreeClassifier(random_state=self.random_state),
            'adaboost': AdaBoostClassifier(random_state=self.random_state),
            'logistic_regression': LogisticRegression(random_state=self.random_state),
            'svm': SVC(probability=True, random_state=self.random_state),
            'k_neighbors': KNeighborsClassifier()
        }

    def get_model(self, model_name):
        """
        返回指定名称的模型实例。

        参数:
            model_name (str): 模型的名称。

        返回:
            model (sklearn.base.BaseEstimator): 请求的机器学习模型。

        抛出:
            ValueError: 如果模型名称不在预定义列表中。
        """
        try:
            return self.models[model_name]
        except KeyError:
            raise ValueError(f"Model '{model_name}' not found. Available models: {list(self.models.keys())}")

# # 使用示例
# selector = ModelSelector()
# model = selector.get_model('decision_tree')  # 获取决策树模型
# print(model)
