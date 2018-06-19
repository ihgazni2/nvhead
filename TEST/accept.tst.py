
#cls Accept
#Accept = TypeSubtypeQ

#accept.0.png
s ="text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8"
accept = Accept(s)
accept
s = accept.str()
pobj(accept.darr)

#accept.1.png
accept.rm_not_type('application')
accept
accept.rm_subtype("xhtml+xml")
accept

#accept.2.png
s ="application/xhtml+xml;q=0.7, application/xml;q=0.9, */*;q=0.8, text/html"
accept = Accept(s)
accept
accept.append("application","json",0.5)
accept


accept.qsort()


###########################
#accept.3.png
accept
accept.rm_q(lambda ele:ele['q']<0.9)




