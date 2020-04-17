============
github-users
============

.. image:: github.png

=================================================
Repository created to test github api with pytest
=================================================


------------------
Dependencies Used:
------------------

 - python = "^3.8"
 - requests = "^2.23.0"
 - pytest = "^5.4.1"
 - black = {version = "^19.10b0", allow-prereleases = true}
 - mypy = "^0.770"
 - responses = "^0.10.12"

------------------
Run tests and mypy
------------------

.. code-block::

    >>> pytest tests && mypy api/github.py 
