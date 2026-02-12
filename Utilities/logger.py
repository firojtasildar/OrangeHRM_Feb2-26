import logging
#search-->1)__name__ 2)inspect.stack[1][1]

class Logger_class:
    @staticmethod
    def get_logger():
        logger=logging.getLogger(__name__)
        if not logger.handlers:  # पहले से handler है तो दोबारा add मत करो
            logger.setLevel(logging.INFO)
            handler=logging.FileHandler(".\\Logs\\OrangeHRM.log")
            formatter=logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        return logger


