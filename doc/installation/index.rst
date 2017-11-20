Installation
============

Datárum requires python >= 3.6.

Via Pip
-------

You can install Datárum via pip, from `pypi`_ : ::

    python3.6 -m pip install --user datarum


Via The Repo
-------------

To install Datárum from the repo, you can clone it and set up a clean environment
with ``virtualenv``: ::

    git clone git@github.com:Autophagy/datarum.git
    cd datarum
    virtualenv .venv -p python3.6
    source .venv/bin/activate

Then, install the ``datarum`` package: ::

    pip install -e .

You can now use the ``datarum`` library.

.. _`pypi`: https://pypi.python.org/pypi/datarum/
