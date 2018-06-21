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


#####
class AcceptEncoding(TypeQ):
    def __init__(self,one,**kwargs):
        super(AcceptEncoding,self).__init__(one,**kwargs)
        self.header_type = "req"
        self.forbidden_header_name = False
    def directives(self):
        #kl = ["gzip","compress","deflate","br","identity","*"]
        #vl = ["LZ77","LZW","zlib_deflate","brotli","no compression","no preference"]
        #d = eded.kvlist2d(kl,vl)
        d = {
            'gzip': 'LZ77',
            'compress': 'LZW',
            'deflate': 'zlib_deflate',
            'br': 'brotli',
            'identity': 'no compression',
            '*': 'no preference'
        }
        pobj(d)

class AcceptLanguage(LanguageLocaleQ):
    def __init__(self,one,**kwargs):
        super(AcceptLanguage,self).__init__(one,**kwargs)
        self.header_type = "req"
        self.forbidden_header_name = False
        self.cros_safelisted_request_header = True



######
