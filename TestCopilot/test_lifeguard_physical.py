import unittest
from lifeguard_physical import convert_units
from lifeguard_physical import calc_result

class TestConvertUnits(unittest.TestCase):
    def test_convert_units(self):
        
        # Test case 1: Standard input values
        dist1_yd = 10
        hight_yd = 5
        vel_sand_mph = 6
        theta1_deg = 45
        expected_dist1 = 30  # 10 yards * 3
        expected_hight = 15  # 5 yards * 3
        expected_vel_sand = 8.8  # 6 mph * 5280 / 3600
        expected_theta1_rad = 0.7853981633974483  # radians(45)
        result = convert_units(dist1_yd, hight_yd, vel_sand_mph, theta1_deg)
        self.assertAlmostEqual(result[0], expected_dist1)
        self.assertAlmostEqual(result[1], expected_hight)
        self.assertAlmostEqual(result[2], expected_vel_sand, places=1)
        self.assertAlmostEqual(result[3], expected_theta1_rad, places=5)

        # Test case 2: Zero values
        dist1_yd = 0
        hight_yd = 0
        vel_sand_mph = 0
        theta1_deg = 0
        expected_dist1 = 0
        expected_hight = 0
        expected_vel_sand = 0
        expected_theta1_rad = 0
        result = convert_units(dist1_yd, hight_yd, vel_sand_mph, theta1_deg)
        self.assertEqual(result[0], expected_dist1)
        self.assertEqual(result[1], expected_hight)
        self.assertEqual(result[2], expected_vel_sand)
        self.assertEqual(result[3], expected_theta1_rad)

        # Test case 3: Negative values
        dist1_yd = -10
        hight_yd = -5
        vel_sand_mph = -6
        theta1_deg = -45
        expected_dist1 = -30  # -10 yards * 3
        expected_hight = -15  # -5 yards * 3
        expected_vel_sand = -8.8  # -6 mph * 5280 / 3600
        expected_theta1_rad = -0.7853981633974483  # radians(-45)
        result = convert_units(dist1_yd, hight_yd, vel_sand_mph, theta1_deg)
        self.assertAlmostEqual(result[0], expected_dist1)
        self.assertAlmostEqual(result[1], expected_hight)
        self.assertAlmostEqual(result[2], expected_vel_sand, places=1)
        self.assertAlmostEqual(result[3], expected_theta1_rad, places=5)

class TestCalcResult(unittest.TestCase):
    def test_calc_result(self):
        
        # Test case 1: Standard input values
        dist1 = 30
        dist2_ft = 50
        hight = 15
        vel_sand = 8.8
        dec_n = 1.5
        theta1_rad = 0.7853981633974483  # radians(45)
        expected_time = 10.2  # Approximate expected time
        result = calc_result(dist1, dist2_ft, hight, vel_sand, dec_n, theta1_rad)
        self.assertAlmostEqual(result, expected_time, places=1)

        # Test case 2: Zero values
        dist1 = 0
        dist2_ft = 0
        hight = 0
        vel_sand = 1  # Avoid division by zero
        dec_n = 1
        theta1_rad = 0
        expected_time = 0
        result = calc_result(dist1, dist2_ft, hight, vel_sand, dec_n, theta1_rad)
        self.assertEqual(result, expected_time)

        # Test case 3: Negative values
        dist1 = -30
        dist2_ft = -50
        hight = -15
        vel_sand = 8.8
        dec_n = 1.5
        theta1_rad = -0.7853981633974483  # radians(-45)
        with self.assertRaises(ValueError):  # Negative distances might raise an error
            calc_result(dist1, dist2_ft, hight, vel_sand, dec_n, theta1_rad)

        # Test case 4: Large values
        dist1 = 1000
        dist2_ft = 2000
        hight = 500
        vel_sand = 15
        dec_n = 2
        theta1_rad = 0.5235987755982988  # radians(30)
        expected_time = 300.0  # Approximate expected time
        result = calc_result(dist1, dist2_ft, hight, vel_sand, dec_n, theta1_rad)
        self.assertAlmostEqual(result, expected_time, places=1)

if __name__ == "__main__":
    unittest.main()
    