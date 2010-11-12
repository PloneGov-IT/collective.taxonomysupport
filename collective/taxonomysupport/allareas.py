# -*- coding: utf-8 -*-

from Products.CMFCore.permissions import View
from Products.CMFCore.utils import getToolByName
from AccessControl import ClassSecurityInfo

from Products.ATContentTypes.criteria import registerCriterion, \
                                             LIST_INDICES
from Products.ATContentTypes.interfaces import IATTopicSearchCriterion
from Products.ATContentTypes.criteria.base import ATBaseCriterion
from Products.ATContentTypes.criteria.schemata import ATBaseCriterionSchema

from collective.taxonomysupport.interfaces import IFolderTaxonomy

ATAllAreasSchema = ATBaseCriterionSchema

class ATAllAreasCriterion(ATBaseCriterion):
    """A criterion that search for all Taxonomy in the site"""

    __implements__ = ATBaseCriterion.__implements__ + (IATTopicSearchCriterion, )
    security       = ClassSecurityInfo()
    schema         = ATAllAreasSchema
    meta_type      = 'ATAllAreasCriterion'
    archetype_name = 'All Taxonomy Criterion'
    shortDesc      = 'Show all Taxonomy in the site'

    security.declareProtected(View, 'getCriteriaItems')
    def getCriteriaItems(self):
        catalog = getToolByName(self, 'portal_catalog')
        results = catalog(object_provides=IFolderTaxonomy.__identifier__)
        return tuple( [x.Title for x in results] )

registerCriterion(ATAllAreasCriterion, LIST_INDICES)
