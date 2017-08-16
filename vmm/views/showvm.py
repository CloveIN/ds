# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

#导入vSphere SDK模块
import atexit
from pyVim import connect
from pyVmomi import vmodl
from pyVmomi import vim

def listvm(request):
    try:
            service_instance = connect.SmartConnectNoSSL(host="172.16.3.141",
                                                         user="administrator@vsphere.local",
                                                         pwd="Server@2012",
                                                         port=443)
            atexit.register(connect.Disconnect, service_instance)

            content = service_instance.RetrieveContent()

            container = content.rootFolder
            viewType = [vim.VirtualMachine]
            recursive = True
            containerView = content.viewManager.CreateContainerView(
            container, viewType, recursive)

            children = containerView.view

            return render(request,"vmm/listvm.html", {"cont:":len(children),"vms":children})
    except vmodl.MethodFault as error:
            return HttpResponse("Caught vmodl fault:"+error.msg)