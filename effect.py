import random
import os
import time

os.system("color 2")

while True:

    for k in range(160):
        choice = random.randrange(1, 4)
        if choice == 1:
            print("0", end="")
        elif choice == 2:
            print("1", end="")
        elif choice == 3:
            print(" ", end="")
    print()
    time.sleep(0.05)
