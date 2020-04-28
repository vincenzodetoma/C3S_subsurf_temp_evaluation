#!/bin/bash
var=thetao

#python mean_section_plot.py ${var} A3 #vel_comp #section
#python mean_section_plot.py ${var} P16
#python mean_section_plot.py ${var} IR06
#python mean_section_plot.py ${var} I06
#python mean_section_plot.py ${var} A21
#python mean_section_plot.py ${var} S3

#trend plot

#python plot_section_trend.py ${var} A3 #vel_comp #section
#python plot_section_trend.py ${var} P16
#python plot_section_trend.py ${var} IR06
#python plot_section_trend.py ${var} I06
#python plot_section_trend.py ${var} A21
#python plot_section_trend.py ${var} S3

python plot_section_pval.py ${var} A3 #vel_comp #section
python plot_section_pval.py ${var} P16
python plot_section_pval.py ${var} IR06
python plot_section_pval.py ${var} I06
python plot_section_pval.py ${var} A21
python plot_section_pval.py ${var} S3




