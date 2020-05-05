'''
'''

from ...constants import *

CHARS_ID           = '-a-zA-Z0-9_'
CHARS_PARAM        = f'{CHARS_ID}%'
CHARS_CONTINUATION = CHARS_PARAM

# Prefixes
PREFIX_ALBUM_ID          = 'MPREb_'
PREFIX_ALBUM_PLAYLIST_ID = 'OLAK5uy_'
PREFIX_ALBUM_RADIO_ID    = 'RDAMPL'
PREFIX_ARTIST_ID         = 'UC'
PREFIX_ARTIST_RADIO_ID   = 'RDEM'
PREFIX_ARTIST_SHUFFLE_ID = 'RDAO'

# Lengths
LEN_ALBUM_ID          = 17
LEN_ALBUM_PLAYLIST_ID = 41
LEN_ARTIST_ID         = 24

# Entropy Lengths
LEN_ENTROPY_ALBUM_ID          = LEN_ALBUM_ID          - len(PREFIX_ALBUM_ID)
LEN_ENTROPY_ALBUM_PLAYLIST_ID = LEN_ALBUM_PLAYLIST_ID - len(PREFIX_ALBUM_PLAYLIST_ID)
LEN_ENTROPY_ARTIST_ID         = LEN_ARTIST_ID         - len(PREFIX_ARTIST_ID)
