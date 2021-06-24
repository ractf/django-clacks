# Django Clacks
The unseen, silent tribute to those we have lost.
<hr>

`django-clacks` contains boilerplate code for working with the nonstandard HTTP header `X-Clacks-Overhead` in Django apps.

You can find out more about the `X-Clacks-Overhead` header here: https://xclacksoverhead.org/home/about


## Installation
Django Clacks is on [PyPI](https://pypi.org/project/django-clacks/). Install it with `pip install django-clacks` or add it with your dependency manager.



## Quickstart
Add `clacks.middleware.ClacksMiddleware` to your `MIDDLEWARE` setting:
```py
MIDDLEWARE = [
    # ...
    "clacks.middleware.ClacksMiddleware",
    # ...
]
