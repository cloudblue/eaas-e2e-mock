# -*- coding: utf-8 -*-
#
# Copyright (c) 2021, Globex Corporation
# All rights reserved.
#
from connect.eaas.extension import (
    Extension,
    OK,
)


class E2EExtension(Extension):

    def process_asset_purchase_request(self, request):
        request_id = request['id']
        template_id = self.config['ASSET_REQUEST_APPROVE_TEMPLATE_ID']
        self.logger.info(f'request_id={request_id} - template_id={template_id}')
        self.client.requests[request_id]('approve').post(
            {
                'template_id': template_id,
            }
        )
        return OK
