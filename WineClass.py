class Review:
    def __init__(self):
        self.author = None
        self.vote = None
        self.text = None


class Wine:

    def __init__(self, name, state, location, avgVal, winery, nVotes, link):
        self.name = name
        self.state = state
        self.location = location
        self.avgVal = avgVal
        self.winery = winery
        self.nVotes = nVotes
        self.link = link
        self.reviews = []

    def __repr__(self):
        return self.name + ' | ' + self.state + ' | ' + self.location + ' | ' + \
               str(self.avgVal) + ' | ' + self.winery + ' | ' + str(self.nVotes) + ' | ' + self.link
