Wending/Gregorian Conversion
============================

Datárum has 2 conversion methods available from converting between
Wending dates and Gregorian dates. These are ``fromdatetime`` and
``todatetime`` and, as expected, they both involve either consuming
or returning an instance of Python's ``datetime`` class::

    >>> dt = datetime.datetime(2017, 8, 15)
    >>> wending_date = datarum.wending.fromdatetime(dt)
    >>> wending_date.strftime('{daeg} {month} {gere}')
    '28 Hát 225'

    >>> wending_date = datarum.wending(225, 11, 28)
    >>> dt = wending_date.todatetime()
    >>> dt.strftime("%d %B %Y")
    '15 August 2017'
