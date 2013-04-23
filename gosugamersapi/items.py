from scrapy.item import Item, Field

class GosugamersapiItem(Item):
    game = Field()
    playerOne = Field()
    playerOneCountry = Field()
    playerTwo = Field()
    playerTwoCountry = Field()
    tournament = Field()
    time = Field()
