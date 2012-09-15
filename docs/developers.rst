Getting Involved
================

Installing
----------

Funday Roulette is a pretty standard Django application. If you are familiar
with Django development you should be right at home.

First you'll need to clone the code base using git::

    git clone https://github.com/wraithan/funday.git

Then set up a `virtualenv <http://virtualenv.org/>`_ and then after activating
it (see virtualenv link if you don't know what I am talking about), install the
dependencies for funday::

    pip install -r requirements.txt

After that you'll set up the database, run migrations, and import a base set of
data::

    ./manage.py syncdb
    ./manage.py migrate
    ./manage.py loaddata funday_monday_import

Now it is simple as running the server and checking that things work::

    ./manage.py runserver

Contributing
------------

All development is done on github in the official repo: `wraithan/funday
<https://github.com/wraithan/funday>`_ please direct pull requests and issues
there.

Before starting work on something please make sure it is an issue in the `issue
tracker <https://github.com/wraithan/funday/issues>`_. When you are done
writing your patch please put `fixes #1` in your commit message (replacing 1
with the issue that your commit fixes) then send a pull request.

I can emphasize this part enough: please do not delete your fork until the pull
request has been closed. If it hasn't been closed and you delete you fork, I
can't pull down your code to test it before merging which means I very likely
wont merge your code.


Code Style
----------

I follow `pep8 <http://www.python.org/dev/peps/pep-0008/>`_ and `pyflakes
<https://crate.io/packages/pyflakes/0.5.0/>`_ closely. If you'd like to check
to see if your code is ready for you to send a pull request please install
fabric then run::

    fab style_check

It will tell you where you have made mistakes, or it will just exit normally
after running pep8 and pyflakes.

On top of those two, I prefer to have imports grouped in the following way::

    # python imports
    import os

    # library imports
    from django.db import models

    # local package imports
    from anyday.core import views

Within the groupings the imports should be alphabetized.
