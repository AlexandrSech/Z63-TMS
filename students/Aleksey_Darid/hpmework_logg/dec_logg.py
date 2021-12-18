from loguru import logger

logger.add("debug.json",
format="{time}::{level}::{message}",
level="DEBUG",
rotation= "10 Mb", 
compression="zip",
serialize=True)


@logger.catch
def d(a,s):
    a/s

d(3,0)