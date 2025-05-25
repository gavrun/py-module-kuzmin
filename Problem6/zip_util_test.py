# https://simplemaps.com/data/us-zips

# zip	lat	lng	city	state_id	state_name	zcta	parent_zcta	population	density	county_fips	county_name	county_weights	county_names_all	county_fips_all	imprecise	military	timezone
# 601	18.18027	-66.75266	Adjuntas	PR	Puerto Rico	TRUE		16721	100.2	72001	Adjuntas	{"72001": 98.74, "72141": 1.26}	Adjuntas|Utuado	72001|72141	FALSE	FALSE	America/Puerto_Rico

# `zip`         
# `lat`, `lng`  
# `city`        
# `state_id`    
# `county_name` 

import zip_util

zip_codes = zip_util.read_zip_all()

print(zip_codes[0])
print(zip_codes[4108])

# ['00601', 18.18027, -66.75266, 'Adjuntas', 'PR', 'Adjuntas']
# ['14202', 42.88798, -78.88358, 'Buffalo', 'NY', 'Erie']
