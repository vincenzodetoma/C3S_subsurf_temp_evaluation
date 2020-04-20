#!/bin/bash
echo "began!!!"
./calc_vert_mean.sh
./make_meanmaps.sh
./calc_glob_mean.sh
./make_globalmeans.sh
./make_stdmaps.sh
./calc_sections.sh
./make_section_trends.sh
./make_section_figures.sh
./make_trends.sh
./make_trend_figures.sh
echo "Finished!!!"
