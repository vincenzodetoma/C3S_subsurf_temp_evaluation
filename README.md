# c3s_subsurf_temp_evaluation
This repository contains the scripts used to assess ORAS5 subsurface temperature in the framework of the Copernicus C3S_511.
All scripts are produced with Python3 and bash scripts (single files have been merged using the cdo command mergetime), using the following libraries, loaded together in a conda environment:

xarray
matplotlib
numpy
cartopy
statsmodels

In the order, the Evaluation has proceeded as follows:
 - the script make_all.sh make all calculations and plot the maps;
 - vertmean.py calculates the different contributions, calc_vert_mean.sh iterates the procedure;
 - plot_meanmap.py produce the mean map, make_meanmaps.sh iterates the procedure;
 - plot_stdmap.py produces the interannual variability maps, make_stdmaps.sh iterates the procedure; 
 - section are extracted by the scripts section*, procedure iterated by calc_sections.sh;
 - global means are calculated by glob_month_depth.py iterated by calc_glob_means.sh;
 - global mean time series done with globmean.py, make_globalmeans.sh iterates the procedure;
 - horizontal trends done with subsurf_trend.py, make_trends.sh iterates the procedure;
 - plot_trend.py makes the correspondent figure, iterated by make_trend_figures.sh
 - section trends done with section_trends.py, iterated by make_section_trends.sh
 - section figures done with the script make_section_figures.sh, mean_section_plot.py for the mean,
 plot_section_trend.py for the trend;
 
 Files are not commented too much but code is easy to read. Ancillary routines are in the other files, such as slice_trend.py, trend_2d_parallel.py, running_mean.py, mk_test.py and bootstr_confidence.py. 
 
 for all further information please refer to:
 
 Vincenzo.DeToma@artov.ismar.cnr.it
