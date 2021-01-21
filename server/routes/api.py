
from flask import jsonify
from server import app
import os
import json
import logging
import logging.handlers
from flask import request

# resource_path = "/resources"

#RESOURCES FOLDER
#discriminiamo il path in base alla macchina su cui gira l'applicativo
if os.uname()[4] == 'ppc64le':
    resource_path = "/resources"
else:
    resource_path = '/Users/it058917/work/ENI/Progetti/git/annotatori/caption/CD-annotator/resources'
#############


#ENV
# Get environment variables
n = os.getenv('from')
greeting = os.environ.get('greeting')
######

# #LOGGING
# LOG_FILENAME = os.path.join(resource_path, 'logging.log')
# my_logger = logging.getLogger('MyLogger')
# my_logger.setLevel("INFO")
# # create formatter
# formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(module)s;%(message)s","%Y-%m-%d %H:%M:%S")
# # Add the log message handler to the logger
# handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=10000, backupCount=5)
# handler.setFormatter(formatter)
# my_logger.addHandler(handler)
############

#LOGGING
LOG_FILENAME = os.path.join(resource_path, 'logging.log')
#LOG_FILENAME = 'logging.log'
my_logger = logging.getLogger('MyLogger')
#my_logger.setLevel(level_logging)
my_logger.setLevel("INFO")
# create formatter
formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(module)s;%(message)s","%Y-%m-%d %H:%M:%S")
# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=10000, backupCount=5)
handler.setFormatter(formatter)
my_logger.addHandler(handler)
############

@app.route("/check")
def check():
    """health route"""
    user = request.args.get('name')
    state = {greeting +"da " + n:user }
    my_logger.info(state)
    #my_logger.info("Function called by " + username)
    return jsonify(state)
