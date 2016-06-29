# -*- coding: utf-8 -*-
from collective.taxonomysupport import logger
from collective.taxonomysupport import taxonomysupportMessageFactory as _
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
import transaction


class FixSearchableText(BrowserView):
    """
    """

    def __call__(self):
        """
        """
        if not self.request.form.get('form.button.Update', ''):
            return self.index()
        pc = getToolByName(self.context, 'portal_catalog')
        pu = getToolByName(self.context, "plone_utils")
        site_areas = pc.uniqueValuesFor('SiteAreas')
        items = pc(SiteAreas=site_areas)
        items_list = list(items)
        failure_list = []
        logger.info('-- Starting SearchableText update --')
        logger.info('Found %s items' % len(items_list))
        savepoint = transaction.savepoint()
        for index, item in enumerate(items_list):
            item_obj = item.getObject()
            item_path = item.getPath()
            try:
                item_obj.reindexObject(idxs=['SearchableText'])
                logger.info("%s) %s - Updated" % (index + 1, item_path))
            except:
                failure_list.append(item_path)
                if savepoint.valid:
                    # Rollback to savepoint
                    logger.info("Rolling back to last safe point. List of not updated items are listed below.")
                    savepoint.rollback()
                    # XXX: savepoints are invalidated once they are used
                    savepoint = transaction.savepoint()
                    continue
                else:
                    logger.error("Savepoint is invalid. Probably a subtransaction "
                        "was committed. Unable to roll back!")
                transaction.abort()
            if index % 500 == 0:
                logger.info('Creating new savepoint after %s objects' % index)
                savepoint = transaction.savepoint()

        if failure_list:
            pu.addPortalMessage(_('update_metadata_error',
                                  default=u'There was some errors in updating the catalog. Read error log for more infos.'),
                                'error')
            logger.error("There was a problem updating metadatas:")
            for element in failure_list:
                logger.error(element)
        else:
            pu.addPortalMessage(_('update_metadata_success',
                                  default=u'Update success!'), 'info')
            logger.info("Update success!")
        return self.context.REQUEST.RESPONSE.redirect(self.context.portal_url())
