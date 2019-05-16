import connexion
import six

from swagger_server.models.gig_interface_config import GigInterfaceConfig  # noqa: E501
from swagger_server.models.std_response import StdResponse  # noqa: E501
from swagger_server import util

from ctypes import *

OVN_DICTLISTFUNC = CFUNCTYPE(c_int, c_char_p, c_char_p, c_uint, c_uint) 
class STRUCT_PYsetInfo(Structure):
    _fields_ = [("action", c_uint),
                ("text", c_char * 256)]

class STRUCT_default(Structure):
    """Base ctypes structure class for uiApi interface structures
       Subclass field names should match JSON data definitions.
       JSON often uses '-' in field names (i.e. "ccm-enable").  

       To automate the field sets this must be converted to
       "ccm_enable" in order for the exec to work.
    """
        
    # sub class must define if needed
    def clear():
        pass

class STRUCT_EthernetInterface(STRUCT_default):
    _fields_ = [("updateAll", c_int),
                ("name",c_char_p),
                ("alias",c_char_p),
                ("admin",c_char_p),       # last common field
                ("mtu", c_int),           # gigabit specific
                ("duplex", c_char_p),
                ("auto_negotiation", c_char_p),
                ("crossover", c_char_p),
                ("speed", c_int),
                ("master_slave", c_char_p),
                ("reserved_mac", c_char_p),                   
                ("ipaddr", c_char_p),     # inband specific
                ("netmask", c_char_p),
                ("vlanId", c_int),
                ("mode", c_char_p),
                ("output_rate", c_int),
                ("queue_profile", c_char_p),
                ("oam", c_char_p),
                ("oam_activity", c_char_p),
                ("oam_loopback", c_char_p),
                ("port_type", c_char_p),  # vport specific
                ("dev_name", c_char_p),   # vport specific
                ("jumbo_frame", c_char_p),# vport specific
                ("ipsec_connection", c_char_p),# ipsec specific
		("public_vrf", c_char_p),# ipsec specific
                ("lacp", c_char_p),       # aggr specific
                ("load_balance", c_char_p),      
                ("max_active_members", c_int),
                ("actor_sys_priority", c_int),
                ("domain", c_char_p),
                ("firewall_profile", c_char_p),
                ("ip_addr", c_char_p), #gig, vport, ip, aggr, lte
                ("owner_tag", c_char_p),
                ("dest_ip", c_char_p),    # tunnel specific
                ("tunnel_id", c_int),     # tunnel specific
                ("type", c_char_p),       # tunnel specific
                ("tx_key_mat", c_char_p),       # tunnel specific
                ("rx_key_mat", c_char_p),       # tunnel specific
                ("tx_auth_mat", c_char_p),       # tunnel specific
                ("rx_auth_mat", c_char_p),       # tunnel specific
                ("key_mat_type", c_char_p),       # tunnel specific
                ("spi", c_int),    # tunnel specific
                ("active_pdp", c_char_p),
                ("l3shunt", c_char_p),     # ip specific
                ("mac_addr", c_char_p), # vport specific
                ("binding_interface", c_char_p),
                ("dest_ipv6_addr",  c_char_p)]

    def clear(self):
        self.updateAll = 0
        self.name = None
        self.alias = None
        self.admin = None
        self.mtu = -1
        self.duplex = None
        self.autonegotiation = None
        self.crossover = None
        self.speed = -1
        self.master_slave = None
        self.reserved_mac = None
        self.ipaddr = None
        self.netmask = None
        self.vlanId = -1
        self.mode = None
        self.output_rate = -1
        self.queue_profile = None
        self.oam = None
        self.oam_activity = None
        self.oam_loopback = None
        self.port_type = None
        self.dev_name = None
        self.jumbo_frame = None
        self.lacp = None
        self.load_balance = None
        self.max_active_members = -1
        self.actor_sys_priority = -1
        self.domain = None
        self.firewall_profile = None
        self.ip_addr = None
        self.owner_tag = None
        self.dest_ip = None
        self.tunnel_id = -1
        self.type = None
        self.tx_key_mat = None
        self.rx_key_mat = None
        self.tx_auth_mat = None
        self.rx_auth_mat = None
        self.key_mat_type = None
        self.spi = -1
        self.active_pdp = None
        self.l3shunt = None
        self.mac_addr = None
        self.binding_interface = None
        self.dest_ipv6_addr = None

OVN_UIAPI_LIB="/ovn/lib/libuiApi.so.1"
handle = CDLL(OVN_UIAPI_LIB)
handle.PY_UiApicreateEthernetEntry.argtypes=[c_void_p, c_char_p, c_void_p]
handle.PY_UiApigetInterface.argtypes=[OVN_DICTLISTFUNC, c_char_p, c_uint]

def uenc(theStr):
    if None == theStr:
        return theStr
    return theStr.encode('utf-8')

def getDictData (fxn, *args):
    # Using closure
    # When the C code calls the callback it will update this local variable directly
    Data={}
    def c_get_dict_data(key,value,typeIndex,newElement):
        """
        Callback function used to return information from C to python
        """
        vStr = value.decode('utf-8')
        tStr = typeIndex.decode('utf-8')
        Data[key] = _data_type[typeIndex](value)
        return 0

    callback = OVN_DICTLISTFUNC(c_get_dict_data)
    fxn(callback, *args)
    return Data



def config_which_db_interfaces_gigabit_gig_get(whichDB, gig):  # noqa: E501
    """Retrieve gigabit interface configuration

    Retrieves the configuration attributes of one or more gigabit interfaces # noqa: E501

    :param whichDB: 
    :type whichDB: str
    :param gig: 
    :type gig: str

    :rtype: GigInterfaceConfig
    """

    response = getDictData(handle.PY_UiApigetInterface, gig, whichDB)

    cfg = GigInterfaceConfig(
        name=response.get("name"),
        admin=response.get("admin"),
        alias=response.get("alias"),
        firewall_profile=response.get("firewall_profile"),
        ip_addr=response.get("ip_addr"))
    return cfg


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
    else :
        return "Invalid Content-Type", 

    if body.name != None and body.name != "" and body.name != gig:
        return "Name mismatch", 400, StdResponse(status=400, message="Name mismatch", action="PUT")

    uiInfo = STRUCT_PYsetInfo()
    intData = STRUCT_EthernetInterface()
    intData.clear()
    intData.updateAll = 1
    intData.name = uenc(gig)
    intData.alias = uenc(body.alias)
    intData.admin = uenc(body.admin)
    intData.firewall_profile = uenc(body.firewall_profile)
    intData.ip_addr = uenc(body.ip_addr)

    intType = "gigabit"
    rc = handle.PY_UiApicreateEthernetEntry(byref(uiInfo), uenc(intType), byref(intData))
    #return uiApiErrorHandler(rc,uiInfo)

    #return "Success", 200, StdResponse(status=200, message="Success", action="PUT")
    return StdResponse(status=200, message="Success", action="PUT")
