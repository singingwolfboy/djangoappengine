from django.core.cache.backends.memcached import BaseMemcachedCache
from google.appengine.api import memcache

class GAEMemcachedCache(BaseMemcachedCache):
    """
    An implementation of a cache binding using Google's memcache-alike library
    bundled with the App Engine SDK.
    """
    def __init__(self, server, params):
        super(GAEMemcachedCache, self).__init__(server, params,
                                                library=memcache,
                                                value_not_found_exception=ValueError)
