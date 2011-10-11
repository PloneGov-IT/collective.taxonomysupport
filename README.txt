What is this?
=============

This product add a new field for all Plone contents (someway similar to keyword field) that allow to
select one or more taxonomies to reference.

A Taxonomy is like normal folder, you can create them all around the site. They make only some
differences when you add additional contents inside them (but to select a taxonomy for a content
you don't need that the content is inside it).

Also the taxonomy support can/must explicitly enabled on the site and/or in one ore many of the
site subsections. In this way you can have different Taxonomy configuration in different areas of
the site.

The list of taxonomies selectable is filtered locally if there are different sections activated
with a marker interface (see instructions below).

The activation of one section, block the inheritance of other taxonomies from upper levels.

If I create and object in this section, I only see taxonomies of the current section, and the object
outside that section doesn't see its taxonomies.

The filtering policy is the following:
* if there isn't any parent of the object that implements the "*ITaxonomyLevel*" interface, no one
taxonomy will be shown and so no one are selectable.
* if there are one or more parents that provides the interface, we take the nearest parent and search
  its availables taxonomies.
* if there aren't taxonomies, or there isn't any activated object (object that implements ITaxonomyLevel interface.
  It could be also the site root) the field doesn't appears in the field edit form.
* if an object is created inside a taxonomy, the taxonomy will be the default value in the field.

Instructions
------------

To activate the taxonomy level, you have to do the following steps:
* go in the ZMI of the folder/section/taxonomy that you want to enable
* in the "*Interfaces*" tab, add "*collective.taxonomysupport.interfaces.taxonomy_layer.ITaxonomyLevel*"
  to the "*Provided Interfaces*" list.
* Reindex the object (reindexing the whole catalog is the simplest way, but can take a long time)

Sorry, right now the aren't any "user-friendly-Plone-UI-way" to do this.

You can also mark an object as a Taxonomy.
To do this, you need to do the previous steps, but for "*collective.taxonomysupport.interfaces.folder_taxonomy.IFolderTaxonomy*"
interface.
  