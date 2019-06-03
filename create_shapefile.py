import os
import glob
import zipfile
import pandas as pd
import geopandas as gpd

base_folder = 'geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_de_setores_censitarios__divisoes_intramunicipais/censo_2000/setor_urbano/'
tmp_folder = f'{base_folder}/tmp/'
output_folder = ''
states = []

# download shapefiles
print(os.popen(f'wget -nc -r ftp://{base_folder}').read())

# extract all zips
zips = glob.glob(f'{base_folder}/**/*.zip', recursive=True)
len(zips)
for zip in zips:
    with zipfile.ZipFile(f'{zip}', 'r') as zip_ref:
        zip_ref.extractall(tmp_folder)

# check projection files
prjs = glob.glob(f'{tmp_folder}/*.PRJ')
txts = []
for prj in prjs:
    txt = open(prj).read()
    txts.append(txt)
list(set(txts))

# merge shapefiles, correct projection
# geopandas (actually, fiona) reads the prj files to wrong projections
# it looks like a problem with the prj files format, so we'll fix it manually
crs_corrected = {
    # from : to
    'epsg:32618': 'epsg:32718',
    'epsg:32619': 'epsg:32719',
    'epsg:32620': 'epsg:32720',
    'epsg:32621': 'epsg:32721',
    'epsg:32622': 'epsg:32722',
    'epsg:32623': 'epsg:32723',
    'epsg:32624': 'epsg:32724',
    'epsg:32625': 'epsg:32725',
}
shps = glob.glob(f'{tmp_folder}/*.SHP')
len(shps)
frames = []
for shp in shps:
    gdf = gpd.read_file(shp)
    # correct projections
    for from_crs in crs_corrected.keys():
        if gdf.crs['init'] == from_crs:
            gdf.crs['init'] = crs_corrected[from_crs]
    # change projections to 4326
    gdf = gdf.to_crs({'init': 'epsg:4326'})
    frames.append(gdf)

# merge to single country shapefile
country = pd.concat(frames)
country.rename(columns={'ID_': 'CD_GEOCODI'}, inplace=True)
country['CD_UF'] = country['CD_GEOCODI'].str[:2]
country.head()

# export shapefile
country.to_file('br_set_cens_2000/br_set_cens_2000.shp')
