# Shapefiles Setores Censitários - Censo 2000

O Censo 2000 disponibiliza os shapefiles com um arquivo zip por município, cada zip com um ou mais setores censitários. Além disso, as projeções variam entre municípios e estados.

Neste repositório há um arquivo shapefile unificado com *todos setores censitários urbanos* do Brasil (`br_set_cens_2000/br_set_cens_2000_4326.zip`) em projeção [WGS84 EPSG:4326](https://spatialreference.org/ref/epsg/4326/).

![Setores Censitários na RMSP](setores_censitarios_rmsp.png)
Exemplo dos setores censitários da região metropolitana de São Paulo. Visualizado no [QGIS](https://www.qgis.org/), tiles por contribuidores [OpenStreetMap](https://www.openstreetmap.org/).

## Recriando o arquivo

O processo de criação desse shapefile unificado pode ser reproduzido com `python create_shapefile.py`.
