.. contents:: **Table of contents**

What is this?
=============

This product add a new field to all Plone contents (someway similar to keyword field) that allow to
select one or more **taxonomies** to reference.

A Taxonomy is like normal folder, you can create them all around the site. They make only some
differences when you add additional contents inside them (but to select a taxonomy for a content
you don't need that the content is inside it).

Also the taxonomy support can/must be explicitly enabled on the site and/or in one ore many of the
site subsections. In this way you can have different Taxonomy configuration in different areas of
the site.

The list of taxonomies selectable is filtered locally if there are different sections activated
with a marker interface (see instructions below).

The activation to one section block the inheritance of other taxonomies from upper levels.

The filtering policies are the following:

* if there isn't any parent of the object that implements the "*ITaxonomyLevel*" interface, no
  taxonomy will be shown and so no one are selectable.
* if there are one or more parents that provides the interface, we take the nearest parent and search
  its availables taxonomies.
* if there aren't taxonomies, or there isn't any activated object (object that implements ITaxonomyLevel
  interface; it could be also the site root) the field doesn't appears in the field edit form.
* if an object is created inside a taxonomy, the taxonomy will be the default value in the field.

Hot to use?
===========

To activate the taxonomy level you can access the "*Add to taxonomy roots*" in the "Action" menu.

You can also mark an object as a Taxonomy.
To do this, you need to do the previous steps, but for "*collective.taxonomysupport.interfaces.folder_taxonomy.IFolderTaxonomy*"
interface.

Collection criteria
-------------------

This product add also a new collection criteria ("*Site Areas*") for easilly use taxonomies in (old-style) collections.

Dependencies
============

This product has been tested on:

* Plone 3.3
* Plone 4.2

Credits
=======
  
Developed with the support of:

* `Regione Emilia Romagna`__

* `Provincia di Ferrara`__

  .. image:: http://www.provincia.fe.it/Distribuzione/logo_provincia.png
     :alt: Provincia di Ferrara - logo

All of them supports the `PloneGov initiative`__.

__ http://www.regione.emilia-romagna.it/
__ http://www.provincia.fe.it/
__ http://www.plonegov.it/

Authors
=======

This product was developed by RedTurtle Technology team.

.. image:: http://www.redturtle.it/redturtle_banner.png
   :alt: RedTurtle Technology Site
   :target: http://www.redturtle.it/
