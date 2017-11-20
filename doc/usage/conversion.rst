Wending/Gregorian Conversion
============================

Datárum has 2 conversion methods available, ``from_date`` and ``to_gregorian``.
``from_date`` takes a python datetime object and returns the equivalent wending
object::

    >>> dt = datetime.datetime(2017, 8, 15)
    >>> wending_date = datarum.from_date(dt)
    >>> wending_date.formatted()
    '28 Hát 225'

``to_gregorian`` converts a wending object to a datetime object::

    >>> wending_date = datarum.wending(225, 11, 28)
    >>> dt = datarum.to_gregorian(wending_date)
    >>> dt.strftime("%d %B %Y")
    '15 August 2017'
