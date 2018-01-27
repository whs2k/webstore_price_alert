class Item(object):
    #object item is going to have a name, price from the web, and a url
    def __init__(self, name, price, url):
        self.name = name
        self.price = price
        self.url = url

    def __repr__(self):
        return "<Item {} with URL {}>".format(self.name, self.url)
    #don't like price