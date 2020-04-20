import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs
import sys
plt.rcParams.update({'font.size':14})
variable=sys.argv[1]
depth=sys.argv[2]
surf_path='/DataArchive/C3S/subsurf_temp'

ds = xr.open_dataset(surf_path+'/Results/'+'glob_'+variable+'_'+depth+'m_ORCA-0.25x0.25_regular_1979_2018.nc')
var = ds[variable+depth]

fig = plt.figure(1, figsize=(15,8))
ax = fig.add_subplot(111)
p = var.plot(ax=ax, color='k')
fig.savefig(surf_path+'/Figures/globmean_'+variable+'_'+depth+'m_ORCA-0.25x0.25_regular_1979_2018.png', dpi=300, transparent=True)
