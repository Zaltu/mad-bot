"""
Sample test config for AigisConfig type
"""
PLUGIN_TYPE = "external"
ENTRYPOINT = "{root}"
LAUNCH = ["python36", "src/main.py"]

SYSTEM_REQUIREMENTS = ["python36", "pip3.6"]

REQUIREMENT_COMMAND = "pip3.6 install -r"
REQUIREMENT_FILE = "{root}/requirements.txt"

SECRETS = {
    "discordKey.secret": "{root}/src/db/",
    "ip.config": "{root}/src/db/",
    "tenor.secret": "{root}/src/db/"
}
