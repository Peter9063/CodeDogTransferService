import logging

class LoggerHelp():
    @staticmethod
    def getDefaultLogger(name):
            logger= logging.getLogger(name)
            handler =logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(logging.INFO)
            return logger
