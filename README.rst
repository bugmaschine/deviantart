new-deviantart 0.1.5
======================================

'new-deviantart' is a python package that provides easy access to the deviantart API.


Installation
----------

Installation using ``pip``::

    pip install new-deviantart

Documentation
-------------

The documentation for this package can be found under: https://neighbordog.github.io/deviantart/

Basic usage
----------

.. code:: python

   #import new-deviantart library
   import new-deviantart

   #create an API object with your client credentials
   da = new-deviantart.Api("YOUR_CLIENT_ID", "YOUR_CLIENT_SECRET")

   #fetch daily deviations
   dailydeviations = da.browse_dailydeviations()

   #loop over daily deviations
   for deviation in dailydeviations:

       #print deviation title
       print deviation.title

       #print username of author of deviation
       print deviation.author.username


License
-------

The deviantart python package is licensed under the `MIT license
<https://opensource.org/licenses/MIT>`_.
