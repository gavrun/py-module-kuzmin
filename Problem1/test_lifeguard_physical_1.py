# integration console test via subprocess by simulating input and capturing output

import subprocess

def test_case_lifeguard_physical():
    # Input data as in manual example
    user_input = '\n'.join([
        '5',     # d1 (yards)
        '3',     # d2 (feet)
        '2',     # h (yards)
        '1',     # v_sand (miles per hour)
        '9',     # n
        '30'     # theta1 (degrees)
    ]) + '\n'

    # Run as a separate process
    result = subprocess.run(
        ["python", "Problem1/lifeguard_physical.py"],
        input=user_input.encode("utf-8"),
        capture_output=True,
        timeout=5
    )

    output = result.stdout.decode("utf-8")
    print(output)

    # Checking expected phrases in output 

    # print(f"\nIf the lifeguard starts moving at an angle {int(round(theta1_deg))} degrees,"
    #  f"he will reach a drowning person in {round(time, 1)} seconds")
    assert "an angle 30 degrees" in output
    assert "person in 36.4 seconds" in output

    # correctness of the logic and formulas is checked
    # the calculation of time (36.4 sec) must coincide with the output

if __name__ == "__main__":
    test_case_lifeguard_physical()
    print("Test passed.")
