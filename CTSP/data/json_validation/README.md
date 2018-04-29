# Data Quality via JSON Validation

## Explanation 

Project Open Data was founded in the second Obama administration to provide tools for data transparency and accountability for federal agencies. Their website offers a tool for JSON validation, which examines the metadata of a file to see if it is in accordance with federal standards. We evaluated data files for 6 cities in the Bay Area, checking against the Non-Federal Scheme version 1.1. We found that none of the cities passed the test. 

Interestingly, the error results for these 6 cities were identical (with the exception of dataset length). What all of these cities have in common is that their open data platforms are powered by Socrata. From this we conclude that while Socrata enforces a JSON metadata format for all datasets in its open data portals, this format has serious errors and does not meet federal government standards, even for non-federal government. 

## Check for yourself 

The tool for JSON validation is here: https://labs.data.gov/dashboard/validate

Here are the links we tested as a representative sample. Except for 502 bad gateway errors, other datasets on these cities' open data platforms had the same results.

Berkeley: https://data.cityofberkeley.info/api/views/7a6r-v8mp/rows.json?accessType=DOWNLOAD
Menlo Park: https://data.menlopark.org/api/views/m8ww-9sgn/rows.json?accessType=DOWNLOAD
Oakland: https://data.oaklandnet.com/api/views/wm75-yhqe/rows.json?accessType=DOWNLOAD
Richmond: https://data.richmondgov.com/api/views/km2h-uk82/rows.json?accessType=DOWNLOAD
Santa Rosa: https://data.srcity.org/api/views/vsiv-m696/rows.json?accessType=DOWNLOAD
San Francisco: https://data.sfgov.org/api/views/v94x-pf9r/rows.json?accessType=DOWNLOAD
