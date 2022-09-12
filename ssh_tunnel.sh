#!/bin/bash

host=`conda run --no-capture -n ngrok_publisher python main.py host`
port=`conda run --no-capture -n ngrok_publisher python main.py port`

ssh root@$host -p $port
