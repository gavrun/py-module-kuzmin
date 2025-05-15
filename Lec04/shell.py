import subprocess
import filecmp

INPUT_FILE_PATH = "input.txt"
OUTPUT_FILE_PATH = "output.txt"
EXPECTED_OUTPUT_FILE_PATH = "output_expected.txt"
command = ["python", "good_kid.py"]

try:
    with open(INPUT_FILE_PATH, "r") as infile, open(OUTPUT_FILE_PATH, "w") as outfile:
        result = subprocess.run(command, stdin=infile, stdout=outfile, stderr=subprocess.PIPE, text=True, check=True)
except OSError:
    print(f'OSError due to failure when opening the file')
except FileNotFoundError:
    print(f'Input file {INPUT_FILE_PATH} not found')
except subprocess.CalledProcessError as e:
    print(f'Process returned a non-zero code')
except Exception as e:
    print(f'An unexpected error {e}')
finally:
    print('Inside finally')

print(f'Exit code {result}')
print(f'Standard error output: {result.stderr}')

result = filecmp.cmp(OUTPUT_FILE_PATH, EXPECTED_OUTPUT_FILE_PATH)
print(result)
result = filecmp.cmp(OUTPUT_FILE_PATH, EXPECTED_OUTPUT_FILE_PATH, shallow=False)
print(result)

