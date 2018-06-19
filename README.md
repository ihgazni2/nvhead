# nvhead
>__http headers APIs__

# install
>__pip3 install nvhead__

# SUMMARY
-----------------------------------------------------------------------

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
![](nvhead/Images/Head.INTRODUCE.1.png)  <br>

    hd.
![](nvhead/Images/Head.INTRODUCE.0.png)  <br>

    hd.count
    hd.for_req
    hd.for_res
    
    hd.accept_encoding
    hd.x_oi_thumbprint
    hd.user_agent
    hd.authorization
    hd.content_length
    hd.content_type
    hd.connection
    hd.cache_control


-----------------------------------------------------------------------

_class Head_  
-------------------------------------------------------------------------
>├──0. [init with string](nvhead/Images/Head.init_with_string.0.png)  <br>
├──1. [init with dict\<0\>](nvhead/Images/Head.init_with_dict.0.png)  <br>
├──1. [init with dict\<1\>](nvhead/Images/Head.init_with_dict.1.png)  <br>
├──1. [init with dict\<2\>](nvhead/Images/Head.init_with_dict.0.png)  <br>
├──2. [init with tlist\<0\>](nvhead/Images/Head.init_with_tlist.0.png)  <br>
├──2. [init with tlist\<1\>](nvhead/Images/Head.init_with_tlist.1.png)  <br>
├──3. [init with res_head\<0\>](nvhead/Images/Head.init_with_res_head.0.png)  <br>
├──4. [append\<0\>](nvhead/Images/Head.append.0.png)  <br>
├──4. [append\<1\>](nvhead/Images/Head.append.1.png)  <br>
├──4. [append\<2\>](nvhead/Images/Head.append.2.png)  <br>
├──4. [append\<3\>](nvhead/Images/Head.append.3.png)  <br>
├──5. [remove\<0\>](nvhead/Images/Head.remove.0.png)  <br>
├──5. [remove\<1\>](nvhead/Images/Head.remove.1.png)  <br>
├──6. [remove_all](nvhead/Images/Head.remove_all.0.png)  <br>

-------------------------------------------------------------------------



