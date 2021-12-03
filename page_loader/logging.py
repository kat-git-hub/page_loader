#import logging.config
import logging
import sys

#LEVELS = {'CRITICAL' : l.critical,
##    'ERROR' : l.error,
##    'WARNING' : l.warning,
 #   'INFO' : l.info,
 #   'DEBUG' : l.debug
#}

#def config_log(name):
#    handlers = logging.StreamHandler(sys.stderr)
##    handlers.setLevel(logging.INFO)
#    formatter = logging.Formatter('%(name)s - %(levelname)s : %(message)s')
#    logger = logging.getLogger(name)
#    logger.getLevelName(logging.DEBUG)
    
#    return logger.basicConfig(level=logger.getLevelName(logging.DEBUG), format=formatter, handlers= handlers)


#LOGGING_CONFIG = {
#    "version":1,
#    "root":{
#        "handlers" : ["console"],
#        "level": "DEBUG"
 #   },
 #   "handlers":{
 #       "console":{
 #           "formatter": "std_out",
 #           "class": "logging.StreamHandler",
 #           "level": "DEBUG"
 #       }
 #   },
 #   "formatters":{
 ##       "std_out": {
 #           "format": "%(asctime)s : %(levelname)s : %(module)s : %(funcName)s : %(lineno)d \nLog : %(message)s",
 #           "datefmt":"%d-%m-%Y %I:%M:%S"
 #       }
 #   },
#}
#LOGGING_CONFIG = {
#    "version":1,
#    "root":{
#        "handlers" : ["console"],
#        "level": "DEBUG"
#    },
#    "handlers":{
#        "console":{
#            "formatter": "std_out",
#            "class": "logging.StreamHandler",
#            "level": "DEBUG"
#        
#        }
#    },
#    "formatters":{
#        "std_out": {
#            "format": "%(asctime)s : %(levelname)s : %(module)s : %(funcName)s : %(lineno)d : (Process Details : (%(process)d, %(processName)s), Thread Details : (%(thread)d, %(threadName)s))\nLog : %(message)s",
#            "datefmt":"%d-%m-%Y %I:%M:%S"
#        }
#    },
#}

LOGGING_CONFIG = { 
    'version': 1,
    'disable_existing_loggers': True,
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
        },
    },
    'loggers': { 
        '': {  # root logger
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': False
        },
        'page_loader': { 
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': False
        },
        'page_loader': {  # if __name__ == '__main__'
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': False
        },
    } 
}


