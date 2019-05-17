# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.gig_interface_config import GigInterfaceConfig  # noqa: E501
from swagger_server.models.std_response import StdResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestConfigController(BaseTestCase):
    """ConfigController integration test stubs"""

    def test_config_which_db_interfaces_gigabit_gig_get(self):
        """Test case for config_which_db_interfaces_gigabit_gig_get

        Retrieve gigabit interface configuration
        """
        response = self.client.open(
            '/vse/api/v2.0/config/{whichDB}/interfaces/gigabit/{gig}/'.format(whichDB='whichDB_example', gig='gig_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_config_which_db_interfaces_gigabit_gig_put(self):
        """Test case for config_which_db_interfaces_gigabit_gig_put

        Create or Replace Gigabit interfaces
        """
        body = GigInterfaceConfig()
        response = self.client.open(
            '/vse/api/v2.0/config/{whichDB}/interfaces/gigabit/{gig}/'.format(whichDB='whichDB_example', gig='gig_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
