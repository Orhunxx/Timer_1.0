import time

saniye = int(input("Second:"))

for i in range(saniye):
    print(str(saniye -i) + " Second Left")
    time.sleep(1)

if saniye -i == 1:
    print("Time Is Up")

    
