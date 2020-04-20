#!/usr/bin/bash
#trends
var=thetao
for d in {1,300,700,2000,6000};do
  python subsurf_trend.py ${var} ${d}
done
