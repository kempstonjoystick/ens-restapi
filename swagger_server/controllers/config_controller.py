import connexion
import six

from swagger_server.models.gig_interface_config import GigInterfaceConfig  # noqa: E501
from swagger_server.models.std_response import StdResponse  # noqa: E501
from swagger_server import util


def config_which_db_interfaces_gigabit_gig_get(whichDB, gig):  # noqa: E501
    """Retrieve gigabit interface configuration

    Retrieves the configuration attributes of one or more gigabit interfaces # noqa: E501

    :param whichDB: 
    :type whichDB: str
    :param gig: 
    :type gig: str

    :rtype: GigInterfaceConfig
    """
    return 'do some magic!'


def config_which_db_interfaces_gigabit_gig_put(whichDB, gig, body=None):  # noqa: E501
    """Create or Replace Gigabit interfaces

    Define a gigabit interface.  Changes must be committed to take effect. # noqa: E501

    :param whichDB: 
    :type whichDB: str
    :param gig: 
    :type gig: str
    :param body: 
    :type body: dict | bytes

    :rtype: StdResponse
    """
    if connexion.request.is_json:
        body = GigInterfaceConfig.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
