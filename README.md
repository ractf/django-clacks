# Django Clacks
The unseen, silent tribute to those we have lost.


![python-versions](https://img.shields.io/pypi/pyversions/django-clacks) ![version](http://img.shields.io/pypi/v/django-clacks.svg?maxAge=3600) [![discord](https://img.shields.io/discord/577123238929498122)](https://discord.gg/mErKh58nWU)
<hr>

`django-clacks` contains boilerplate code for working with the nonstandard HTTP header `X-Clacks-Overhead`.

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
```
By default, all responses will now have a header `X-Clacks-Overhead`, with the content `GNU Terry Pratchett`. <br>
You can modify the names used with the `CLACKS_NAMES` setting. The following setting:
```py
CLACKS_NAMES = [
    "Terry Pratchett",
    "Joe Armstrong",
]
```
Will result in an `X-Clacks-Overhead` header containing `GNU Terry Pratchett, Joe Armstrong`.
