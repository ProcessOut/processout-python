try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import processout

from processout.networking.request  import Request
from processout.networking.response import Response

# The content of this file was automatically generated

class GatewayConfiguration(object):
    def __init__(self, client, prefill = None):
        self._client = client

        self._id = None
        self._project = None
        self._gateway = None
        self._enabled = None
        self._publicKeys = None
        if prefill != None:
            self.fillWithData(prefill)

    
    @property
    def id(self):
        """Get id"""
        return self._id

    @id.setter
    def id(self, val):
        """Set id
        Keyword argument:
        val -- New id value"""
        self._id = val
        return self
    
    @property
    def project(self):
        """Get project"""
        return self._project

    @project.setter
    def project(self, val):
        """Set project
        Keyword argument:
        val -- New project value"""
        if isinstance(val, dict):
            obj = processout.Project(self._client)
            obj.fillWithData(val)
            self._project = obj
        else:
            self._project = val
        return self
    
    @property
    def gateway(self):
        """Get gateway"""
        return self._gateway

    @gateway.setter
    def gateway(self, val):
        """Set gateway
        Keyword argument:
        val -- New gateway value"""
        if isinstance(val, dict):
            obj = processout.Gateway(self._client)
            obj.fillWithData(val)
            self._gateway = obj
        else:
            self._gateway = val
        return self
    
    @property
    def enabled(self):
        """Get enabled"""
        return self._enabled

    @enabled.setter
    def enabled(self, val):
        """Set enabled
        Keyword argument:
        val -- New enabled value"""
        self._enabled = val
        return self
    
    @property
    def publicKeys(self):
        """Get publicKeys"""
        return self._publicKeys

    @publicKeys.setter
    def publicKeys(self, val):
        """Set publicKeys
        Keyword argument:
        val -- New publicKeys value"""
        self._publicKeys = val
        return self
    

    def fillWithData(self, data):
        """Fill the current object with the new values pulled from data
        Keyword argument:
        data -- The data from which to pull the new values"""
        if "id" in data.keys():
            self.id = data["id"]
        if "project" in data.keys():
            self.project = data["project"]
        if "gateway" in data.keys():
            self.gateway = data["gateway"]
        if "enabled" in data.keys():
            self.enabled = data["enabled"]
        if "public_keys" in data.keys():
            self.publicKeys = data["public_keys"]
        
        return self

    
