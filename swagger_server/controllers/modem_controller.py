import connexion
import six

from swagger_server.models.lte_interface_proto_modem_info_hardware import LTEInterfaceProtoModemInfoHardware  # noqa: E501
from swagger_server import util

import grpc
from ovnLib.protos.LTE_IF_pb2 import *
from ovnLib.protos.LTE_IF_pb2_grpc import *


def get_all_modems():  # noqa: E501
    """Returns all modems

    Get the modem details # noqa: E501


    :rtype: List[LTEInterfaceProtoModemInfoHardware]
    """
    #try:
    with grpc.insecure_channel('10.64.204.135:35130') as channel:
        stub = ModemHandlerStub(channel)
        print("-------------- GetModems --------------")
        req = GetModemReq()
        results = stub.GetModems(req).modems
        responses = []
        for result in results:
            responses.append(LTEInterfaceProtoModemInfoHardware(manufacturer=result.hardware.manufacturer, model=result.hardware.model, revision=result.hardware.revision, equipment_id=result.hardware.equipment_id))
        return responses

    #except Exception as e:
    #    return e, 404
