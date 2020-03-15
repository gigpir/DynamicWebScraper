import time
from selenium import webdriver
import WineClass

driver = webdriver.Chrome('./chromedriver')  # Optional argument, if not specified will search path.
# driver.get('http://www.google.com/');
# time.sleep(5) # Let the user actually see something!
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(5) # Let the user actually see something!
# driver.quit()


driver.get('https://www.vivino.com/explore?e=eJwFwbEOQDAUBdC_uaNownhHg1WYROSpapoo8jTF3zsnKquiRgwHS0R5WZWwH9sels3Q4aKB35hFg0uy41yoksLh71myU_EOJ1d3WzxpnGh-BxEawA==');
time.sleep(5) # Let the user actually see something!

# SCROLL PAGE TILL THE END
SCROLL_PAUSE_TIME = 2.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")-1000
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight-1000);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

wines = []
names = driver.find_elements_by_class_name('vintageTitle__wine--U7t9G')
locationsAndStates = driver.find_elements_by_class_name('vintageLocation__vintageLocation--1DF0p')
avgVals = driver.find_elements_by_class_name('vivinoRatingWide__averageValue--1zL_5')
wineries = driver.find_elements_by_class_name('vintageTitle__winery--2YoIr')
nVotess = driver.find_elements_by_class_name('vivinoRatingWide__basedOn--s6y0t')
links = driver.find_elements_by_class_name('vintageTitle__vintageTitle--2iCdc')



# check if got same numbers of element. they should be already sorted correctly
if len(names)==len(locationsAndStates) and len(locationsAndStates) == len(avgVals) and len(avgVals) == len(wineries) and len(wineries) == len(nVotess) and len(links) == len(names):
    # print size of result
    print("% 2d wines found" % (len(names)))

    #fill a list of wines
    for i in range(len(names)):

        state = (locationsAndStates[i].find_elements_by_css_selector('a'))[1].text
        location = (locationsAndStates[i].find_elements_by_css_selector('a'))[2].text
        nVotes = int(nVotess[i].text.split(' ', 2)[0])
        link = links[i].find_element_by_css_selector('a').get_attribute('href')
        w = WineClass.Wine(name=names[i].text,
                           state=state,
                           location=location,
                           avgVal=float(avgVals[i].text),
                           winery=wineries[i].text,
                           nVotes=nVotes,
                           link=link)
        print(w)
        wines.append(w)

time.sleep(5) # Let the user actually see something!
driver.quit()