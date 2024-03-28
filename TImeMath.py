import random
import time


operators = ["+", "-", "*"]
start = 3
end = 12



def Problem_Generator():
    right = random.randint(start,end)
    left = random.randint(start,end)
    operator = random.choice(operators)

    exp = str(right) + " " + operator + " " + str(left)
    answer = eval(exp)
    exp += " = "
    return exp, answer


print("This program test your speed at math calculations")
input("Press Enter to start the test")
print("-------------------------------------------------------------")

start_time = time.time()

for i in range(10):
    exp, answer = Problem_Generator()
    while True:
        try:
            ans = int(input("#Problem"+str(i+1)+" "+exp))
        except:
            continue
        if ans == answer:
            break
        print("try again")

end_time = time.time()
total_time = end_time - start_time
print("-------------------------------------------------------------")
print("You have completed the test in ",round(total_time,2),"seconds")



