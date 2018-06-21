from nvhead.consts import *
from nvhead.common import *


class Accept(TypeSubtypeQ):
    def __init__(self,one,**kwargs):
        super(Accept,self).__init__(one,**kwargs)
        self.header_type = "req"
        self.forbidden_header_name = False
        self.cros_safelisted_request_header = True


class AcceptCharset(TypeQ):
    def __init__(self,one,**kwargs):
        super(AcceptCharset,self).__init__(one,**kwargs)
        self.header_type = "req"
        self.forbidden_header_name = False



