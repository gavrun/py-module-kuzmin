import zip_util
import math

# main REPL 

def main():
    zip_codes = zip_util.read_zip_all() # load zip_data

    while True:
        command = input("Command ('loc', 'zip', 'dist', 'end') => ").strip().lower()

        if command == 'end':
            print("Done")
            break
        elif command == 'loc':
            zip_code = input("Enter a ZIP Code to lookup => ").strip()
            loc_cmd(zip_code, zip_codes)
        elif command == 'zip':
            city = input("Enter a city name to lookup => ").strip()
            state = input("Enter the state name to lookup => ").strip()
            zip_cmd(city, state, zip_codes)
        elif command == 'dist':
            zip1 = input("Enter the first ZIP Code => ").strip()
            zip2 = input("Enter the second ZIP Code => ").strip()
            dist_cmd(zip1, zip2, zip_codes)
        else:
            print("Invalid command.")


# Haversine formula

def haversine(lat1, lon1, lat2, lon2):
    R = 3958.8  # Earth radius in miles
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c


# Input commands

def loc_cmd(zip_code, zip_data):
    for entry in zip_data:
        if entry[0] == zip_code:
            print(
                f"ZIP Code {zip_code} is in {entry[3]}, {entry[4]}, {entry[5]} county,\n"
                f"coordinates: ({entry[1]:07.2f}°N, {entry[2]:07.2f}°W)"
            )
            return
    
    print("ZIP Code not found.")


def zip_cmd(city, state, zip_data):
    zip_matches = [entry[0] for entry in zip_data
               if entry[3].lower() == city.lower() and entry[4].lower() == state.lower()]
    if zip_matches:
        print(f"The following ZIP Code(s) found for {city.title()}, {state.upper()}: {', '.join(zip_matches)}")
    else:
        print("City/State not found.")
    

def dist_cmd(zip1, zip2, zip_data):
    loc1 = next((entry for entry in zip_data if entry[0] == zip1), None)
    loc2 = next((entry for entry in zip_data if entry[0] == zip2), None)

    if not loc1 or not loc2:
        print("ZIP Code not found.")
        return
    
    dist = haversine(loc1[1], loc1[2], loc2[1], loc2[2])

    print(f"The distance between {zip1} and {zip2} is {dist:.2f} miles")


# main 
if __name__ == "__main__":
    main()

