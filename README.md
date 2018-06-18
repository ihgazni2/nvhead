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
![](nvhead/Images/Head.INTRODUCE.0.png)  <br>

    hd.
![](nvhead/Images/Head.INTRODUCE.0.png)  <br>

-----------------------------------------------------------------------

#_class Head_
-----------------------------------------------------------------------
>├──0. [](nvhead/Images/.0.png)  <br>
