#!/bin/bash

host=`conda run --no-capture -n ngrok_publisher python main.py host`

echo $host