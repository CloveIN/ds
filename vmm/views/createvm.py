# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

# 引入我们创建的表单类
from vmm.django_forms.forms import AddForm


def createvm(request):
    if request.method == 'POST':  # 当提交表单时

        form = AddForm(request.POST)  # form 包含提交的数据

        if form.is_valid():  # 如果提交的数据合法
            print(form.cleaned_data)
            return HttpResponse(form.cleaned_data)
        else:  #错误信息包含是否为空，或者符合正则表达式的规则
            print(form.cleaned_data)
    else:  # 当正常访问时
        form = AddForm()
    return render(request, 'vmm/createvm.html', {'form': form})