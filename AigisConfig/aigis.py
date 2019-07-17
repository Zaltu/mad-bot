"""
Sample test config for AigisConfig type
"""
from types import SimpleNamespace

SECRETS = SimpleNamespace()

PLUGIN_TYPE = "multiprocess"

RUN_HOST = None
RUN_METHOD = "python3.6"
RUN_CMD = "python3.6 {root}/src/main.py"

REQUIREMENT_TYPE = "pip3.6"
REQUIREMENT_LIST = "{root}/requirements.txt"
