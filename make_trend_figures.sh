#!/usr/bin/bash
#trends
var=thetao
for d in {1,300,700,2000,6000};do
  #python plot_trend.py ${var} _trend_matrix ${d}
  python plot_pval.py ${var} _trend_pvalue ${d}
done
