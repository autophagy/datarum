=======
Datárum
=======

.. image:: http://scieldas.autophagy.io/rtd/datarum.png
    :target: http://datarum.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: http://scieldas.autophagy.io/travis/Autophagy/datarum.png
    :target: https://travis-ci.org/Autophagy/datarum
    :alt: Build Status

.. image:: http://scieldas.autophagy.io/pypi/version/datarum.png
   :target: https://pypi.python.org/pypi/datarum/
   :alt: Pypi Version

.. image:: http://scieldas.autophagy.io/pypi/pyversions/datarum.png
   :target: https://pypi.python.org/pypi/datarum/
   :alt: Python Version

.. image:: http://scieldas.autophagy.io/licenses/MIT.png
   :target: LICENSE
   :alt: MIT License

Datárum is a small python library to convert Gregorian dates to Wending,
an Old English variant on the `French Republican calendar`_, for use in
various projects. Documentation is available on `ReadTheDocs`_.

The leap years are calculated according to the Romme rule, which uses
the 4-100-400 rule from the Gregorian calendar (a leap day becoming an
extra 6th Wending day).

Hwý?
----

I appreciate the political impulse behind the French Republican
calendar, as well as its more rational system (12 months of 30 days,
plus 5/6 celebratory days at the end of the year). However, I like the
aesthetics of Old English more than the original french names for the
months, so I’ve attempted to rougly translate or otherwise approximate
the Old English equivalents.

Translation
-----------

+-------------------+----------------+-------------+-----------------------------+
|                   | French         | Old English | Translation                 |
+===================+================+=============+=============================+
| **Autumn**        | Vendémiaire    | Hærfest     | Harvest, autumn             |
+-------------------+----------------+-------------+-----------------------------+
|                   | Brumaire       | Mist        | Mist, fog                   |
+-------------------+----------------+-------------+-----------------------------+
|                   | Frimaire       | Forst       | Frost                       |
+-------------------+----------------+-------------+-----------------------------+
| **Winter**        | Nivôse         | Snáw        | Snow                        |
+-------------------+----------------+-------------+-----------------------------+
|                   | Pluviôse       | Reg         | Rain                        |
+-------------------+----------------+-------------+-----------------------------+
|                   | Ventôse        | Wind        | Wind                        |
+-------------------+----------------+-------------+-----------------------------+
| **Spring**        | Germinal       | Sǽd         | Seed                        |
+-------------------+----------------+-------------+-----------------------------+
|                   | Floréal        | Blóstm      | Blossom, flower             |
+-------------------+----------------+-------------+-----------------------------+
|                   | Prairial       | Mǽdland     | Meadow-land                 |
+-------------------+----------------+-------------+-----------------------------+
| **Summer**        | Messidor       | Ríp         | Reaping, harvest            |
+-------------------+----------------+-------------+-----------------------------+
|                   | Thermidor      | Hát         | Heat                        |
+-------------------+----------------+-------------+-----------------------------+
|                   | Fructidor      | Wæstm       | Growth, produce, fruit      |
+-------------------+----------------+-------------+-----------------------------+
| **Complementary** | Sansculottides | Wending     | A turning round, revolution |
+-------------------+----------------+-------------+-----------------------------+

.. _French Republican calendar: https://en.wikipedia.org/wiki/French_Republican_Calendar
.. _ReadTheDocs: http://datarum.readthedocs.io
