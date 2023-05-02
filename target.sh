#!/bin/bash
DATE=$(date +"%Y-%m-%d_%H-%M-%S")
mkdir -p target/$DATE
cp src/api.py src/model.py requirements.txt models/ -r target/$DATE/
