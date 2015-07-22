#! /usr/bin/env python
# encoding: UTF-8

'''This file defines functions to get all bsps defined in py/waf/defaults/bsp'''

import wx
import inspect
import py.waf.defaults.bsp

def get_bsp_classes(module):
        bsp_list = []
        skip = ("__class__", "Base", "Config")

        for tmp_name, tmp_obj in inspect.getmembers(module):
                for name, obj in inspect.getmembers(tmp_obj):
                        if inspect.isclass(obj) and name not in skip:
                                bsp_list.append(obj)
        return bsp_list

