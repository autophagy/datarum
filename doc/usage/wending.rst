Wending
=======

I have named this merger of revolutionary calendar and Old English names the
'Wending' calendar, which means a turning round, changing, or revolution.

Wending Creation
----------------

There is a class within datarum called ``wending`` that represents a Wending date,
and can be invoked via::

    from datarum import wending

A Wending date can be created 3 ways. The first, via a constructor giving the
year, month and date::

    new_wending = wending(226, 3, 13)

The second, is by creating the Wending date of today::

    today_wending = wending.today()

The third, is via a date string::

    date_string_wending = wending.from_date_string('30 mist 226')

The date string constructor is intended to be used with user input, so that to
create the date 01 Mǽdland 226, you can pass in ``'01 maedland 226'`` - as
typing the æsc, thorn, and other accented characters can be a little tricky.

Wending Details
---------------

A created wending date can then be used in date comparisons::

    >>> w1 = wending.from_date_string('25 mist 226')
    >>> w2 = wending.from_date_string('30 mist 226')
    >>> w1 < w2
    True

``__eq__``, ``__le__``, ``__lt__``, ``_ge__`` and
``__gt__`` are all supported.

Wending dates also support returning formatted of their dates::

    >>> wending_date = wending(226, 7, 13)
    >>> wending_date.formatted()
    '13 Sǽd 226'

as well as returning a (year, month, day) tuple::

    >>> wending_date = wending(226, 7, 13)
    >>> wending_date.tuple()
    (226, 7, 13)
