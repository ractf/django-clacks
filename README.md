# Django Clacks
The unseen, silent tribute to those we have lost.
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
You can modify the names used with the `CLACKS_NAMES` setting. For example, the following setting:
```py
CLACKS_NAMES = [
    "Terry Pratchett",
    "Joe Armstrong",
]
```
Will result in an `X-Clacks-Overhead` header containing `GNU Terry Pratchett, Joe Armstrong`.
