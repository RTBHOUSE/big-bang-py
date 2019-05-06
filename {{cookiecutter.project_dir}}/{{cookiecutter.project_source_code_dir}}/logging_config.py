import os

from dirs import PROJECT_ROOT

logs_folder = PROJECT_ROOT / "logs"
os.makedirs(logs_folder, exist_ok=True)

DICT_CONFIG = {
    "version": 1,
    "formatters": {
        "standard": {
            "format": "%(asctime)s %(name)-8s %(levelname)-8s %(message)s",
        },
    },
    "handlers": {
        "stderr": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "standard",
        },
        "rotating_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "formatter": "standard",
            "filename": logs_folder / "logs.log",
            # Set max log file size to 1MB.
            "maxBytes": 1024 * 1024,
            # At most `backupCount` of backup log files will be kept. If more
            # would be created when rollover occurs, the oldest one is deleted.
            "backupCount": 2,
        },
    },
    "loggers": {
        "main": {
            "handlers": ["stderr", "rotating_file_handler"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}
