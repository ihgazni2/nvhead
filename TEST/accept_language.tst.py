s = '''en;q=0.8, de;q=0.7, fr-CH, fr;q=0.9, *;q=0.5'''
accept_language = AcceptLanguage(s)
pobj(accept_language.sarr)
pobj(accept_language.darr)


accept_language.header_type
accept_language.forbidden_header_name
accept_language.cros_safelisted_request_header
accept_language.qsort()
accept_language.rm_locale("CH")
accept_language.rm_language("*")
accept_language.rm_q(lambda ele:ele['q']>=0.8)
