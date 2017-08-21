#!/usr/bin/python
# -*- coding: UTF-8 -*-

def test_var_args(f_arg, *args):
    print("first normal arg:", f_arg)
    for arg in args:
        print("another arg through *argv:", arg)


# test_var_args('a', 'b', 'c', 'd')

def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} == {1}".format(key, value))


greet_me(name="yasoob")
