Introduction:
-------------
This product add a new field for all archetypes that allow to select one or more taxonomies to reference.
The list of taxonomies is filtered locally if there are different sections activated with a marker interface (the instructions are above).
The activation of one section, block the Inheritance of other taxonomies.
If i create and object in this section, i only see taxonomies of the current section, and the object ouside that section doesn't see his taxonomies.

The filtering policy is the following:
 * if there isn't any parent of the object that implements the leve linterface, no one taxonomy will be shown.
 * if there are one or more parents with the interface, we take the nearest parent and search his availables taxonomies. 
 
If there isn't taxonomies, the field doesn't appears in the archetype's schema.
If an object is created directly in a taxonomy, the taxonomy will be the default value in the field.

Instructions:
-------------
To activate the taxonomy level, you have to do the following steps::
 * Go in the ZMI of the folder/section/taxonomy that you want to enable
 * in the "interfaces" tab, add "collective.taxonomysupport.interfaces.taxonomy_layer.ITaxonomyLevel" to Provided Interfaces list.
 * Reindex the object
 