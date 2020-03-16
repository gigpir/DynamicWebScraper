
class Airline:

    def __init__(self, companyName, nReviews, avgMark):
        self.companyName = companyName
        self.nReviews = nReviews
        self.avgMark = avgMark
        self.reviews = []


class Review:

    def __init__(self, author, date, flightFromCity, flightToCity, flightType, flightClass, mark, title, text):

        self.author = author
        self.date = date
        self.flightFromCity = flightFromCity
        self.flightToCity = flightToCity
        self.flightType = flightType
        self.flightClass = flightClass
        self.mark = mark
        self.title = title
        self.text = text

