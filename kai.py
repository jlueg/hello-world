# importing time module
# edited version of filei V2
import time

print("Gleich muss ich warten")
time.sleep(5)
print("habe 5 Sekunden gewartet..")

message = "ich blinke froehlich vor mich hin"

for i in message:
    # drucke jeden einzelnen Buchstaben
	print(i)
	time.sleep(0.1)
