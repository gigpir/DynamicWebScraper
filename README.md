# VivinoBasicWineWebScraper.py
Python script that retrieves basic wine info from dynamic vivino webpage like this one https://www.vivino.com/explore?e=eJzLLbI1UcvNzLM1VstNrLA1NFBLrrT1DFFLtnUNDVIrsDVUS0-zLUssykwtScxRy0-yLUosycxLL45PLEstSkxPVcu3TUktTlYrL4mOBSoGU0YAqSQclQ== .

# Requirements
This project, in order to use dynamic web scraping features, needs [Selenium] and a [driver] for the browser you want to use.
This project contains already a chromedriver for Chrome version 80. To know your Chrome version type chrome://settings/help in your Chrome search bar.

# Instructions
Run scraperv3.py


# TripAdvisorReviewScraper.py
Dynamic web scraping from Flight Company page of tripadvisor.it

use with python3
```
usage: TripAdvisorReviewScraper.py [-h] [--company-link [COMPANY_LINK]]
                                   [--max-rev [MAX_REV]] [--csv]

optional arguments:
  -h, --help            show this help message and exit
  --company-link [COMPANY_LINK]
                        paste the trip advisor link of the company you want to
                        know about
  --max-rev [MAX_REV]   max reviews to scrape, set to 50 default
  --csv                 to produce a csv file
```
Command line example:
```
python3 TripAdvisorReviewScraper.py --company-link https://www.tripadvisor.it/Airline_Review-d8729074-Reviews-Etihad-Airways  --csv --max-rev 150
```
 