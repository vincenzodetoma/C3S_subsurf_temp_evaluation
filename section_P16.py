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

section_P16 = var.sel(lon=-150.125, lat=slice(-60,60)).rename(variable)
section_P16.to_netcdf(dest_path+'tmp/'+year+'/'+variable+'_P16_ORCA-0.25x0.25_regular_'+year+month+'.nc')

ds.close()

