#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 16:32
# @Author  : lixiaofeng
# @Site    : 
# @File    : except_check.py
# @Software: PyCharm

from base.models import Project, Sign, Environment, Interface, Case, Plan, Report
from django.contrib.auth.models import User  # django自带user
import logging

log = logging.getLogger('log')  # 初始化log


def project_info_logic(prj_name, prj_id=''):
    """
    项目新增、编辑逻辑
    :param prj_name:
    :param prj_id:
    :param make:
    :return:
    """
    if prj_name == '':  # 判断输入框
        return '项目名称不能为空！'
    else:
        if not prj_id:
            name_exit = Project.objects.filter(prj_name=prj_name)
        else:
            name_exit = Project.objects.filter(prj_name=prj_name).exclude(prj_id=prj_id)
        if name_exit:
            return '项目: {}，已存在！'.format(prj_name)
        else:
            return 'ok'


def sign_info_logic(sign_name, sign_id=''):
    """
    签名新增、编辑逻辑
    :param sign_name:
    :return:
    """
    if sign_name == '':
        return '签名名称不能为空！'
    if not sign_id:
        name_exit = Sign.objects.filter(sign_name=sign_name)
    else:
        name_exit = Sign.objects.filter(sign_name=sign_name).exclude(sign_id=sign_id)
    if name_exit:
        return '签名: {}，已存在！'.format(sign_name)
    else:
        return 'ok'


def env_info_logic(env_name, url, env_id=''):
    if env_name == '':
        return '环境名称不能为空！'
    if url == '':
        return 'url不能为空！'
    if not env_id:
        name_exit = Environment.objects.filter(env_name=env_name)
    else:
        name_exit = Environment.objects.filter(env_name=env_name).exclude(env_id=env_id)
    if name_exit:
        return '环境: {}，已存在！'.format(env_name)
    else:
        return 'ok'


def interface_info_logic(if_name, url, method, is_sign, data_type, is_headers, if_id=''):
    if if_name == '':
        return '接口名称不能为空！'
    if url == '':
        return 'url不能为空！'
    if method == '':
        return '请选择接口的请求方式！'
    if is_sign == '':
        return '请设置接口是否需要签名！'
    if data_type == '':
        return '请选择接口的请求数据类型！'
    if is_headers == '':
        return '请设置接口是否需要设置请求头！'
    if not if_id:
        name_exit = Interface.objects.filter(if_name=if_name)
    else:
        name_exit = Interface.objects.filter(if_name=if_name).exclude(if_id=if_id)
    if name_exit:
        return '接口: {}，已存在！'.format(if_name)
    else:
        return 'ok'


def format_params(params):
    """
    格式化参数
    :param params:
    :return:
    """
    if params.method == 'get':
        method = 0
    elif params.method == 'post':
        method = 1
    elif params.method == 'delete':
        method = 2
    elif params.method == 'put':
        method = 3
    else:
        method = ''
    if params.is_sign == 0:
        is_sign = 0
    elif params.is_sign == 1:
        is_sign = 1
    else:
        is_sign = ''
    if params.is_header == 0:
        is_headers = 0
    elif params.is_header == 1:
        is_headers = 1
    else:
        is_headers = ''
    return method, is_sign, is_headers
