class Art:
    def __init__(self, artist, title, medium, year, owner):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner

    def __repr__(self):
        return "{artist}. \"{title}\". {year}, {medium}. {owner}, " \
               "{location}.".format(
            artist=self.artist,
            title=self.title,
            year=self.year,
            medium=self.medium,
            owner=self.owner.name,
            location=self.owner.location
            )


class Marketplace:
    def __init__(self):
        self.listings = []

    def add_listing(self, new_listing):
        self.listings.append(new_listing)

    def remove_listings(self, listing_to_remove):
        self.listings.remove(listing_to_remove)
        print("this is working now, finally")

    def show_listings(self):
        for listing in self.listings:
            print(listing)


class Client:
    def __init__(self, name, location, is_museum):
        self.name = name
        if location == "":
            self.location = "Private Collection"
        else:
            self.location = location
        if is_museum == True:
            self.is_museum = "Museum"
        elif is_museum == False:
            self.is_museum = "Collector"

    def sell_artwork(self, artwork, price):
        if artwork.owner == self:
            new_listing = Listing(artwork, price, self)
            veneer.add_listing(new_listing)

    def buy_artwork(self, artwork):
        if artwork.owner != self:
            for listing in veneer.listings:
                if artwork == listing.art:
                    veneer.remove_listings(listing)
                    artwork.owner = self


class Listing:
    def __init__(self, art, price, seller):
        self.art = art
        self.price = price
        self.seller = seller

    def __repr__(self):
        return "{name}, {price}".format(name=self.art.title, price=self.price)


veneer = Marketplace()
print(veneer.show_listings())

edytta = Client("Edytta Halpirt", "", False)
moma = Client("The MOMA", "New York", True)

girl_with_mandolin = Art("Picasso, Pablo",
                         "Girl with a Mandolin (Fanny Tellier)",
                         "oil on canvas", 1910, edytta)
print(girl_with_mandolin)

edytta.sell_artwork(girl_with_mandolin, "$6M (USD)")
veneer.show_listings()

moma.buy_artwork(girl_with_mandolin)
print(girl_with_mandolin)
print(veneer.show_listings())
