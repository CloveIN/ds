# -*- coding: utf-8 -*-
from django import forms


class AddForm(forms.Form):
    user_name = forms.CharField()
    user_email = forms.EmailField()
    vm_use = forms.CharField()
    vm_os_password = forms.PasswordInput()

    vm_name = forms.CharField()

    vm_os = forms.CharField()
    vm_cpu = forms.IntegerField()
    vm_memory = forms.IntegerField()
    vm_disk = forms.IntegerField()