from src.logger import logging
from src.exception import MyException
import sys

try:
    a = 1 / 0
except Exception as e:
    logging.info("Divide by zero error occurred")
    raise MyException(e, sys) from e