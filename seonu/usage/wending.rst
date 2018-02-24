Wending
=======

I have named this merger of revolutionary calendar and Old English names the
'Wending' calendar, which means a turning round, changing, or revolution.

Wending Creation
----------------

There is a class within datarum called ``wending`` that represents a Wending date,
and can be invoked via::

    from datarum import wending

A Wending date can be created 5 ways. The first, via a constructor giving the
year, month and date, hour, minute and second (the latter 3 being optional)::

    new_wending = wending(226, 3, 13)
    new_wending = wending(226, 3, 13, 15, 30, 25)

The second, is by creating the current Wending datetime::

    today_wending = wending.now()

The third, is via ``fromordinal``. This returns a Wending date that offset a
number of days from the inception date of the calendar::

    new_wending = wending.fromordinal(1000)

The fourth, is via a conversion from a Python ``datetime`` object::

    dt = datetime.datetime(2018, 07, 01)
    wending_from_dt = wending.fromdatetime(dt)

The fifth, is via ``strptime``::

    wending_date = wending.strptime('30 mist 226 // 12.35', '{daeg} {month} {gere} // {tid_zero}.{minute_zero}')

``strptime`` aims to loosely mimic the similarly named function from the python
datetime library in that it produces a wending object from a string and a given
format. ``strptime`` currently supports in the formatting string:

- ``daeg_zero``   :: Dæg of Mónþ as zero padded number
- ``daeg``        :: Dæg of Mónþ as decimal number
- ``month``       :: Mónþ as formatted string
- ``gere``        :: Gere as decimal number
- ``tid_zero``    :: Hour as zero padded number
- ``tid``         :: Hour as decimal number
- ``minute_zero`` :: minute as zero padded decimal
- ``minute``      :: minute as decimal number
- ``second_zero`` :: second as zero padded decimal
- ``second``      :: second as decimal

The month element also supports 'easy month' format, where the string 'maedland'
is a valid substitute for 'Mǽdland', for environments/set ups where typing the
æsc, thorn, and other accented characters can be a little tricky.

Wending Details
---------------

A wending date also supports ``strftime`` to output a specifically formatted
date string. It supports same elements as ``strptime``::

    >>> w = wending(226, 2, 7, 12, 5, 0)
    >>> w.strftime('{daeg} {month} {gere} // {tid_zero}.{minute_zero}')
    '7 Mist 226 // 12.05'

A created wending date can also be used in date comparisons::

    >>> w1 = wending.strptime('25 mist 226', '{daeg} {month} {gere}')
    >>> w2 = wending.strptime('30 mist 226', '{daeg} {month} {gere}')
    >>> w1 < w2
    True

``__eq__``, ``__le__``, ``__lt__``, ``_ge__`` and
``__gt__`` are all supported.

Wending can also return a (year, month, day) tuple::

    >>> wending_date = wending(226, 7, 13)
    >>> wending_date.tuple()
    (226, 7, 13)
