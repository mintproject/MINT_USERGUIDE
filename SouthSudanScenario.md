<img src="https://mintproject.github.io/MINT_USERGUIDE/Figures/mint-logo-vertical.png" width="100">

# Examining precipitation data

**Question 1a:** What is the precipitation forecast for the 2017 growing season in the Pongo Basin area?

**Question 1b**: How does the precipitation forecast compare with historical precipitation data for the 2017 growing season in the Pongo Basin area?

Default:
* dataset_source: FLDAS
* max_lat: 9.335303
* max_lon: 27.74012
* max_month: 8
* min_lat: 6.700375
* min_lon: 24.15234
* min_month: 5
* weather: FLDAS_NOAH01_C_EA_M_001.tar.gz
* year: 2017

**Question 1c**: What would the precipitation prediction be if we assume a 60% increase over normal conditions in the Pongo Basin area?

Default:
* daily_weather: FLDAS_NOAH01_A_EA_D_001.tar.gz
* flagP: Rainf_f_tavg
* level: 0.7
* max_lat: 9.335303
* max_lon: 27.74012
* max_month: 8
* min_lat: 6.700375
* min_lon: 24.15234
* mont_month: 5
* monthly_weather: FLDAS_NOAH01_C_EA_M_001.tar.gz

# Relationship between precipitation and flooding

**Question 2a**: What is the water runoff in the Pongo Basin area of South Sudan during the 2017 growing season?
- Driving variable: precipitation
- Response variable: Surface runoff

Defaults:
 * FLDAS daily data.
 * Start date: 2017-01-01
 * End Date: 2017-12-31

**Question 2b**: Can we expect flooding in the Pongo Basin area of South Sudan during the lean season of 2017?  
- Driving variable: precipitation
- Response variable: Flooding
Same requirements as before

Defaults:
* Flooding threshold: 0.1

**Question 2c**: What are the roads/vegetation/population in the flooded region?

Same requirements as before


**Question 2d**: What are the maximum river water levels in the previous years in the flooded region?
- Driving variable: precipitation
- Response variable: river water levels

Defaults: 
* Basin id: 100. 
* Start date: 2016-01-01
* End date: 2017-03-31
* Numsamples: 3.

# Relationship between precipitation and crop theoretical yield

**Question 3a:** Given the precipitation forecast, what are the predicted theoretical yields for sorghum and maize in the lean season 2017?
- Driving variable: precipitation
- Response variable: theoretical yields

Suggested values: (day1: 100, duration 10; day2:225, duration:10)

**Question 3b:** Given the precipitation forecast, would changing planting dates improve the theoretical yields for sorghum and maize in the lean season 2017?
- Driving variable: precipitation
- Response variable: theoretical yields
- Intervention: Planting dates (suggested value: day1: 85, duration 15; day2:162, duration:29)

# Relationship between precipitation and crop production

**Question 4a**: How will crop production be impacted by precipitation in the 2017 lean season?
- Driving variable: precipitation
- Response variable: crop production

**Question 4b**: Would giving subsidies to farmers mitigate the impact of the precipitation forecast in the 2017 lean season?
- Driving variable: precipitation
- Response variable: crop production
- Intervention: subsidies
