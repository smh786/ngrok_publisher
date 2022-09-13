#!/bin/bash

read -r host port <<< "$(conda run --no-capture -n ngrok_publisher python main.py)"
ssh root@$host -p $port
