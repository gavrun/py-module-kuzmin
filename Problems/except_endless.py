import time

print("Endless cycle is launched. Try to click Ctrl+C...")

try:
    while True:
        time.sleep(1)
        print("Working...")
except Exception:
    print("Caught an exception... Exiting not possible!")
    # Loop cycle continues
    while True:
        time.sleep(1)
        print("Executing anyway ... there is no way out.")
