Changelog
=========

1.4.2 (unreleased)
------------------

- Nothing changed yet.


1.4.1 (2016-06-30)
------------------

- Make taxonomy categorization searchable in SearchableText index.
  We don't provide an upgrade step to update old stored contents because it
  could be a very slow task and it's better to do it in a separate task (maybe
  with a script or pdb).
  [cekk]


1.4.0 (2012-10-12)
------------------

- Added utility view that update metadata infos [cekk]


1.3.1 (2012-08-07)
------------------

* Added catalog.xml for "SiteAreas" metadata [andrea]
* Add modify to handle default page case and add test [lucabel]
* Add import permission.zcml from CMFCore in case of plone4 [lucabel]
* Update test to works on plone 4


1.3.0 (2012-08-02)
------------------

* Added Plone 4.2 compatibility
* updated documentation [keul]
* fixed translations [keul]
* added proper i18ndude script [keul]
* Add action to mark/unmark taxonomy root [lucabel]

1.2.0 (2011-09-27)
------------------

* changed product to allow all contents to be a taxonomy, implementing IFolderTaxonomy [andrea]
* added tinyMCE configuration for FolderTaxonomy content [mirco]

1.1.0 (Unreleased)
------------------

* version 1.0.2 was bad; partial rever of changes [keul]
* added a new collection criterion, only for Taxonomy [keul]
* fixed translations [keul]

1.0.2 (2010-11-12)
------------------

* when used for collections, show all Taxonomy, not only the used ones [keul]

1.0.1 (2010-09-27)
------------------

* collective.taxonomysupport was breaking some contents like EasyNewsletter [keul]

1.0.0
-----

* Initial release
