# Django-Middleware

## Overview

This is just a collection of middleware I have created for various projects that I wanted all in
one place that I can easily update and also share with the Django community.

## Installation

If you clone this project in your project application add the following to your MIDDLEWARE_CLASSES

### IPhone

Add the following to the tuple

    django-middleware.iphone.iPhoneMiddleware

### AllowedIPs

Add the following to the tuple

    django-middleware.allowedips.AllowedIPS


## Usage

### iPhoneMiddleware

Once the middleware is installed any app that has the UserAgent of iPhone or iPod the middleware will pick up and check a new template location.

If your TEMPLATE_DIRS is set to something like project_root/templates, the middleware will check in project_root/templates/iphone and failback to project_root/templates

So if you have the following

    return render_to_response('index/index.html')

A normal client will look in project_root/templates/index/index.html. If your iPhone loads the page it will look in project_root/templates/iphone/index/index.html and will failback to the normal template location if it can't find the iPhone template. 

### AllowedIPS

This is middleware to protect the whole site from all IPs but the ones that are whitelisted. So once the middleware is installed you just need to add the following to your settings.py

    ALLOWED_IPS = (
        ('127.0.0.1'),
        ('192.168.71'),
    )

So it can handle a single IP or a class of IPs
