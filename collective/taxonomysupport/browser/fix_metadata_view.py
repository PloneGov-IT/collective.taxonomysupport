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
        failure_list = []
        for index, item in enumerate(items):
            item_obj = item.getObject()
            item_path = item.getPath()
            try:
                pc.catalog_object(item_obj, item_path, update_metadata=1)
                logger.info("%s) %s - Updated" % (index, item_path))
            except:
                failure_list.append(item_path)
        if failure_list:
            pu.addPortalMessage('There was some errors in updating the catalog. Read error log for more infos.', 'error')
        else:
            pu.addPortalMessage('Update success!', 'info')
        self.context.REQUEST.RESPONSE.redirect('%s/@@fix_metadata_view' % self.context.portal_url())
