import os
from appdirs import user_data_dir

APP_NAME = "VPNSwitchboard"
# APP_AUTHOR can be the same as APP_NAME or your specific author/company name
APP_AUTHOR = "VPNSwitchboard" 

def _get_config_file_path() -> str:
    """Gets the platform-specific path for the configuration file."""
    data_dir = user_data_dir(appname=APP_NAME, appauthor=APP_AUTHOR)
    os.makedirs(data_dir, exist_ok=True)
    return os.path.join(data_dir, "configurations.txt")

CONFIG_FILE = _get_config_file_path()

def add_configuration(configuration: str):
    """Adds a new VPN configuration to the storage file if not already present."""
    if not is_configured(configuration):
        with open(CONFIG_FILE, "a") as f:
            f.write(configuration + "\n")

def remove_configuration(configuration: str):
    """Removes a VPN configuration from the storage file."""
    configs = list_configurations()
    if configuration in configs:
        configs.remove(configuration)
        with open(CONFIG_FILE, "w") as f:
            for config in configs:
                f.write(config + "\n")

def list_configurations() -> list[str]:
    """Lists all stored VPN configurations."""
    if not os.path.exists(CONFIG_FILE):
        return []
    with open(CONFIG_FILE, "r") as f:
        return [line.strip() for line in f if line.strip()]

def is_configured(configuration: str) -> bool:
    """Checks if a VPN configuration is already stored."""
    return configuration in list_configurations()
