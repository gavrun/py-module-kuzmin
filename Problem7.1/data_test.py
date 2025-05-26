import os

from fm_farmers import (
    read_markets_csv,
    search_by_city_state,
    search_by_zip,
    get_market,
    sort_markets
)

from fm_review import (
    load_reviews,
    save_review,
    get_reviews
)

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'farmersmarkets', 'Export.csv')

REVIEWS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'reviews.csv')


markets = read_markets_csv(DATA_FILE)
print(len(markets))

# FMID	MarketName	Website	Facebook	Twitter	Youtube	OtherMedia	street	city	County	State	zip	Season1Date	Season1Time	Season2Date	Season2Time	Season3Date	Season3Time	Season4Date	Season4Time	x	y	Location	Credit	WIC	WICcash	SFMNP	SNAP	Organic	Bakedgoods	Cheese	Crafts	Flowers	Eggs	Seafood	Herbs	Vegetables	Honey	Jams	Maple	Meat	Nursery	Nuts	Plants	Poultry	Prepared	Soap	Trees	Wine	Coffee	Beans	Fruits	Grains	Juices	Mushrooms	PetFood	Tofu	WildHarvested	updateTime
# 1018261	 Caledonia Farmers Market Association - Danville	https://www.caledoniafarmersmarket.com	https://www.facebook.com/Danville.VT.Farmers.Market/					Danville	Caledonia	Vermont	5828	06/10/2020 to 10/07/2020	Wed: 9:00 AM-1:00 PM;							-72.140337	44.411036		Y	Y	N	Y	N	Y	Y	Y	Y	Y	Y	N	Y	Y	Y	Y	Y	Y	N	N	N	Y	Y	Y	Y	N	Y	Y	Y	N	N	Y	Y	N	N	8/3/2020 3:23:12 PM

results = search_by_city_state(markets, "Danville", "Vermont")
for market in results:
    print(f"{market['FMID']}: {market['MarketName']} ({market['city']}, {market['State']})")

results = search_by_zip(markets, "5828")
for market in results:
    print(f"{market['FMID']}: {market['MarketName']} ({market['city']}, {market['State']})")

market_id = "1018261"
market = get_market(markets, market_id)
if market:
    print(f"{market['FMID']}: {market['MarketName']} ({market['city']}, {market['State']})")
else:
    print("mmhmm")

sorted_markets = sort_markets(markets, "MarketName")
for market in sorted_markets[:5]:
    print(f"{market['FMID']}: {market['MarketName']} ({market['city']}, {market['State']})")

reviews = load_reviews(REVIEWS_FILE)
print(len(reviews))

new_review = {
    'market_id': market_id,
    'name': 'Alice',
    'surname': 'Smith',
    'rating': '5',
    'review': 'Test review'
}
# save_review(REVIEWS_FILE, new_review)

reviews = load_reviews(REVIEWS_FILE)
market_reviews = get_reviews(reviews, market_id)
for review in market_reviews:
    print(f"{review['name']} {review['surname']} (Rating: {review['rating']}): {review['review']}")


# market_id	name	surname	rating	review
# 1018261	Alice	Smith	5	Test review

