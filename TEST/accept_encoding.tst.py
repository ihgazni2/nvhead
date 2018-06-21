s = '''deflate;q=0.2, gzip;q=1.0, *;q=0.5'''
accept_encoding = AcceptEncoding(s)
sarr = accept_encoding.sarr
pobj(sarr)
darr = accept_encoding.darr
pobj(darr)
accept_encoding.header_type
accept_encoding.forbidden_header_name
accept_encoding.directives()


accept_encoding.qsort()
accept_encoding.append('compress')
accept_encoding.append('br',0.7)
accept_encoding.rm_q(lambda ele:ele['q']>=0.5)
accept_encoding.rm_type("*")


