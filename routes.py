#!/usr/bin/python
# -*- coding: utf-8 -*-

routes_in=(('/(?P<a>.*)','/init/$a'),) 
routes_out=(('/init/(?P<a>.*)','/$a'),) 
