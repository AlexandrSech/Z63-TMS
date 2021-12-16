from loguru import logger

def timeit(foo):
    def wrapper():
        logger.add("logg.log",
        format="{time}::{level}::{message}",
        level="DEBUG",
        rotation= "10 Mb")
        logger.debug("Start foo")
        result = foo()
        logger.debug("Finish foo")

        return result
    return wrapper

