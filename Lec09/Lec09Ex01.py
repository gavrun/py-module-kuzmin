import logging
import logging.handlers
import math
from zip_util import read_zip_all


EARTH_RADIUS_MILES = 3959.191


def calculate_distance(location1, location2):
    """
    This function returns the great-circle distance between location1 and
    location2.
    
    (iterable, iterable) -> float

    Parameters:
    location1 (iterable): The geographic coordinates
    of the first location. The first element of the iterable is latitude,
    the second one is longitude.

    location2 (iterable): The geographic coordinates
    of the second location. The first element of the iterable is latitude,
    the second one is longitude.

    Returns:
    float: Value of the distance between two locations computed using
    the haversine formula
    """


    lat1 = math.radians(location1[0])
    lat2 = math.radians(location2[0])
    long1 = math.radians(location1[1])
    long2 = math.radians(location2[1])
    del_lat = (lat1 - lat2) / 2
    del_long = (long1 - long2) / 2
    angle = math.sin(del_lat)**2 + math.cos(lat1) * math.cos(lat2) * \
        math.sin(del_long)**2
    distance = 2 * EARTH_RADIUS_MILES * math.asin(math.sqrt(angle))
    return distance


def degree_minutes_seconds(location):
    minutes, degrees = math.modf(location)
    degrees = int(degrees)
    minutes *= 60
    seconds, minutes = math.modf(minutes)
    minutes = int(minutes)
    seconds = 60 * seconds
    return degrees, minutes, seconds


def format_location(location):
    ns = ""
    if location[0] < 0:
        ns = 'S'
    elif location[0] > 0:
        ns = 'N'

    ew = ""
    if location[1] < 0:
        ew = 'W'
    elif location[0] > 0:
        ew = 'E'

    format_string = '{:03d}\xb0{:0d}\'{:.2f}"'
    latdegree, latmin, latsecs = degree_minutes_seconds(abs(location[0]))
    latitude = format_string.format(latdegree, latmin, latsecs)
    longdegree, longmin, longsecs = degree_minutes_seconds(abs(location[1]))
    longitude = format_string.format(longdegree, longmin, longsecs)
    return '(' + latitude + ns + ',' + longitude + ew + ')'

def location_by_zip(codes, zipcode):
    #zip_codes = '12180'
    for code in codes:
        if code[0] == zipcode:
            return tuple(code[1:])
    return ()


def zip_by_location(codes, location):
    zips = []
    for code in codes:
        if location[0].lower() == code[3].lower() and \
           location[1].lower() == code[4].lower():
            zips.append(code[0])
    return zips


def process_loc(codes):
    zipcode = input('Enter a ZIP Code to lookup => ')
    print(zipcode)
    location = location_by_zip(codes, zipcode)
    if len(location) > 0:
        print('ZIP Code {} is in {}, {}, {} county,\ncoordinates: {}'.
              format(zipcode, location[2], location[3], location[4],
                     format_location((location[0], location[1]))))
    else:
        print('Invalid or unknown ZIP Code')

def process_zip(codes):
    city = input('Enter a city name to lookup => ')
    print(city)
    city = city.strip().title()
    state = input('Enter the state name to lookup => ')
    print(state)
    state = state.strip().upper()
    zipcodes = zip_by_location(codes, (city, state))
    if len(zipcodes) > 0:
        print('The following ZIP Code(s) found for {}, {}: {}'.
              format(city, state, ", ".join(zipcodes)))
    else:
        print('No ZIP Code found for {}, {}'.format(city, state))


def process_dist(codes):
    zip1 = input('Enter the first ZIP Code => ')
    print(zip1)
    # logging.info(f'Received the first ZIP {zip1}')
    logger.info(f'Received the first ZIP {zip1}')
    zip2 = input('Enter the second ZIP Code => ')
    print(zip2)
    # logging.info(f'Received the second ZIP {zip2}')
    logger.info(f'Received the second ZIP {zip2}')

    location1 = location_by_zip(codes, zip1)
    location2 = location_by_zip(codes, zip2)
    if len(location1) == 0 or len(location2) == 0:
        print('The distance between {} and {} cannot be determined'.
              format(zip1, zip2))
    else:
        dist = calculate_distance(location1, location2)
        print('The distance between {} and {} is {:.2f} miles'.
              format(zip1, zip2, dist))

zip_codes = read_zip_all()

if __name__ == "__main__":
    
    
    # del zip_codes[3]
    # zip_codes[4108][3] = 'troy'
    # zip_codes[456][1] = None
    # zip_codes[1345][2] = 0.0
    
    assert len(zip_codes) == 42049, \
        f'The number of ZIP codes read is {len(zip_codes)} instead of 42049'
    print(zip_codes[4108])
    assert zip_codes[4108] == \
        ['12180', 42.673701, -73.608792, 'Troy', 'NY', 'Rensselaer'], \
        'Properties of ZIP 12180 are incorrect'
    print(zip_codes[42048])
    assert zip_codes[42048] == \
        ['99950', 55.542007, -131.432682, 'Ketchikan', 'AK', 'Ketchikan Gateway'], \
        'Properties of ZIP 99950 are incorrect'
    for elem in zip_codes:
        assert elem[1] is not None and elem[1] != 0.0, \
            f'Latitude of ZIP {elem[0]} is {elem[1]} which is invalid'
        assert elem[2] is not None and elem[2] != 0.0, \
            f'Latitude of ZIP {elem[0]} is {elem[2]} which is invalid'
    print('All tests passed!')
    
    rfh = logging.handlers.RotatingFileHandler(
        filename='zip_app.log',
        mode='a',
        maxBytes=100,#5*1024*1024,
        backupCount=9,
        encoding=None,
        delay=0
    )
    logging.basicConfig(format='%(asctime)s: %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO, datefmt="%y-%m-%d %H:%M:%S", handlers=[rfh])
    logger = logging.getLogger('main')
    logger2 = logging.getLogger('second_logger')
    #logger.setLevel(logging.ERROR)
    command = ""
    while command != 'end':
        command = input("Command ('loc', 'zip', 'dist', 'end') => ")
        logger.info(f'Received command {command}')
        logger2.info(f'Received command {command}')
        print(command)
        command = command.strip().lower()
        if command == 'loc':
            process_loc(zip_codes)
        elif command == 'zip':
            process_zip(zip_codes)
        elif command == 'dist':
            process_dist(zip_codes)
        elif command != 'end':
            print("Invalid command, ignoring")
    print()
print("Done")
logging.shutdown()
                