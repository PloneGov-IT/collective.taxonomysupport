from collective.taxonomysupport.interfaces import ITaxonomyLayer
from zope.component import getUtility, queryUtility
from zope.schema.interfaces import IVocabularyFactory
from Products.CMFCore.utils import getToolByName
from Acquisition import aq_chain
from collective.taxonomysupport.interfaces import IFolderTaxonomy

def getDefaultTaxonomy(self):
    if not self.REQUEST.__provides__(ITaxonomyLayer):
        return ''
    vocab=queryUtility(IVocabularyFactory,name='collective.taxonomyvocab')
    list_taxonomies=vocab(self)
    if not list_taxonomies:
        return ''
    taxonomy_folder=[x for x in self.getFolderWhenPortalFactory().aq_chain if getattr(x,'portal_type','')=='FolderTaxonomy']
    if not taxonomy_folder:
        return ''
    for elem in list_taxonomies:
        if elem.value == taxonomy_folder[0].UID():
            return elem.value
    return ''

def getSiteAreas(self):
        """Generated accessor"""
        return self.getRawSiteAreas()

def getRawSiteAreas(self):
    """Generated raw accessor"""
    siteAreas = list(self.getField('siteAreas').get(self))
    for parent in aq_chain(self):
        if IFolderTaxonomy.providedBy(parent):
            siteAreas.append(parent.UID())
    no_dupl = set(siteAreas)
    return tuple(no_dupl)

def SiteAreas(self):
        """Generated indexes"""
        portal_catalog=getToolByName(self,'portal_catalog')
        if not self.REQUEST.__provides__(ITaxonomyLayer):
            return ()
        areas=getattr(self,'siteAreas',())
        if not areas:
            return ()
        listtitle = []
        for elem in areas:
            results = portal_catalog.searchResults(UID=elem)
            if results:
                listtitle.append(results[0].Title)
        return tuple(listtitle)

def showAreas(self):
    if not self.REQUEST.__provides__(ITaxonomyLayer):
        return ''
    vocab=queryUtility(IVocabularyFactory,name='collective.taxonomyvocab')
    if not vocab(self):
        return False
    return True