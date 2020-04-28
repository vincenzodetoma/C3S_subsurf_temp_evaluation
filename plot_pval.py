import xarray as xr
import xarray.ufuncs as xu
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import cartopy.crs as ccrs
import sys
plt.rcParams.update({'font.size':18})
variable=sys.argv[1]
restofname=sys.argv[2]
depth=sys.argv[3]

surf_path='/DataArchive/C3S/subsurf_temp'

ds = xr.open_dataset(surf_path+'/Results/'+'pvalue_'+variable+'_'+depth+'_ORCA-0.25x0.25_regular_1979_2018.nc')
var = ds[variable+restofname]
meanvar = var.rename(variable+' pvalue % ')

palette='Greens'

fig = plt.figure(1, figsize=(15,8))
ax = fig.add_subplot(111, projection=ccrs.PlateCarree())
p = meanvar.plot.contourf(ax=ax, 
                 transform=ccrs.PlateCarree(),
                 extend='both',
                 vmin=0., vmax=100.,
                 #norm=colors.LogNorm(vmin=meanvar.min(), vmax=meanvar.max()),
                 cmap=palette,
                 levels=21,
                 cbar_kwargs={'shrink' : 0.65, 'drawedges': True})
ax.coastlines('50m')
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True)
gl.xlabels_top = False
gl.ylabels_right = False
fig.savefig(surf_path+'/Figures/'+variable+'_pval_'+depth+'_ORCA-0.25x0.25_regular_1979_2018.png', dpi=300, transparent=True)
plt.show()


