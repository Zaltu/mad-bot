"""
Sample test config for AigisConfig type
"""
PLUGIN_TYPE = "external"
ENTRYPOINT = "{root}"
LAUNCH = "python3.6 src/main.py"

SYSTEM_REQUIREMENTS = ["python3.6", "pip3.6"]

REQUIREMENT_COMMAND = "pip3.6 install -r"
REQUIREMENT_LIST = ["../requirements.txt"]
