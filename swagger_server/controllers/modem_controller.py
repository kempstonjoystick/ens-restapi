import connexion
import six

from swagger_server.models.lte_interface_proto_modem_info_hardware import LTEInterfaceProtoModemInfoHardware  # noqa: E501
from swagger_server.models.std_response import StdResponse  # noqa: E501
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
        req = GetModemReq()
        results = stub.GetModems(req).modems
        responses = []
        for result in results:
            current_resp = []
            for current_value in result.hardware.current:
                current_resp.append(current_value)
            supported_resp = []
            for supported_value in result.hardware.supported:
                supported_resp.append(supported_value)
            responses.append(LTEInterfaceProtoModemInfoHardware(manufacturer=result.hardware.manufacturer, model=result.hardware.model, revision=result.hardware.revision, equipment_id=result.hardware.equipment_id, supported=supported_resp, current=current_resp))
        return responses
    #except Exception as e:
    #    return e, 404
    return StdResponse(status=403, message="Could not connect with GRPC channel", action="GET")

def get_modem(eqptId):  # noqa: E501
    """Returns a single modem

    Get the modem details for a single modem # noqa: E501

    :param eqptId: Optional Equipment ID to only return a single modem
    :type eqptId: str

    :rtype: List[LTEInterfaceProtoModemInfoHardware]
    """
    if len(eqptId) != 15:
        return StdResponse(status=400, message="Invalid Equipment ID", action="GET")
    
    with grpc.insecure_channel('10.64.204.135:35130') as channel:
        stub = ModemHandlerStub(channel)
        req = GetModemReq()
        results = stub.GetModems(req).modems
        for result in results:
            if result.hardware.equipment_id == eqptId:
                current_resp = []
                for current_value in result.hardware.current:
                    current_resp.append(current_value)
                supported_resp = []
                for supported_value in result.hardware.supported:
                    supported_resp.append(supported_value)
                return LTEInterfaceProtoModemInfoHardware(manufacturer=result.hardware.manufacturer, model=result.hardware.model, revision=result.hardware.revision, equipment_id=result.hardware.equipment_id, supported=supported_resp, current=current_resp)
        return StdResponse(status=404, message="Equipment ID does not exist", action="GET")
    return StdResponse(status=403, message="Could not connect with GRPC channel", action="GET")

