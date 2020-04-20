#!/bin/bash
var=thetao

python section_trends.py ${var} A3 #vel_comp #section

python section_trends.py ${var} P16

python section_trends.py ${var} IR06

python section_trends.py ${var} I06

python section_trends.py ${var} A21

python section_trends.py ${var} S3

