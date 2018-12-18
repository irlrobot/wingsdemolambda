#!/usr/bin/env python3

def handler(event, context):
    print("Hello World!")
    print("=====Event=====")
    print("{}".format(event))
    print("=====Context=====")
    print("{}".format(context))
    