LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '  %(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout'
        },
        'errors': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'standard'
        }
    },
    'loggers': {
        '': {
            'handlers': ['default', 'errors'],
            'level': 'DEBUG',
            'propagate': False
        },
        'page_loader': {
            'handlers': ['default', 'errors'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}
