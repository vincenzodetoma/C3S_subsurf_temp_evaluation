import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
from mk_test import mk_test
from trend_2d_parallel import trend_2d_parallel
from statsmodels.tsa.seasonal import seasonal_decompose
import sys
plt.rcParams.update({'font.size':14})

variable=sys.argv[1]
section=sys.argv[2]

surf_path='/DataArchive/C3S/subsurf_temp'

ds = xr.open_dataset(surf_path+'/Results/'+variable+'_'+section+'_ORCA-0.25x0.25_regular_1979_2018.nc')


depth=ds.depth
if(section=='A3'):
  var2 = ds.lon
else:
  var2 = ds.lat

time = ds.time
var = ds[variable]

frequency = 12*2 #12=months; 2=years
nsplit = 16
trend_matrix, trend_pvalue, trend_significance = trend_2d_parallel(var.fillna(0), var.fillna(0), depth, var2, time, var[0,0,0], frequency, nsplit)
trend_matrix = xr.DataArray(trend_matrix,
                            coords={'depth': depth, str(var2.name) :var2},
                            dims=['depth', str(var2.name)])

trend_pvalue = xr.DataArray(trend_pvalue,
                            coords={'depth': depth, str(var2.name) :var2},
                            dims=['depth', str(var2.name)])

mask = trend_pvalue / trend_pvalue #create the mask
trend_pvalue = trend_pvalue / mask
trend_matrix = trend_matrix.rename(variable+'_trend_matrix')
trend_pvalue = trend_pvalue.rename(variable+'_trend_pvalue')

trend_matrix.to_netcdf(surf_path+'/Results/'+'trend_'+variable+'_'+section+'_ORCA-0.25x0.25_regular_1979_2018.nc')
trend_pvalue.to_netcdf(surf_path+'/Results/'+'pvalue_'+variable+'_'+section+'_ORCA-0.25x0.25_regular_1979_2018.nc')

