Django all page login
=====================

Django middleware that requires login for whole site. 

How to use
==========

1. Install this module. 
2. Add follwing to ``MIDDLEWARE`` setting
   **after** ``AuthenticationMiddleware``: ``all_page_login.middleware.LoginRequiredMiddleware``
   Your middleware should look like that: 
   
        MIDDLEWARE = [
            # Anything
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            # Anything
            'all_page_login.middleware.LoginRequiredMiddleware'
            # Anything
        ]
        
3. If you want to make some urls exempt from this middleware
   use: ``LOGIN_EXEMPT_URLS``, each one is a **regular expression**, 
   of url will match this regexp users that are not logged in 
   will be able to view it.  
   
This work is adapted from: http://onecreativeblog.com/post/59051248/django-login-required-middleware
original work is licensed under CC-SA 3.0 US license, which we re-license under MIT.
