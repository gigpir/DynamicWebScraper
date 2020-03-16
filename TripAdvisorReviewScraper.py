# link to Airlines list https://www.tripadvisor.it/Airlines

import time
from selenium import webdriver
import Airline

driver = webdriver.Chrome('./chromedriver')  # Optional argument, if not specified will search path.

driver.get('https://www.tripadvisor.it/Airline_Review-d8729018-Reviews-Alitalia');

time.sleep(2) # Let the user actually see something!


companyName = driver.find_element_by_class_name('flights-airline-review-page-airline-review-header-AirlineDetailHeader__airlineName--2JeT1').text

nReviews = driver.find_element_by_class_name('ui_poi_review_rating  ')
nReviews = int(nReviews.text.split(' ', 2)[0].replace('.', '', 6))

avgMark = driver.find_element_by_class_name('flights-airline-review-page-overview-module-OverviewModule__overall_rating--30Bld').text
avgMark = float(avgMark.split('\n', 2)[0].replace(',', '.', 5))

#there will be 16 boxes bcause this class references to a box that is common for reviews, photos and suggestions tabs. we care only about the first 5 indices of the following list
reviewBoxes = driver.find_elements_by_xpath('//div[@class="location-review-card-Card__ui_card--2Mri0 location-review-card-Card__card--o3LVm location-review-card-Card__section--NiAcw"]')

print(companyName)
print(nReviews)
print(avgMark)
print(len(reviewBoxes))
print(reviewBoxes[1].text)
#time.sleep(5) # Let the user actually see something!
driver.quit()