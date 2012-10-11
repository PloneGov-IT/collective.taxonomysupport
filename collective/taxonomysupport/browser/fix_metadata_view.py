# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName
from collective.taxonomysupport import logger


class FixSiteAreasMetadata(BrowserView):
    """
    """

    def __call__(self):
        """
        """
        pc = getToolByName(self.context, 'portal_catalog')
        pu = getToolByName(self.context, "plone_utils")
        items = pc()
        items_list = list(items)
        failure_list = []
        logger.info('Found %s items' % len(items))
        for index, item in enumerate(items_list):    
            item_obj = item.getObject()
            item_path = item.getPath()
            try:
                pc.catalog_object(item_obj, item_path, update_metadata=1)
                logger.info("%s) %s - Updated" % (index, item_path))
            except:
                failure_list.append(item_path)
        if failure_list:
            pu.addPortalMessage('There was some errors in updating the catalog. Read error log for more infos.', 'error')
            logger.error("There was a problem updating metadatas:")
            for element in failure_list:
                logger.error(element)
        else:
            pu.addPortalMessage('Update success!', 'info')
        return self.context.REQUEST.RESPONSE.redirect(self.context.portal_url())
