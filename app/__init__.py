import sys
import os

import boto3

from . import workx

def entry_point():
    workx.helo()
    env = os.getenv('DEV', False)
    if env:
        print("work on dev")
    else:
        print("work on prod")
    
    # dyno = boto3.client('dynamodb')
    arg = None
    if len(sys.argv) > 1:
        arg = sys.argv[1]
    
    print("MAIS DOCKER")
    print("entrou com", arg)
