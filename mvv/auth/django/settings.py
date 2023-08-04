#  _____      _                         _      _____ _____   _____                       _ _   _
# /  ___|    | |                       | |    |_   _|_   _| /  __ \                     | | | (_)
# \ `--.  ___| |__  _ __ ___   ___  ___| | __   | |   | |   | /  \/ ___  _ __  ___ _   _| | |_ _ _ __   __ _
#  `--. \/ __| '_ \| '__/ _ \ / _ \/ __| |/ /   | |   | |   | |    / _ \| '_ \/ __| | | | | __| | '_ \ / _` |
# /\__/ / (__| | | | | | (_) |  __/ (__|   <   _| |_  | |   | \__/\ (_) | | | \__ \ |_| | | |_| | | | | (_| |
# \____/ \___|_| |_|_|  \___/ \___|\___|_|\_\  \___/  \_/    \____/\___/|_| |_|___/\__,_|_|\__|_|_| |_|\__, |
#                                                                                                       __/ |
#                                                                                                      |___/

"""

"""
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent


class OAuthSettings(BaseSettings):
    """
    Settings required for OAuth
    """
    oauth_client_id: str = Field(env="OAUTH_CLIENT_ID")
    oauth_client_secret: str = Field(env="OAUTH_CLIENT_SECRET")
    oauth_conf_url: str = Field(env="OAUTH_CONF_URL")


# AUTHLIB CLIENTS
settings = OAuthSettings(_env_file='.env', _env_file_encoding='utf-8')

# Import this into your Django settings
AUTHLIB_OAUTH_CLIENTS = {
    'keycloak': {
        "client_id": settings.oauth_client_id,
        "client_secret": settings.oauth_client_secret
    }
}
