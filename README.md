# Django Clacks
The unseen, silent tribute to those we have lost.

<hr>

## Installation
Django Clacks is on [PyPI](https://pypi.org/project/django-clacks/). Install it with `pip install django-clacks` or add it with your project's dependency manager.



## Quickstart
Add `clacks.middleware.ClacksMiddleware` to your `MIDDLEWARE` setting:
```py
MIDDLEWARE = [
    ...,
    "clacks.middleware.ClacksMiddleware",
    ...,
]
