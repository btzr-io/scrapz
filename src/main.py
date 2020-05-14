#----------------- #
#  Import modules  #
# ---------------- #

from chainquery  import query, queries

# Basic options
queryOptions = {
    'limit': 1,
}

# Example usage
data = query(
    # Predefined query:
    queries.contentAudio(),
    # Query options
    queryOptions
)

print(data)
