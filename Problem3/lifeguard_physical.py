# Physical (analytical) approach - Fermat's principle

import math

def get_input():
    """Input data and print back optionally"""
    dist1_yd = float(input("Enter the shortest distance between the lifeguard and the water's edge (yards): "))
    # print(dist1_yd)
    dist2_ft = float(input("Enter the shortest distance from a drowning person to the shore (feet): "))
    # print(dist2_ft)
    hight_yd = float(input("Enter the lateral offset between the lifeguard and a drowning person (yards): "))
    # print(hight_yd)
    vel_sand_mph = float(input("Enter the speed of the lifeguard on the sand (mph): "))
    # print(vel_sand_mph)
    dec_n = float(input("Enter the deceleration coefficient of the lifeguard when moving in water (const): "))
    # print(dec_n)
    theta1_deg = float(input("Enter the direction angle of the lifeguard's movement on the sand (degrees): "))
    # print(theta1_deg)

    return dist1_yd, dist2_ft, hight_yd, vel_sand_mph, dec_n, theta1_deg

def convert_units(dist1_yd, hight_yd, vel_sand_mph, theta1_deg):
    """Convert units"""
    dist1 = dist1_yd * 3  # yards > feet
    hight = hight_yd * 3  
    vel_sand = vel_sand_mph * 5280 / 3600  # miles per hour > feet per second
    theta1_rad = math.radians(theta1_deg)

    return dist1, hight, vel_sand, theta1_rad

def calc_result(dist1, dist2_ft, hight, vel_sand, dec_n, theta1_rad):
    """Calculate the result"""
    x_path = dist1 * math.tan(theta1_rad)
    L1 = math.sqrt(x_path ** 2 + dist1 ** 2 )
    L2 = math.sqrt((hight - x_path) ** 2 + dist2_ft ** 2)
    time = (L1 + dec_n * L2) / vel_sand

    return time

def find_angle(dist1, dist2_ft, hight, vel_sand, dec_n):
    best_angle = 0
    best_time = float(9999999)
    for angle in range(0, 90): # 0..89 deg
        theta1_rad = math.radians(angle)
        temp_time = calc_result(dist1, dist2_ft, hight, vel_sand, dec_n, theta1_rad)
        if temp_time < best_time:
            best_time = temp_time
            best_angle = angle
    return best_angle, best_time

def print_result(theta1_deg, time):
    """Output the result"""
    print(f"\nIf the lifeguard starts moving at an angle {int(round(theta1_deg))} degrees,"
        f" he will reach a drowning person in {round(time, 1)} seconds")

def print_best_result(angle, time):
    """Output the best result"""
    print(f"\nThe lifeguard better start moving at an angle {int(round(angle))} degrees,"
        f" to reach a drowning person in shortest {round(time, 1)} seconds")
    
# Main
if __name__ == "__main__":
    dist1_yd, dist2_ft, hight_yd, vel_sand_mph, dec_n, theta1_deg = get_input()

    dist1, hight, vel_sand, theta1_rad = convert_units(dist1_yd, hight_yd, vel_sand_mph, theta1_deg)

    time = calc_result(dist1, dist2_ft, hight, vel_sand, dec_n, theta1_rad)

    best_angle, best_time = find_angle(dist1, dist2_ft, hight, vel_sand, dec_n)

    print_result(theta1_deg, time)

    print_best_result(best_angle, best_time)
