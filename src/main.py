#----------------- #
#  Import modules  #
# ---------------- #

# Http / https requests
import requests

# Type checking
from typing import Final

#--------------------- #
#  Constant variables  #
# -------------------- #

# Public chainquery API
CHAINQUERY_API: Final = "https://chainquery.lbry.io/api";
CHAINQUERY_API_SQL: Final = CHAINQUERY_API + "/sql";

# The mature tag is the first entry on the tags table
MATURE_TAG_ID: Final = 1;

#--------------- #
#  Inital test   #
# -------------- #

try:
    # Send the sql query as url parameter
    payload = {'query': ''}

    # Initial request test
    response = requests.get(CHAINQUERY_API)

    # Parse to json
    response.raise_for_status()

    # Print to console
    print(response.json())

# Handle connection error
except requests.ConnectionError as error:
     print("[!] Connection error: {0}".format(error))

# Handle http error ( 404, 503, etc... )
except requests.HTTPError as error:
    print("[!] Http error: {0}".format(error))
