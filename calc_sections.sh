#!/bin/bash

subsurf_dir=/DataArchive/C3S/subsurf_temp
var=thetao

#for (( y=1979;y<=2018;y++ ));do
#  mkdir -p ${subsurf_dir}/tmp/${y}
#  for (( m=1;m<=12;m++ ));do
#    python section_A3.py ${var} ${y} `printf "%02d" ${m}`
#    python section_P16.py ${var} ${y} `printf "%02d" ${m}`
#    python section_IR06.py ${var} ${y} `printf "%02d" ${m}`
#    python section_I06.py ${var} ${y} `printf "%02d" ${m}`
#    python section_A21.py ${var} ${y} `printf "%02d" ${m}`
#    python section_S3.py ${var} ${y} `printf "%02d" ${m}`
#  done
#done
cdo mergetime ${subsurf_dir}/tmp/*/${var}_A3_ORCA-0.25x0.25_regular_*.nc ${subsurf_dir}/Results/${var}_A3_ORCA-0.25x0.25_regular_1979_2018.nc
cdo mergetime ${subsurf_dir}/tmp/*/${var}_P16_ORCA-0.25x0.25_regular_*.nc ${subsurf_dir}/Results/${var}_P16_ORCA-0.25x0.25_regular_1979_2018.nc
cdo mergetime ${subsurf_dir}/tmp/*/${var}_IR06_ORCA-0.25x0.25_regular_*.nc ${subsurf_dir}/Results/${var}_IR06_ORCA-0.25x0.25_regular_1979_2018.nc
cdo mergetime ${subsurf_dir}/tmp/*/${var}_I06_ORCA-0.25x0.25_regular_*.nc ${subsurf_dir}/Results/${var}_I06_ORCA-0.25x0.25_regular_1979_2018.nc
cdo mergetime ${subsurf_dir}/tmp/*/${var}_A21_ORCA-0.25x0.25_regular_*.nc ${subsurf_dir}/Results/${var}_A21_ORCA-0.25x0.25_regular_1979_2018.nc
cdo mergetime ${subsurf_dir}/tmp/*/${var}_S3_ORCA-0.25x0.25_regular_*.nc ${subsurf_dir}/Results/${var}_S3_ORCA-0.25x0.25_regular_1979_2018.nc







