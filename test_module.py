#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : test_module.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2024/3/31
import os
import sys

from pyquickjs import Context

base_path = os.path.dirname(__file__)


def _(p):
    return os.path.join(base_path, p)


def moduleloader(number):
    print(f"module_ name: {number}")
    _str = ''
    with open(_(number), encoding='utf-8') as f:
        _str = f.read()
    #print(_str)
    return _str


def handleLog(*args):
    print(*args)


if __name__ == '__main__':
    module_js = """
    function addd(a,b){
    return a+b
    }
    export default {
    addd
    }
    """
    mod_test = '''import { fib } from "./fib_module.js";
    import q from "./1.js";

    console.log("Hello World 你好");

    console.log(typeof(q.add));

    console.log("fib(10)=", fib(10));'''

