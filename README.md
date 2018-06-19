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
├──7. [prepend\<0\>](nvhead/Images/Head.prepend.0.png)  <br>
├──7. [prepend\<1\>](nvhead/Images/Head.prepend.1.png)  <br>
├──8. [insert](nvhead/Images/Head.insert.0.png)  <br>
├──9. [uniqualize](nvhead/Images/Head.uniqualize.0.png)  <br>
├──10. [uniqualize_all](nvhead/Images/Head.uniqualize_all.0.png)  <br>
├──11. [getitem\<0\>](nvhead/Images/Head.get.0.png)  <br>
├──11. [getattr\<1\>](nvhead/Images/Head.get.1.png)  <br>
├──12. [delitem\<0\>](nvhead/Images/Head.delitem.0.png)  <br>
├──12. [delitem\<1\>](nvhead/Images/Head.delitem.1.png)  <br>
├──13. [setitem\<0\>](nvhead/Images/Head.setitem.0.png)  <br>
├──13. [setitem\<1\>](nvhead/Images/Head.setitem.1.png)  <br>
├──14. [setattr\<0\>](nvhead/Images/Head.setattr.0.png)  <br>
├──14. [setattr\<1\>](nvhead/Images/Head.setattr.1.png)  <br>
├──15. [delattr](nvhead/Images/Head.delattr.0.png)  <br>
-------------------------------------------------------------------------


#SPECIFIC HEADERS (In Progressing...) 
--------------------------------------------------------------------------
├──0. [www_authenticate](nvhead/Images/www_authenticate.0.png)  <br>
├──1. [authorization](nvhead/Images/authorization.0.png)  <br>
├──2. [proxy_authenticate](nvhead/Images/proxy_authenticate.0.png)  <br>
├──3. [proxy_authorization](nvhead/Images/proxy_authorization.0.png)  <br>
├──4. [age](nvhead/Images/age.0.png)  <br>
├──5. [cache_control](nvhead/Images/cache_control.0.png)  <br>
├──6. [expires](nvhead/Images/expires.0.png)  <br>
├──7. [pragma](nvhead/Images/pragma.0.png)  <br>
├──8. [warning](nvhead/Images/warning.0.png)  <br>
├──9. [accept_ch](nvhead/Images/accept_ch.0.png)  <br>
├──10. [accept_ch_lifetime](nvhead/Images/accept_ch_lifetime.0.png)  <br>
├──11. [early_data](nvhead/Images/early_data.0.png)  <br>
├──12. [content_dpr](nvhead/Images/content_dpr.0.png)  <br>
├──13. [dpr](nvhead/Images/dpr.0.png)  <br>
├──14. [downlink](nvhead/Images/downlink.0.png)  <br>
├──15. [save_data](nvhead/Images/save_data.0.png)  <br>
├──16. [viewport_width](nvhead/Images/viewport_width.0.png)  <br>
├──17. [width](nvhead/Images/width.0.png)  <br>
├──18. [last_modified](nvhead/Images/last_modified.0.png)  <br>
├──19. [etag](nvhead/Images/etag.0.png)  <br>
├──20. [if_match](nvhead/Images/if_match.0.png)  <br>
├──21. [if_none_match](nvhead/Images/if_none_match.0.png)  <br>
├──22. [if_modified_since](nvhead/Images/if_modified_since.0.png)  <br>
├──23. [if_unmodified_since](nvhead/Images/if_unmodified_since.0.png)  <br>
├──24. [connection](nvhead/Images/connection.0.png)  <br>
├──25. [keep_alive](nvhead/Images/keep_alive.0.png)  <br>
├──26. [accept](nvhead/Images/accept.0.png)  <br>
├──27. [accept_charset](nvhead/Images/accept_charset.0.png)  <br>
├──28. [accept_encoding](nvhead/Images/accept_encoding.0.png)  <br>
├──29. [accept_language](nvhead/Images/accept_language.0.png)  <br>
├──30. [expect](nvhead/Images/expect.0.png)  <br>
├──31. [max_forwards](nvhead/Images/max_forwards.0.png)  <br>
├──32. [cookie](nvhead/Images/cookie.0.png)  <br>
├──33. [set_cookie](nvhead/Images/set_cookie.0.png)  <br>
├──34. [cookie2](nvhead/Images/cookie2.0.png)  <br>
├──35. [set_cookie2](nvhead/Images/set_cookie2.0.png)  <br>
├──36. [access_control_allow_origin](nvhead/Images/access_control_allow_origin.0.png)  <br>
├──37. [access_control_allow_credentials](nvhead/Images/access_control_allow_credentials.0.png)  <br>
├──38. [access_control_allow_headers](nvhead/Images/access_control_allow_headers.0.png)  <br>
├──39. [access_control_allow_methods](nvhead/Images/access_control_allow_methods.0.png)  <br>
├──40. [access_control_expose_headers](nvhead/Images/access_control_expose_headers.0.png)  <br>
├──41. [access_control_max_age](nvhead/Images/access_control_max_age.0.png)  <br>
├──42. [access_control_request_headers](nvhead/Images/access_control_request_headers.0.png)  <br>
├──43. [access_control_request_method](nvhead/Images/access_control_request_method.0.png)  <br>
├──44. [origin](nvhead/Images/origin.0.png)  <br>
├──45. [timing_allow_origin](nvhead/Images/timing_allow_origin.0.png)  <br>
├──46. [dnt](nvhead/Images/dnt.0.png)  <br>
├──47. [tk](nvhead/Images/tk.0.png)  <br>
├──48. [content_disposition](nvhead/Images/content_disposition.0.png)  <br>
├──49. [content_length](nvhead/Images/content_length.0.png)  <br>
├──50. [content_type](nvhead/Images/content_type.0.png)  <br>
├──51. [content_encoding](nvhead/Images/content_encoding.0.png)  <br>
├──52. [content_language](nvhead/Images/content_language.0.png)  <br>
├──53. [content_location](nvhead/Images/content_location.0.png)  <br>
├──54. [forwarded](nvhead/Images/forwarded.0.png)  <br>
├──55. [x_forwarded_for](nvhead/Images/x_forwarded_for.0.png)  <br>
├──56. [x_forwarded_host](nvhead/Images/x_forwarded_host.0.png)  <br>
├──57. [x_forwarded_proto](nvhead/Images/x_forwarded_proto.0.png)  <br>
├──58. [via](nvhead/Images/via.0.png)  <br>
├──59. [location](nvhead/Images/location.0.png)  <br>
├──60. [from](nvhead/Images/from.0.png)  <br>
├──61. [host](nvhead/Images/host.0.png)  <br>
├──62. [referer](nvhead/Images/referer.0.png)  <br>
├──63. [referrer_policy](nvhead/Images/referrer_policy.0.png)  <br>
├──64. [user_agent](nvhead/Images/user_agent.0.png)  <br>
├──65. [allow](nvhead/Images/allow.0.png)  <br>
├──66. [server](nvhead/Images/server.0.png)  <br>
├──67. [accept_ranges](nvhead/Images/accept_ranges.0.png)  <br>
├──68. [range](nvhead/Images/range.0.png)  <br>
├──69. [if_range](nvhead/Images/if_range.0.png)  <br>
├──70. [content_range](nvhead/Images/content_range.0.png)  <br>
├──71. [content_security_policy](nvhead/Images/content_security_policy.0.png)  <br>
├──72. [content_security_policy_report_only](nvhead/Images/content_security_policy_report_only.0.png)  <br>
├──73. [expect_ct](nvhead/Images/expect_ct.0.png)  <br>
├──74. [public_key_pins](nvhead/Images/public_key_pins.0.png)  <br>
├──75. [public_key_pins_report_only](nvhead/Images/public_key_pins_report_only.0.png)  <br>
├──76. [strict_transport_security](nvhead/Images/strict_transport_security.0.png)  <br>
├──77. [upgrade_insecure_requests](nvhead/Images/upgrade_insecure_requests.0.png)  <br>
├──78. [x_content_type_options](nvhead/Images/x_content_type_options.0.png)  <br>
├──79. [x_download_options](nvhead/Images/x_download_options.0.png)  <br>
├──80. [x_frame_options](nvhead/Images/x_frame_options.0.png)  <br>
├──81. [x_permitted_cross_domain_policies](nvhead/Images/x_permitted_cross_domain_policies.0.png)  <br>
├──82. [x_powered_by](nvhead/Images/x_powered_by.0.png)  <br>
├──83. [x_xss_protection](nvhead/Images/x_xss_protection.0.png)  <br>
├──84. [ping_from](nvhead/Images/ping_from.0.png)  <br>
├──85. [ping_to](nvhead/Images/ping_to.0.png)  <br>
├──86. [last_event_id](nvhead/Images/last_event_id.0.png)  <br>
├──87. [transfer_encoding](nvhead/Images/transfer_encoding.0.png)  <br>
├──88. [te](nvhead/Images/te.0.png)  <br>
├──89. [trailer](nvhead/Images/trailer.0.png)  <br>
├──90. [sec_websocket_key](nvhead/Images/sec_websocket_key.0.png)  <br>
├──91. [sec_websocket_extensions](nvhead/Images/sec_websocket_extensions.0.png)  <br>
├──92. [sec_websocket_accept](nvhead/Images/sec_websocket_accept.0.png)  <br>
├──93. [sec_websocket_protocol](nvhead/Images/sec_websocket_protocol.0.png)  <br>
├──94. [sec_websocket_version](nvhead/Images/sec_websocket_version.0.png)  <br>
├──95. [date](nvhead/Images/date.0.png)  <br>
├──96. [expect_ct](nvhead/Images/expect_ct.0.png)  <br>
├──97. [large_allocation](nvhead/Images/large_allocation.0.png)  <br>
├──98. [link](nvhead/Images/link.0.png)  <br>
├──99. [retry_after](nvhead/Images/retry_after.0.png)  <br>
├──100. [server_timing](nvhead/Images/server_timing.0.png)  <br>
├──101. [sourcemap](nvhead/Images/sourcemap.0.png)  <br>
├──102. [upgrade](nvhead/Images/upgrade.0.png)  <br>
├──103. [vary](nvhead/Images/vary.0.png)  <br>
├──104. [x_dns_prefetch_control](nvhead/Images/x_dns_prefetch_control.0.png)  <br>
├──105. [x_firefox_spdy](nvhead/Images/x_firefox_spdy.0.png)  <br>
├──106. [x_requested_with](nvhead/Images/x_requested_with.0.png)  <br>
├──107. [x_robots_tag](nvhead/Images/x_robots_tag.0.png)  <br>
├──108. [x_ua_compatible](nvhead/Images/x_ua_compatible.0.png)  <br>  

--------------------------------------------------------------------------
