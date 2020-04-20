#!/bin/bash
var=thetao
for d in {1,300,700,2000,6000};do
  python globmean.py ${var} ${d}
done

