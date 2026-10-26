import logging
import sys
from pathlib import Path


def setup_logger(log_dir, name="sparse_scene", level=logging.INFO) -> logging.Logger:
    log_dir = Path(log_dir)
    log_dir.mkdir(parents= True, exist_ok = True) # for making the directory where logger output will be saved

    logger = logging.getLogger(name)   # definig logger here
    logger.setLevel(level)              # setting the level of logger as INFO but can be changed in particular scripts when setup_logger function is called
    logger.propagate = False            # logger documentation says it is something related to root logger and if configured for root logger then will be print twice 

    if logger.handlers:
        return logger

    fmt = logging.Formatter("%(asctime)s | %(levelname)-7s | %(message)s", "%H:%M:%S") #fromatter is defined

    console = logging.StreamHandler(sys.stdout)     #console for the terminal output
    console.setFormatter(fmt)
    console.setLevel(level)
    logger.addHandler(console)

    file_handler = logging.FileHandler(log_dir/ f"{name}.log", encoding ="utf-8")  #for the files that will be saved, we will arrange the name and format
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(fmt)
    logger.addHandler(file_handler)

    return logger
