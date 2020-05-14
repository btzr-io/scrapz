from typing import Final

#--------------- #
#  Content Type  #
# -------------- #

# Hardcoded content type
# TODO: Add addition media types ( images, documents, etc..)

CONTENT_TYPE: Final = {
    'AUDIO': 'audio',
    'VIDEO': 'video'
}

# ------------- #
#  Claim Type   #
# ------------- #

CLAIM_TYPE = {
    'STREAM': 'stream',
    'CHANNEL': 'channel',
    'CLAIM_LIST': 'claimList',
    'CLAIM_REPOST': 'claimreference',
}

# ------------- #
#  Tables name  #
# ------------- #

TABLE_NAME: Final = {
    'TAG': 'tag',
    'CLAIM': 'claim',
}

#------- #
#  Tags  #
# ------ #

# Hardcoded tags for initial discover
# TODO: Analyze related tags used

TAG_ID: Final = {
    'MUSIC': [19],
    'MATURE': [1],
    'PODCAST':  [1847, 1717, 2900186],
    'AUDIO_BOOK': [1061, 274079, 14579]
}
