#----------------- #
#  Import modules  #
# ---------------- #

import requests as req
from typing import Final
from pypika import Query, Table

#--------------------- #
#  Constant variables  #
# -------------------- #

# Public chainquery API endpoints:
CHAINQUERY_API: Final = "https://chainquery.lbry.io/api";
CHAINQUERY_API_SQL: Final = CHAINQUERY_API + "/sql";

# The mature tag is the first entry on the tags table
MATURE_TAG_ID: Final = 1;

#-------------- #
#  Test query   #
# ------------- #

def testQuery():
    claim = Table('claim')
    # Basic query
    q =  Query.from_(claim).select(claim.name, claim.claim_id).limit(10)
    # returns string from query
    return q.get_sql().replace('"', '')

#--------------------- #
#  Chainqury wrapper   #
# -------------------- #

def query():
    try:
        # Build query string
        q = testQuery()
        # Send the sql query as url parameter
        payload = {'query': q }

        # Initial request test
        res = req.get(CHAINQUERY_API_SQL, params = payload)

        res.raise_for_status()

        # Parse to json
        res = res.json()

        data = res['data']

        print(data)

    # Handle connection error
    except req.ConnectionError as error:
        print("[!] Connection error: {0}".format(error))

    # Handle http error ( 404, 503, etc... )
    except req.HTTPError as error:
        print("[!] Http error: {0}".format(error))
