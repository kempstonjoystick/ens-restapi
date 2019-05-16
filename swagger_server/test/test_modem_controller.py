# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.lte_interface_proto_modem_info_hardware import LTEInterfaceProtoModemInfoHardware  # noqa: E501
from swagger_server.test import BaseTestCase


class TestModemController(BaseTestCase):
    """ModemController integration test stubs"""

    def test_get_all_modems(self):
        """Test case for get_all_modems

        Returns all modems
        """
        response = self.client.open(
            '/vse/api/v2.0//modem',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
