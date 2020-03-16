
class Airline:

    def __init__(self, companyName, nReviews, avgMark):
        self.companyName = companyName
        self.nReviews = nReviews
        self.avgMark = avgMark
        self.reviews = []

    def __repr__(self):

        return self.companyName +' | '+ \
        str(self.nReviews) +' | '+ \
        str(self.avgMark)

class Review:

    def __init__(self, author, flightDate, flightFromCity, flightToCity, flightType, flightClass, mark, title, text):

        self.author = author
        self.flightDate = flightDate
        self.flightFromCity = flightFromCity
        self.flightToCity = flightToCity
        self.flightType = flightType
        self.flightClass = flightClass
        self.mark = mark
        self.title = title
        self.text = text

    def __repr__(self):
        return self.author +' | '+ self.flightDate +' | '+ self.flightFromCity +' | '+ self.flightToCity +' | '+ self.flightType +' | '+ self.flightClass +' | '+ str(self.mark) +' | '+ self.title +' | '+ self.text
