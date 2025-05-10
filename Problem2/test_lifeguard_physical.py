import math
import unittest
from lifeguard_physical import convert_units, calc_result

class TestLifeguardPhysical(unittest.TestCase):

    def test_convert_units(self):
        # correctness of units conversion
        dist1_ft, hight_ft, vel_fps, theta_rad = convert_units(5, 2, 1, 30)

        self.assertAlmostEqual(dist1_ft, 15)
        self.assertAlmostEqual(hight_ft, 6)
        self.assertAlmostEqual(vel_fps, 5280 / 3600)
        self.assertAlmostEqual(theta_rad, math.radians(30))

    def test_calc_result(self):
        # correctness of time calculation (core logic)
        
        # check using the example: (5 yards, 2 yards, 3 feet, 1 mph, n=9, angle=30°)
        # verify after conversion: dist1 = 15, hight = 6, vel = 1.4667, theta = pi / 6
        dist1 = 15
        hight = 6
        dist2_ft = 3
        vel_sand = 5280 / 3600
        dec_n = 9
        theta_rad = math.radians(30)

        time = calc_result(dist1, dist2_ft, hight, vel_sand, dec_n, theta_rad)

        self.assertAlmostEqual(time, 36.4, places=1)

if __name__ == "__main__":
    unittest.main()
