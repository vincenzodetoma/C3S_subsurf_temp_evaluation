import xarray as xr
import sys
variable=sys.argv[1]
year=sys.argv[2]
month=sys.argv[3]
data_path='/DataArchive/C3S/ORAS5/REGULAR/opa0/'
dest_path = '/DataArchive/C3S/subsurf_temp/'
ds = xr.open_dataset(data_path+variable+'/'+variable+'_ORCA-0.25x0.25_regular_'+year+month+'.nc')
ds.coords['lon'] = (ds.coords['lon'] + 180) % 360 - 180
ds = ds.sortby(ds.lon)
var = ds[variable]

section_A3 = var.sel(lat=36.125, lon=slice(-75,-5)).rename(variable)
section_A3.to_netcdf(dest_path+'tmp/'+year+'/'+variable+'_A3_ORCA-0.25x0.25_regular_'+year+month+'.nc')

ds.close()

