import xarray as xr
import xarray.ufuncs as xu
import numpy as np
import matplotlib.pyplot as plt
import sys
plt.rcParams.update({'font.size':14})

variable=sys.argv[1]
section=sys.argv[2]

surf_path='/DataArchive/C3S/subsurf_temp'

ds = xr.open_dataset(surf_path+'/Results/pvalue_'+variable+'_'+section+'_ORCA-0.25x0.25_regular_1979_2018.nc')
var = ds[variable+'_trend_pvalue'].squeeze().rename(variable+' pvalue % ')
colors='Greens'
if(section=='A3'):
  xname = 'loongitude'
else:
  xname = 'latitude'

mask = xu.isnan(var)
fig = plt.figure(1, figsize=(15,8))
ax = fig.add_subplot(211)
p = var.sel(depth=slice(0,1000)).plot.contourf(ax=ax, cmap=colors, vmin=0., vmax=100., extend='both', levels=21, cbar_kwargs={'drawedges': True, 'shrink' : 1.})
mask.sel(depth=slice(0,1000)).plot.contour(ax=ax, colors='k', levels=1)
ax.set_xlabel(xname)
ax.invert_yaxis()
ax2 = fig.add_subplot(212)
p2 = var.plot.contourf(ax=ax2, cmap=colors, vmin=0., vmax=100., extend='both', levels=21, cbar_kwargs={'drawedges': True, 'shrink' : 1.})
mask.plot.contour(ax=ax2, colors='k',levels=1)
ax2.set_xlabel(xname)
ax2.invert_yaxis()
fig.tight_layout()
fig.savefig(surf_path+'/Figures/'+'pval_'+variable+'_'+section+'_ORCA-0.25x0.25_regular_1979_2018.png', transparent=True, dpi=300)
plt.show()
