import logging


class Logger:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        handler = self.get_handler()
        self.logger.addHandler(handler)

    def get_handler(self):
        handler = logging.FileHandler('log.txt')
        handler.setLevel(logging.DEBUG)
        log_format = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(log_format)
        return handler
