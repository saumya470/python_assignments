# Below are different levels of the logging the messages in order
# Default log level is warning, i.e., logger logs all messages above warning level

import logging
#To import the messages in a file instead of console.
#This creates a file where we can see all the looging messages, above the level defined in level
logging.basicConfig(filename='Myfile.log',level=logging.WARNING)

logging.critical('Critical')
logging.error('Error')
logging.warning('Warning')
logging.info('Info')
logging.debug('Debug')


