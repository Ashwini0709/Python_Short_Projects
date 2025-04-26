import time
import random

def waiting_game():
    target = random.randint(2,5)
    print("Welcome to the TimeTap game")
    print(f"your target time is {target} seconds")

    input("-----Please enter to begin, match your target time and enter again to stop. Let see how perfect you are!!!!------")
    start = time.perf_counter()

    input(f"Enter again after {target} seconds to stop")
    stop = time.perf_counter()

    elapsed_time = stop - start

    print(f"Elapsed time : {elapsed_time} seconds")

    if elapsed_time == target:
        print("well done perfect timing")
    elif elapsed_time < target:
        print(f"too fast -->  {target - elapsed_time} seconds") 
    else:
        print(f"too slow --> {elapsed_time - target} seconds")




waiting_game()
while(True):
	print("Want to play again")
	hit = input("Enter 'y' to play or 'n' to exit : " )
	if hit == 'y' or hit == 'Y':
		print("-----------------------------------------------------------")
		waiting_game()
	else :
		break


