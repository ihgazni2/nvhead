from xdict.jprint import pobj
from xdict.jprint import pdir
import requests
from navegador5 import head as nvhead
from navegador5 import body as nvbody
from navegador5 import solicitud as nvsoli
import elist.elist as elel
import tlist.tlist as tltl
import edict.edict as eded
import estring.estring as eses
import requests
import nvhead.head as nvhd

##############Introduce ####################
from xdict.jprint import pobj
from xdict.jprint import pdir
import nvhead.head as nvhd

req_head_s = '''Accept-Encoding: gzip, deflate
X-OI-Thumbprint: 154cda3ef3299e031f660850b40db1d30b53aec9
User-Agent: SmartScreen/2814750890000385
Authorization: SmartScreenHash eyJhdXRoSWQiOiJhZGZmZjVhZC1lZjllLTQzYTYtYjFhMy0yYWQ0MjY3YWVlZDUiLCJoYXNoIjoielAyTmlkZDkwLzg9Iiwia2V5IjoiUXJBL3lSRHJUNCs0Y2FZRkU2T0NyQT09In0=
Content-Length: 1871
Content-Type: application/json; charset=utf-8
Connection: Keep-Alive
Cache-Control: no-cache'''

hd =nvhd.Head(req_head_s)
hd

hd.

#Head.INTRODUCE.0.png

hd.count

hd.accept_encoding
hd.x_oi_thumbprint
hd.user_agent
hd.authorization
hd.content_length
hd.content_type
hd.connection
hd.cache_control

hd.for_req






#################################



#1. __init__  init with string
#Head.init_with_string.0.png
req_head_s = '''Accept-Encoding: gzip, deflate
X-OI-Thumbprint: 154cda3ef3299e031f660850b40db1d30b53aec9
User-Agent: SmartScreen/2814750890000385
Authorization: SmartScreenHash eyJhdXRoSWQiOiJhZGZmZjVhZC1lZjllLTQzYTYtYjFhMy0yYWQ0MjY3YWVlZDUiLCJoYXNoIjoielAyTmlkZDkwLzg9Iiwia2V5IjoiUXJBL3lSRHJUNCs0Y2FZRkU2T0NyQT09In0=
Content-Length: 1871
Content-Type: application/json; charset=utf-8
Connection: Keep-Alive
Cache-Control: no-cache'''

hd =nvhd.Head(req_head_s)
hd


#2. __init__  init with dict

# Head.init_with_dict.0.png
req_head_d = {
 'Accept-Encoding': 'gzip, deflate',
 'X-OI-Thumbprint': '154cda3ef3299e031f660850b40db1d30b53aec9',
 'User-Agent': 'SmartScreen/2814750890000385',
 'Authorization': 'SmartScreenHash eyJhdXRoSWQiOiJhZGZmZjVhZC1lZjllLTQzYTYtYjFhMy0yYWQ0MjY3YWVlZDUiLCJoYXNoIjoielAyTmlkZDkwLzg9Iiwia2V5IjoiUXJBL3lSRHJUNCs0Y2FZRkU2T0NyQT09In0=',
 'Content-Length': '1871',
 'Content-Type': 'application/json; charset=utf-8',
 'Connection': 'Keep-Alive',
 'Cache-Control': 'no-cache'
}

hd =nvhd.Head(req_head_d)
hd

# Head.init_with_dict.1.png
sarr = hd.sarr()
s = hd.str()

# Head.init_with_dict.2.png
tl = hd.tlist()


#3. __init__  init with tlist
# Head.init_with_tlist.0.png
req_head_tl = [
 (
  'Accept-Encoding',
  'gzip, deflate'
 ),
 (
  'X-OI-Thumbprint',
  '154cda3ef3299e031f660850b40db1d30b53aec9'
 ),
 (
  'User-Agent',
  'SmartScreen/2814750890000385'
 ),
 (
  'Authorization',
  'SmartScreenHash eyJhdXRoSWQiOiJhZGZmZjVhZC1lZjllLTQzYTYtYjFhMy0yYWQ0MjY3YWVlZDUiLCJoYXNoIjoielAyTmlkZDkwLzg9Iiwia2V5IjoiUXJBL3lSRHJUNCs0Y2FZRkU2T0NyQT09In0='
 ),
 (
  'Content-Length',
  '1871'
 ),
 (
  'Content-Type',
  'application/json; charset=utf-8'
 ),
 (
  'Connection',
  'Keep-Alive'
 ),
 (
  'Cache-Control',
  'no-cache'
 )
]
# Head.init_with_tlist.1.png

hd = nvhd.Head(req_head_tl)
hd

#4 . init with resp head 
# Head.init_with_resp_head.0.png

res_head_s='''Server: Apache-Coyote/1.1
Cache-Control: no-store, private
Pragma: no-cache
Location: https://dc.ads.linkedin.com/collect/?pid=6883&s=1&url=https%3A%2F%2Fwww.blizzard.com%2Fzh-tw%2F&pageUrl=https%3A%2F%2Fwww.blizzard.com%2Fzh-tw%2F&ref=&cookiesTest=true&opid=87751&fmt=js&time=1529252650904
Content-Language: en-US
Vary: Accept-Encoding
Date: Sun, 17 Jun 2018 16:24:13 GMT
X-FS-UUID: 6e69c6a12fff38154052ca49162b0000
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Content-Security-Policy: default-src *; connect-src 'self' static.licdn.com media.licdn.com static-exp1.licdn.com static-exp2.licdn.com media-exp1.licdn.com media-exp2.licdn.com https://media-src.linkedin.com/media/ wss://*.linkedin.com; img-src data: blob: *; font-src data: *; style-src 'unsafe-inline' 'self' static-src.linkedin.com *.licdn.com; script-src 'report-sample' 'unsafe-inline' 'unsafe-eval' 'self' platform.linkedin.com spdy.linkedin.com static-src.linkedin.com *.ads.linkedin.com *.licdn.com; object-src 'none'; media-src blob: *; frame-ancestors http://*.adnxs.com https://*.adnxs.com http://*.linkedin.com https://*.linkedin.com http://*.slideshare.net https://*.slideshare.net https://*.msn.com http://*.msn.com http://*.outlook.com https://*.outlook.com translate.googleusercontent.com pemberly.www.linkedin.com:4443; report-uri https://www.linkedin.com/lite/contentsecurity?f=ad
X-Li-Fabric: prod-lsg1
Set-Cookie: bcookie="v=2&8daa83b0-075e-4a15-8d92-fb074bcd7f8f"; domain=.linkedin.com; Path=/; Expires=Wed, 17-Jun-2020 04:01:45 GMT
Set-Cookie: bscookie="v=1&20180617162413fbe7b854-d7bf-4ed7-8471-bb1294285ac8AQEOHnEH1lP0cXl9AhPpkrqCJZUDEz2I"; domain=.www.linkedin.com; Path=/; Secure; Expires=Wed, 17-Jun-2020 04:01:45 GMT; HttpOnly
Connection: keep-alive
X-Li-Pop: prod-ela1
X-LI-Proto: http/1.1
X-LI-UUID: bmnGoS//OBVAUspJFisAAA==
Content-Length: 0'''

hd = nvhd.Head(res_head_s,for_res=True)
hd
#head of http response could have duplicate head name, such as Set-Cookie
pobj(hd.set_cookie)

#2.





#3. append
#Head.append.0.png
req_head_s = '''Accept-Encoding: gzip, deflate
X-OI-Thumbprint: 154cda3ef3299e031f660850b40db1d30b53aec9
User-Agent: SmartScreen/2814750890000385
Authorization: SmartScreenHash eyJhdXRoSWQiOiJhZGZmZjVhZC1lZjllLTQzYTYtYjFhMy0yYWQ0MjY3YWVlZDUiLCJoYXNoIjoielAyTmlkZDkwLzg9Iiwia2V5IjoiUXJBL3lSRHJUNCs0Y2FZRkU2T0NyQT09In0=
Content-Length: 1871
Content-Type: application/json; charset=utf-8
Connection: Keep-Alive
Cache-Control: no-cache'''

hd =nvhd.Head(req_head_s)
hd

#Head.append.1.png
hd.append("Upgrade-Insecure-Requests",1)
sarr = hd.sarr()

hd.upgrade_insecure_requests
hd.append("Upgrade-Insecure-Requests",1)
hd

#Head.append.2.png
from xdict.jprint import pobj
from xdict.jprint import pdir
import nvhead.head as nvhd

res_head_s='''Server: Apache-Coyote/1.1
Cache-Control: no-store, private
Pragma: no-cache
Location: https://dc.ads.linkedin.com/collect/?pid=6883&s=1&url=https%3A%2F%2Fwww.blizzard.com%2Fzh-tw%2F&pageUrl=https%3A%2F%2Fwww.blizzard.com%2Fzh-tw%2F&ref=&cookiesTest=true&opid=87751&fmt=js&time=1529252650904
Content-Language: en-US
Vary: Accept-Encoding
Date: Sun, 17 Jun 2018 16:24:13 GMT
X-FS-UUID: 6e69c6a12fff38154052ca49162b0000
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Content-Security-Policy: default-src *; connect-src 'self' static.licdn.com media.licdn.com static-exp1.licdn.com static-exp2.licdn.com media-exp1.licdn.com media-exp2.licdn.com https://media-src.linkedin.com/media/ wss://*.linkedin.com; img-src data: blob: *; font-src data: *; style-src 'unsafe-inline' 'self' static-src.linkedin.com *.licdn.com; script-src 'report-sample' 'unsafe-inline' 'unsafe-eval' 'self' platform.linkedin.com spdy.linkedin.com static-src.linkedin.com *.ads.linkedin.com *.licdn.com; object-src 'none'; media-src blob: *; frame-ancestors http://*.adnxs.com https://*.adnxs.com http://*.linkedin.com https://*.linkedin.com http://*.slideshare.net https://*.slideshare.net https://*.msn.com http://*.msn.com http://*.outlook.com https://*.outlook.com translate.googleusercontent.com pemberly.www.linkedin.com:4443; report-uri https://www.linkedin.com/lite/contentsecurity?f=ad
X-Li-Fabric: prod-lsg1
Set-Cookie: bcookie="v=2&8daa83b0-075e-4a15-8d92-fb074bcd7f8f"; domain=.linkedin.com; Path=/; Expires=Wed, 17-Jun-2020 04:01:45 GMT
Set-Cookie: bscookie="v=1&20180617162413fbe7b854-d7bf-4ed7-8471-bb1294285ac8AQEOHnEH1lP0cXl9AhPpkrqCJZUDEz2I"; domain=.www.linkedin.com; Path=/; Secure; Expires=Wed, 17-Jun-2020 04:01:45 GMT; HttpOnly
Connection: keep-alive
X-Li-Pop: prod-ela1
X-LI-Proto: http/1.1
X-LI-UUID: bmnGoS//OBVAUspJFisAAA==
Content-Length: 0'''

hd = nvhd.Head(res_head_s,for_res=True)
hd

hd.for_res
pobj(hd.set_cookie)
hd.append('Set-Cookie','PageHistory=1')
pobj(hd.set_cookie)


#4. remove

from xdict.jprint import pobj
from xdict.jprint import pdir
import nvhead.head as nvhd

res_head_s='''Server: Apache-Coyote/1.1
Cache-Control: no-store, private
Pragma: no-cache
Location: https://dc.ads.linkedin.com/collect/?pid=6883&s=1&url=https%3A%2F%2Fwww.blizzard.com%2Fzh-tw%2F&pageUrl=https%3A%2F%2Fwww.blizzard.com%2Fzh-tw%2F&ref=&cookiesTest=true&opid=87751&fmt=js&time=1529252650904
Content-Language: en-US
Vary: Accept-Encoding
Date: Sun, 17 Jun 2018 16:24:13 GMT
X-FS-UUID: 6e69c6a12fff38154052ca49162b0000
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Content-Security-Policy: default-src *; connect-src 'self' static.licdn.com media.licdn.com static-exp1.licdn.com static-exp2.licdn.com media-exp1.licdn.com media-exp2.licdn.com https://media-src.linkedin.com/media/ wss://*.linkedin.com; img-src data: blob: *; font-src data: *; style-src 'unsafe-inline' 'self' static-src.linkedin.com *.licdn.com; script-src 'report-sample' 'unsafe-inline' 'unsafe-eval' 'self' platform.linkedin.com spdy.linkedin.com static-src.linkedin.com *.ads.linkedin.com *.licdn.com; object-src 'none'; media-src blob: *; frame-ancestors http://*.adnxs.com https://*.adnxs.com http://*.linkedin.com https://*.linkedin.com http://*.slideshare.net https://*.slideshare.net https://*.msn.com http://*.msn.com http://*.outlook.com https://*.outlook.com translate.googleusercontent.com pemberly.www.linkedin.com:4443; report-uri https://www.linkedin.com/lite/contentsecurity?f=ad
X-Li-Fabric: prod-lsg1
Set-Cookie: bcookie="v=2&8daa83b0-075e-4a15-8d92-fb074bcd7f8f"; domain=.linkedin.com; Path=/; Expires=Wed, 17-Jun-2020 04:01:45 GMT
Set-Cookie: bscookie="v=1&20180617162413fbe7b854-d7bf-4ed7-8471-bb1294285ac8AQEOHnEH1lP0cXl9AhPpkrqCJZUDEz2I"; domain=.www.linkedin.com; Path=/; Secure; Expires=Wed, 17-Jun-2020 04:01:45 GMT; HttpOnly
Connection: keep-alive
X-Li-Pop: prod-ela1
X-LI-Proto: http/1.1
X-LI-UUID: bmnGoS//OBVAUspJFisAAA==
Content-Length: 0'''

hd = nvhd.Head(res_head_s,for_res=True)
pobj(hd.set_cookie)
hd.remove("Set-Cookie",1)
print(hd.set_cookie)

hd = nvhd.Head(res_head_s,for_res=True)
pobj(hd.set_cookie)
hd.remove("Set-Cookie")
print(hd.set_cookie)
hd.remove("Set-Cookie")
print(hd.set_cookie)
hd['Set-Cookie']


hd = nvhd.Head(res_head_s,for_res=True)
pobj(hd.set_cookie)
hd.remove_all("Set-Cookie")
print(hd.set_cookie)
hd['Set-Cookie']

###################################################################################
#5. prepend


req_head_s = '''Accept-Encoding: gzip, deflate
X-OI-Thumbprint: 154cda3ef3299e031f660850b40db1d30b53aec9
User-Agent: SmartScreen/2814750890000385
Authorization: SmartScreenHash eyJhdXRoSWQiOiJhZGZmZjVhZC1lZjllLTQzYTYtYjFhMy0yYWQ0MjY3YWVlZDUiLCJoYXNoIjoielAyTmlkZDkwLzg9Iiwia2V5IjoiUXJBL3lSRHJUNCs0Y2FZRkU2T0NyQT09In0=
Content-Length: 1871
Content-Type: application/json; charset=utf-8
Connection: Keep-Alive
Cache-Control: no-cache'''
hd =nvhd.Head(req_head_s)
hd

sarr=hd.prepend("If-None-Match","5b261910-10372")
sarr = hd.sarr()
hd.if_none_match

hd.prepend("If-Modified-Since","Sun, 17 Jun 2018 08:17:20 GMT")
sarr = hd.sarr()
hd.if_modified_since



#6. insert
hd
hd.insert(8,"Referer","https://docs.python.org/3.7")
sarr = hd.sarr()
hd.referer



#7. uniqualize
hd.prepend("If-None-Match","5b261910-10372")
hd.prepend("If-None-Match","5b261910-10372",force=True)
hd.prepend("If-None-Match","5b261910-10372",force=True)
sarr= hd.sarr()

hd.uniqualize("If-None-Match")
sarr = hd.sarr()


#8. uniqualize_all
hd.prepend("If-None-Match","5b261910-10372")
hd.prepend("If-None-Match","5b261910-10372",force=True)
hd.prepend("If-None-Match","5b261910-10372",force=True)

hd.append("Upgrade-Insecure-Requests",1,force=True)
hd.append("Upgrade-Insecure-Requests",1,force=True)

sarr = hd.sarr()

hd.uniqualize_all()
sarr = hd.sarr()


# __getitem__
hd =Head(h)
hd.prepend("If-None-Match","1-1")
hd.prepend("If-None-Match","1-2",force=True)
hd.prepend("If-None-Match","1-3",force=True)

sarr = hd.sarr()
hd['If-None-Match']
hd['If-None-Match',0]
hd['If-None-Match',1]
hd['If-None-Match',2]

# __getattribute__
hd =Head(h)
hd.prepend("If-None-Match","1-1")
hd.prepend("If-None-Match","1-2",force=True)
hd.prepend("If-None-Match","1-3",force=True)
hd.if_none_match
hd.str()
hd.sarr()
#dict will lose some info
hd








# __setitem__
hd =Head(h)
hd.prepend("If-None-Match","1-1")
hd.prepend("If-None-Match","1-2",force=True)
hd.prepend("If-None-Match","1-3",force=True)

sarr = hd.sarr()
hd['If-None-Match'] = "1-5"
sarr = hd.sarr()
hd['If-None-Match',2] = "1-7"
sarr = hd.sarr()


hd['Referer'] = "https://docs.python.org/3.7"
hd.sarr()

# __delitem__
hd =Head(h)
hd.prepend("If-None-Match","1-1")
hd.prepend("If-None-Match","1-2",force=True)
hd.prepend("If-None-Match","1-3",force=True)

sarr = hd.sarr()
del hd['If-None-Match',1]
sarr = hd.sarr()
del hd['If-None-Match']
sarr = hd.sarr()






# __setattr__
hd =Head(h)
hd
hd.connection="close"
hd

# __delattr__
hd =Head(h)
del hd.x_oi_thumbprint
hd
hd.sarr()
