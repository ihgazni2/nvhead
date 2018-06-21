

#cls AcceptCharset
#AcceptCharset = TypeSubtypeQ

#accept_charset.0.png
s = 'Accept-Charset: gb2312;q=0.3, utf-8, iso-8859-1;q=0.5, *;q=0.1'

accept_charset = AcceptCharset(s)
accept_charset

accept_charset.qsort()

pobj(accept_charset.darr)


#accept_charset.1.png
accept_charset
accept_charset.rm_type('*')
accept_charset
accept_charset
accept_charset.rm_q(lambda ele:ele['q']<0.4)
accept_charset.append("utf-8",0.8)




###########################






