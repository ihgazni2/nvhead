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

class AcceptRange():
    def __init__(self,one,**kwargs):
        self.str = one
        self.header_type = "res"
        self.forbidden_header_name = False
    def directives(self):
        pobj(["none","bytes"])

class AccessControlAllowCredentials():
    def __init__(self,one,**kwargs):
        self.str = one
        self.header_type = "res"
        self.forbidden_header_name = False

class AccessControlAllowOrigin():
    def __init__(self,one,**kwargs):
        self.str = one
        self.header_type = "res"
        self.forbidden_header_name = False

class AccessControlMaxAge():
    def __init__(self,one,**kwargs):
        self.str = one
        self.header_type = "res"
        self.forbidden_header_name = False


class AccessControlAllowHeaders(Comma):
    def __init__(self,one,**kwargs):
        super(AccessControlAllowHeaders,self).__init__(one,**kwargs)
        self.header_type = "res"
        self.forbidden_header_name = False


class AccessControlAllowMethods(Comma):
    def __init__(self,one,**kwargs):
        super(AccessControlAllowMethods,self).__init__(one,**kwargs)
        self.header_type = "res"
        self.forbidden_header_name = False
    def directives(self):
        pobj(["GET","HEAD","POST","PUT","DELETE","CONNECT","OPTIONS","TRACE","PATCH"])

class AccessControlExposeHeaders(Comma):
    def __init__(self,one,**kwargs):
        super(AccessControlExposeHeaders,self).__init__(one,**kwargs)
        self.header_type = "res"
        self.forbidden_header_name = False
    def directives(self):
        print("by default the below six are exposed")
        pobj(["Cache-Control","Content-Language","Content-Type","Expires","Last-Modified","Pragma"])


class AccessControlRequestHeaders(Comma):
    def __init__(self,one,**kwargs):
        super(AccessControlRequestHeaders,self).__init__(one,**kwargs)
        self.header_type = "req"
        self.forbidden_header_name = True


class AccessControlRequestMethod():
    def __init__(self,one,**kwargs):
        self.str = one
        self.header_type = "req"
        self.forbidden_header_name = True
    def directives(self):
        print("one of the below http method")
        pobj(["GET","HEAD","POST","PUT","DELETE","CONNECT","OPTIONS","TRACE","PATCH"])


######################


class Age():
    def __init__(self,one,**kwargs):
        self.str = one
        self.header_type = "res"
        self.forbidden_header_name = False


# Entity headers are used in both, HTTP requests and responses.

class Allow(Comma):
    def __init__(self,one,**kwargs):
        super(Allow,self).__init__(one,**kwargs)
        self.header_type = "entity"
        self.forbidden_header_name = False
    def directives(self):
        pobj(["GET","HEAD","POST","PUT","DELETE","CONNECT","OPTIONS","TRACE","PATCH"])

#  Alt-Svc: h2=":443"; ma=3600



class Authorization():
    def __init__(self,one,**kwargs):
        self.str = one
        self.str = eses.replace(self.str,re.compile('[\x20]+'),"\x20")
        self.header_type = "req"
        self.forbidden_header_name = False
        self.type,self.credentials = self.str.split('\x20')

# Cache-Control: no-cache, no-store, must-revalidate

class CacheControl(Comma):
    def __init__(self,one,**kwargs):
        super(CacheControl,self).__init__(one,**kwargs)
        self.header_type = "general"
        self.forbidden_header_name = False
        self.cros_safelisted_request_header = True
        self.for_req = ["max-age","max-stale","min-fresh","no-cache","no-store","no-transform","only-if-cached"]
        self.for_res = ["must-revalidate","no-cache","no-store","no-transform","public","private","proxy-revalidate","max-age","s-maxage"]
        self.extensions = ["immutable","stale-while-revalidate","stale-if-error"]
        self.expirations = ["max-age","s-maxage","max-stale","min-fresh","stale-while-revalidate","stale-if-error"]
        self.revalidations = ["must-revalidate","proxy-revalidate","immutable"]
        self.reloadings = ["must-revalidate","proxy-revalidate","immutable"]
        self.others = ["no-store","no-transform"]
    def directives(self,cond):
        if(cond == 'req'):
            pobj(["max-age=<seconds>","max-stale[=<seconds>]","min-fresh=<seconds>","no-cache","no-store","no-transform","only-if-cached"])
        elif(cond == 'res'):
            pobj(["must-revalidate","no-cache","no-store","no-transform","public","private","proxy-revalidate","max-age=<seconds>","s-maxage=<seconds>"])
        elif(cond == 'ext'):
            pobj(["immutable","stale-while-revalidate=<seconds>","stale-if-error=<seconds>"])
        elif(cond == 'cacheability'):
            pobj(["public","private","no-cache","only-if-cached"])
        elif(cond == 'expiration'):
            pobj(["max-age=<seconds>","s-maxage=<seconds>","max-stale[=<seconds>]","min-fresh=<seconds>","stale-while-revalidate=<seconds>","stale-if-error=<seconds>"])
        elif(cond == 'revalidation'):
            pobj(["must-revalidate","proxy-revalidate","immutable"])
        elif(cond == 'other'):
            pobj(["no-store","no-transform"])
        else:
            pass

#Clear-Site-Data: "cache", "cookies", "storage", "executionContexts"

class ClearSiteData(Comma):
    def __init__(self,one,**kwargs):
        super(ClearSiteData,self).__init__(one,**kwargs)
        self.header_type = "res"
        self.forbidden_header_name = False
    def directives(self):
        pobj(["cache","cookies","storage","executionContexts","*"])
#@@@@@@@@@@@@@@@@@@@@
