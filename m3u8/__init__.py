from urllib2 import urlopen

from m3u8.model import M3U8
from m3u8.parser import parse

__all__ = 'M3U8', 'loads', 'load', 'parse'

def loads(content):
    '''
    Given a string with a m3u8 content, returns a M3U8 object.
    Raises ValueError if invalid content
    '''
    return M3U8(content)

def load(uri):
    '''
    Retrieves the content from a given URI and returns a M3U8 object.
    Raises ValueError if invalid content or IOError if request fails.
    '''
    if uri.startswith('http://') or uri.startswith('https://'):
        content = urlopen(uri).read().strip()
    else:
        with open(uri) as fileobj:
            content = fileobj.read().strip()

    return M3U8(content)
