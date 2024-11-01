import logging
import logging.handlers

def setup_logger(log_path):
    # 获取日志记录器
    logger = logging.getLogger(__name__)
    
    # 如果已经有处理器，就不再重复添加
    if not logger.handlers:
        # 设置最低日志级别
        logger.setLevel(logging.DEBUG)

        # 创建文件处理器，用于写入日志文件
        file_handler = logging.FileHandler(log_path)
        file_handler.setLevel(logging.DEBUG)

        # 创建控制台处理器，用于输出到控制台
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # 设置日志格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # 将处理器添加到日志记录器中
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
