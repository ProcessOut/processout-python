try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout

from processout.networking.request  import Request
from processout.networking.response import Response

# The content of this file was automatically generated

class CustomerAction(object):
    def __init__(self, client, prefill = None):
        self._client = client

        self._type = ""
        self._value = ""
        if prefill != None:
            self.fillWithData(prefill)

    
    @property
    def type(self):
        """Get type"""
        return self._type

    @type.setter
    def type(self, val):
        """Set type
        Keyword argument:
        val -- New type value"""
        self._type = val
        return self
    
    @property
    def value(self):
        """Get value"""
        return self._value

    @value.setter
    def value(self, val):
        """Set value
        Keyword argument:
        val -- New value value"""
        self._value = val
        return self
    

    def fillWithData(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "type" in data.keys():
            self.type = data["type"]
        if "value" in data.keys():
            self.value = data["value"]
        
        return self

    
