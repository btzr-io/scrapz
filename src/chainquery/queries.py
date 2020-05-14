from pypika import Query, Table, functions as fn

#  local modules
from .constants import TABLE_NAME, CLAIM_TYPE, CONTENT_TYPE

#---------------- #
#  Useful queries #
# --------------- #

def contentType(contentType):
    claim = Table(TABLE_NAME['CLAIM'])
    # Basic query
    q =  Query.from_(claim).select(
        #claim.title,
        #claim.claim_id,
        #claim.content_type,
        '*'
    ).where(
        claim.type == CLAIM_TYPE['STREAM']
    ).where(
        claim.content_type.like(contentType + '%')
    )
    # returns new query
    return q


def contentAudio():
    return contentType(CONTENT_TYPE['AUDIO'])

def contentVideo():
    return contentType(CONTENT_TYPE['VIDEO'])
