mantis
======

Mantis a partial parser for kismet netxml logs. It reads the XML-files produced
by kismet and spits data into couchdb. The software is intented for
privacy-aware Wifi-mapping efforts.

license: AGPL
```
if you use this code
you and your children’s children
must make your source free
```

The database layout follows the original XML format. The UID view uses the
BSSID and the SSIDs as key ("[ BSSID, [SSIDs]]"). The associated ID points
to the source document, where additional information can be retrieved from.

references
----------
* [kismet](http://www.kismetwireless.net/) the sniffer
* [CouchDB](http://www.couchdb.org) the database
* [py-couchdb](https://py-couchdb.readthedocs.org) the CouchDB bindings for python
    * install on fedora: ```python3-pip install pycouchdb```