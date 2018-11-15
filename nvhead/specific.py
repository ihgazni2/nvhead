from nvhead.consts import *
from nvhead.common import *
from xdict.jprint import pobj
import estring.estring as eses
import re

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

class AltSvc(SemiColon):
    def __init__(self,one,**kwargs):
        super(AltSvc,self).__init__(one,**kwargs)


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


#

class Connection():
    def __init__(self,one,**kwargs):
        self.str = one
        self.header_type = "general"
        self.forbidden_header_name = True
    @classmethod
    def is_close(cls,s):
        cond = (s.lower() == 'close')
        return(cond)
    @classmethod
    def is_keepalive(cls,s):
        cond = (s.lower() == 'keepalive')
        return(cond)

#

#https://aiohttp.readthedocs.io/en/stable/multipart.html

class ContentDisposition(SemiColon):
    def __init__(self,one,body_part,**kwargs):
        super(ContentDisposition,self).__init__(one,**kwargs)
        self.body_part = body_part
        if(self.body_part == "main"):
            self.header_type = "res"
        elif(self.body_part == "subpart"):
            self.header_type = "general"
        self.forbidden_header_name = False
        self.types = {'main':["inline","attachment"],"subpart":["form-data"]}


class ContentEncoding(Comma):
    def __init__(self,one,**kwargs):
        super(ContentEncoding,self).__init__(one,**kwargs)
        self.header_type = "entity"
        self.forbidden_header_name = False
    def directives(self):
        pobj(["gzip","compress","deflate","identity","br"])


class ContentLanguage(Comma):
    def __init__(self,one,**kwargs):
        super(ContentLanguage,self).__init__(one,**kwargs)
        self.header_type = "entity"
        self.forbidden_header_name = False
        self.cros_safelisted_request_header = True
        self.cros_safelisted_res_header = True
    def directives(self):
        pobj(["gzip","compress","deflate","identity","br"])

class ContentLength():
    def __init__(self,one,**kwargs):
        self.str = one
        self.header_type = "entity"
        self.forbidden_header_name = True
    def directives(self):
        print("The length in decimal number of octets")


class ContentLocation():
    def __init__(self,one,**kwargs):
        self.str = one
        self.header_type = "entity"
        self.forbidden_header_name = False
    def directives(self):
        print("A relative (to the request URL) or absolute URL")

class ContentRange():
    def __init__(self,one,**kwargs):
        self.str = self.fmt(one)
        self.header_type = "entity"
        self.forbidden_header_name = False
        self.unit,self.start,self.end,self.size = self.decode(self.str,mode='tuple')
    def fmt(self,one):
        one = eses.replace(one,re.compile('[\x20]+'),"\x20")
        one = abstract_fmt(one,c='-')
        return(one)
    @classmethod
    def asterisk(cls,s):
        if(s == None):
            return("*")
        else:
            return(s)
    @classmethod
    def decode(cls,one,**kwargs):
        if('mode' in kwargs):
            mode = kwargs['mode']
        else:
            mode = 'dict'
        unit,others = one.split("\x20")
        ranges,size = others.split("/")
        start,end = ranges.split("-")
        if(mode == "tuple"):
            rslt = (try_int(unit),try_int(start),try_int(end),try_int(size))
        else:
            rslt = {"unit":try_int(unit),"start":try_int(start),"end":try_int(end),"size":try_int(size)}
        return(rslt)
    @classmethod
    def encode(cls,d):
        cond = isinstance(d,dict)
        if(cond):
            unit = asterisk(d['unit'])
            start = asterisk(d['start'])
            end = asterisk(d['end'])
            size = asterisk(d['size'])
        else:
            unit,start,end,size = d
        unit = try_int(unit)
        start = try_int(start)
        end = try_int(end)
        size = try_int(size)
        one = unit + "\x20" + start+"-"+ end + '/' + size
        return(one)

#######


