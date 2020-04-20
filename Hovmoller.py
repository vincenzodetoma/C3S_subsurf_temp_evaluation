import xarray as xr
import xarray.ufuncs as xu
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import cartopy.crs as ccrs
import sys
plt.rcParams.update({'font.size':18})
variable='thetao700'

surf_path='/DataArchive/C3S/subsurf_temp'

ds = xr.open_dataset(surf_path+'/Results/thetao_700m_ORCA-0.25x0.25_regular_1979_2018.nc')
var = ds[variable] - ds[variable].mean('time')
weights = np.cos(ds.lat*np.pi/180)

hov_nino = (var*weights).sel(lat=slice(-5,5), lon=slice(130, 280)).mean(dim='lat')
hov_nino = hov_nino.rename(r'$Temp~Anomalies~[^oC]$')
fig=plt.figure(1, figsize=(8,10))
ax=fig.add_subplot(111)
p = hov_nino.plot.contourf(ax=ax, 
                  extend='both',
                  cmap='RdBu_r', 
                  vmin=-1.5, vmax=1.5, levels=31,
                  cbar_kwargs={'drawedges': True, 'shrink' : 0.80})
fig.savefig(surf_path+'/Figures/'+variable+'_hovmoller_ORCA-0.25x0.25_regular_1979_2018.png', dpi=300, transparent=True)
plt.show()

