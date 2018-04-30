# Spotlight: A Data Accountability Tool for Citizens

This repository contains the data and code used to build https://spotlight-data.github.io/index.html. s

Check out our visualizations at https://spotlight-data.github.io/vis.html.

## The Question

**How do we quantitatively evaluate data transparency in local governments?** 

The Obama administration brought attention to Open Data in the United States by creating the Memorandum on Transparency and Open Government, which states, Information maintained by the Federal Government is a national asset. My Administration will take appropriate action, consistent with law and policy, to disclose information rapidly in forms that the public can readily find and use. The Digital Accountability and Transparency Act, signed in 2014, aims to increase access to information on federal expenditures and has led to the creation of nationwide open data platforms such as data.gov. While this is a major step forward, the law does not mandate such transparency at the state and local level. Since open data is vital in evaluating the effectiveness of public officials and holding them accountable, we wanted to analyze how “open” data at the local level is.

## Methodology 

Based on a meeting with the city of Berkeley IT department and research on government open data policies we determined five key categories that we could use to compare the open data platforms of different local governments in the Bay Area — quantity, recency, accessibility, breadth and quality.

To select the cities to compare, we decided to focus on the governments which use Socrata. Socrata is a software company which many cities use to power their open data platforms, including San Francisco and Oakland. Next, we considered various statistics we could collect about each city’s data platform, and how these could inform our metrics.

Having decided on a set of cities and metrics by which to assess them, we built a collection of web-scraping algorithms. These deterministically searched from the navigation page of an open data platform, “clicking” every possible link and checking to see if the link fulfills the “dataset” criterion. We applied Regular Expressions (RegEx) on each webpage’s source code and link to guide the scraper’s search.

Once we had a list of links to the datasets published by each city, we were able to extract more information from the corresponding JSON (Javascript Object Notation) files. Our scripts extracted relevant information from the metadata section of each file, such as view count and recency.

Finally, we organized these statistics by city and dataset and wrote our results to files for further analysis. We discuss our analytical methods below.

See https://spotlight-data.github.io/methodology.html for more details. 

## Team Members 

Aura Barrera, Clara de Martel, Ameet Rahane, and Akhil Jalan.

## Acknowledgments 

We conducted this project as part of the Data for Good Competition in UC Berkeley's Center for Technology, Society, and Policy (CTSP). We thank Daniel Griffin and Elaine Sedenberg for their advice and support. 