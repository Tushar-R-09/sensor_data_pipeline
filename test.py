from src.kafka_logger.logger import logging


def add(a,b):

    logging.info("Add function is called")

    res = a+b

    logging.info(f"result of addition of {a} and {b} is {res}")

    return res


add(3,4)
