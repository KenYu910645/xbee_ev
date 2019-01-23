import os
import yaml
from global_var.global_logger import logger
from pprint import pprint, pformat

# Load parameters
f = open(os.path.join(os.path.dirname(__file__), "../param.yaml") ,'r')
params_raw = f.read()
f.close()
param_dict = yaml.load(params_raw)

# Load parameters
WAIT_AWK_MAX_TIME = param_dict['WAIT_AWK_MAX_TIME'] # sec 
MAX_RESEND_TIMES = param_dict['MAX_RESEND_TIMES'] # sec 
KEEPALIVE = param_dict['KEEPALIVE'] # sec 
KEPPALIVE_MAX = param_dict['KEPPALIVE_MAX'] # sec 

# Print out parameters
logger.info("[param_loader] WAIT_AWK_MAX_TIME = " + pformat(WAIT_AWK_MAX_TIME))
logger.info("[param_loader] MAX_RESEND_TIMES = " + pformat(MAX_RESEND_TIMES))
logger.info("[param_loader] KEEPALIVE = " + pformat(KEEPALIVE))
logger.info("[param_loader] KEPPALIVE_MAX = " + pformat(KEPPALIVE_MAX))
