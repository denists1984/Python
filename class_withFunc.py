class Store():
    open = 8
    close = 20
    
    def hours(self):
        return "We're open from {} to {}".format(self.open, self.close)
