import configparser

import os
from dotenv import load_dotenv
load_dotenv()

config = configparser.RawConfigParser()
config.read("Configurations/config.ini")


class ReadConfig:
    @staticmethod
    def getOrganizationstelnyxkey():
        Organizations_telnyx_key = os.getenv('ORGANIZATIONS_TELNYX_KEY')
        return Organizations_telnyx_key















