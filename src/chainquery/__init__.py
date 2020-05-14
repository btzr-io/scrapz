#----------------- #
#  Import modules  #
# ---------------- #

import requests as req
from typing import Final

#--------------------- #
#  Constant variables  #
# -------------------- #

# Public chainquery API base url:
CHAINQUERY_API: Final = "https://chainquery.lbry.io/api";
# Public chainquery API for sql queries:
CHAINQUERY_API_SQL: Final = CHAINQUERY_API + "/sql";

def formatQuery(q):
    return q.get_sql().replace('"', '')

def query(q, options):
    try:
        # Apply options
        q = q.limit(options['limit'])
        # Preapare string for url encoding
        queryString = formatQuery(q)
        # Send the sql query as url parameter
        payload = {'query': queryString }
        # Initial request test
        res = req.get(CHAINQUERY_API_SQL, params = payload)
        res.raise_for_status()
        # Parse to json and return results
        res = res.json()
        data = res['data']
        return data

    # Handle connection error
    except req.ConnectionError as error:
        print("[!] Connection error: {0}".format(error))

    # Handle http error ( 404, 503, etc... )
    except req.HTTPError as error:
        print("[!] Http error: {0}".format(error))
