# integration unit test

import unittest
import subprocess

class TestLifeguardPhysical(unittest.TestCase):
    def test_case_lifeguard_physical(self):
        user_input = '\n'.join([
            '5',
            '3',
            '2',
            '1',
            '9',
            '30'
        ]) + '\n'

        result = subprocess.run(
            ["python", "Problem1/lifeguard_physical.py"],
            input=user_input.encode("utf-8"),
            capture_output=True,
            timeout=5
        )

        output = result.stdout.decode("utf-8")

        self.assertIn("an angle 30 degrees", output)
        self.assertIn("person in 36.4 seconds", output)

if __name__ == "__main__":
    unittest.main()
