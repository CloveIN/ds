# -*-coding:utf-8 -*-
from django.http import HttpResponse

import atexit
from pyVmomi import vim
from pyVim import connect

def power(request):
    uuid=request.GET.get('uuid')
    op_type=request.GET.get('type')
    print op_type
    try:
        si = connect.SmartConnectNoSSL(host="172.16.3.141",
                                       user="administrator@vsphere.local",
                                       pwd="Server@2012",
                                       port=443)
    except vim.fault.InvalidLogin:
        print("Could not connect to the specified host using specified "
              "username and password")
        return -1

    atexit.register(connect.Disconnect, si)
    off = si.content.searchIndex.FindByUuid(None, uuid, True, True)
    if op_type=='Off':
        off.ShutdownGuest()
    elif op_type=='On':
        off.PowerOn()
    elif op_type=='Reboot':
        off.RebootGuest()
    return HttpResponse(op_type)


