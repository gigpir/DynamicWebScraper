# link to Airlines list https://www.tripadvisor.it/Airlines

import time
from selenium import webdriver
import Airline
import argparse
# Some functions
def scapeReviewsFromReviewBox(reviewBoxes):
    reviews = []
    for i in range(5):
        author = reviewBoxes[i].find_element_by_css_selector(
            'a.social-member-event-MemberEventOnObjectBlock__member--35-jC').text

        flightDate = reviewBoxes[i].find_elements_by_css_selector(
            'span.location-review-review-list-parts-EventDate__event_date--1epHa')

        # optional review attribute replace null if no exist
        if len(flightDate) != 0:
            flightDate = flightDate[0].text.replace('Data del viaggio: ', '', 2)
        else:
            flightDate = 'NULL'

        # grab flight labels like trip, type of the flight, type of the flight
        labels = reviewBoxes[i].find_elements_by_css_selector(
            'div.location-review-review-list-parts-RatingLine__labelBtn--e58BL')

        flightFromCity = labels[0].text.split(' - ', 2)[0]
        flightToCity = labels[0].text.split(' - ', 2)[1]
        flightType = labels[1].text
        flightClass = labels[2].text

        # retrieve title of the review
        title = reviewBoxes[i].find_element_by_css_selector(
            'a.location-review-review-list-parts-ReviewTitle__reviewTitleText--2tFRT').text

        # expand text all boxes (always present)
        if i == 0:
            reviewBoxes[i].find_element_by_css_selector(
                'span.location-review-review-list-parts-ExpandableReview__cta--2mR2g').click()


        # retrieve text of the review
        text = reviewBoxes[i].find_element_by_css_selector(
            'q.location-review-review-list-parts-ExpandableReview__reviewText--gOmRC').text
        # remove new line characters and other junk
        text = text.replace('<br>', ' ')
        text = text.replace('\n', ' ')
        # get the class of the number of bubble MARK
        mark = str(reviewBoxes[i].find_element_by_css_selector('span.ui_bubble_rating').get_attribute('class'))
        # parse the class text
        mark = float(mark.split('_', 20)[-1]) / 10

        review = Airline.Review(author=author,
                                flightDate=flightDate,
                                flightFromCity=flightFromCity,
                                flightToCity=flightToCity,
                                flightType=flightType,
                                flightClass=flightClass,
                                mark=mark,
                                title=title,
                                text=text)

        reviews.append(review)

    return reviews



def main(args):

    driver = webdriver.Chrome('./chromedriver')  # Optional argument, if not specified will search path.

    driver.get(args.company_link);

    time.sleep(2)  # Let the user actually see something!

    companyName = driver.find_element_by_class_name(
        'flights-airline-review-page-airline-review-header-AirlineDetailHeader__airlineName--2JeT1').text

    nReviews = driver.find_element_by_class_name('ui_poi_review_rating  ')
    nReviews = int(nReviews.text.split(' ', 2)[0].replace('.', '', 6))

    avgMark = driver.find_element_by_class_name(
        'flights-airline-review-page-overview-module-OverviewModule__overall_rating--30Bld').text
    avgMark = float(avgMark.split('\n', 2)[0].replace(',', '.', 5))


    print(companyName)
    print(nReviews)
    print(avgMark)

    airline = Airline.Airline(companyName=companyName,
                              nReviews=nReviews,
                              avgMark=avgMark)

    #iterate over the pages
    while len(airline.reviews)<nReviews and len(airline.reviews) < args.max_rev:

        # there will be 16 boxes bcause this class references to a box that is common for reviews, photos and suggestions tabs. we care only about the first 5 indices of the following list
        reviewBoxes = driver.find_elements_by_xpath(
            '//div[@class="location-review-card-Card__ui_card--2Mri0 location-review-card-Card__card--o3LVm location-review-card-Card__section--NiAcw"]')

        airline.reviews.extend(scapeReviewsFromReviewBox(reviewBoxes))

        #driver.find_element_by_xpath(
        #    '//a[@class="ui_button nav next primary"]').click()
        driver.find_element_by_link_text('Avanti').click()
        time.sleep(1)

    print(airline)

    for r in airline.reviews:
        print(r)

    if args.csv:
        import csv
        data_list = [['author',
                      'flightDate',
                      'flightFromCity',
                      'flightToCity',
                      'flightType',
                      'flightClass',
                      'mark',
                      'title',
                      'text'
                      ]]
        with open(airline.companyName+'_'+str(len(airline.reviews))+'_of_'+str(airline.nReviews)+'_'+str(airline.avgMark)+'.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter='|')
            writer.writerows(data_list)
            writer.writerows(airline.getListReviews())

    # time.sleep(5) # Let the user actually see something!
    driver.quit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--company-link", type=str, help="paste the trip advisor link of the company you want to know about",
                        nargs='?', default='https://www.tripadvisor.it/Airline_Review-d8729018-Reviews-Alitalia', const=0)
    parser.add_argument("--max-rev", type=int, help="max reviews to scrape, set to 50 default",
                        nargs='?', default='50', const=0)
    parser.add_argument("--csv", dest='csv', action='store_true', default=False, help="to produce a csv file")

    args = parser.parse_args()

    main(args)
