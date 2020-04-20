#!/bin/bash
var=thetao
for d in {1,300,700,2000,6000};do
  python plot_stdmap.py ${var} ${d}
done
