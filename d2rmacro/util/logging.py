import logging
import logging.config
import sys


def init_logging(name, level):
    logging_conf = {
        'version': 1,
        'formatters': {
            'standard': {
                'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                'datefmt': '%Y-%m-%d - %H:%M:%S'},
        },
        'handlers': {
            'console': {'class': 'logging.StreamHandler',
                        'formatter': "standard",
                        'level': level,
                        'stream': sys.stdout
                        },
            'file': {
                'formatter': "standard",
                'level': level,
                'filename': 'd2r_overlay.log',
                'mode': 'w',
                'class': 'logging.FileHandler',
            }
        },
        'loggers': {
            name: {'level': 'INFO',
                   'handlers': ['console', 'file'],
                   'propagate': False},
        }
    }

    logging.config.dictConfig(logging_conf)
    log = logging.getLogger(name)
    log.setLevel(level)
    return log


log = init_logging("d2r_overlay", logging.DEBUG)
