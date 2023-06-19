#Creator: Chan Hoi Ching
#project description: simulation for the farmer's problem
import numpy as np
import matplotlib.pyplot as plt
array_size = 100 #the number of growth being attempted in the simulation
seed1 = int(input("input a integer number as the seed(random state e.g. 125) of your 1st farmer: ")) #125 as in the example
seed2 = int(input("input a integer number as the seed(random state e.g. 398) of your 2nd farmer: ")) #398 as in the example

success_weight = np.float32(input("input a float number(number with decimal e.g. 1.5) as the gaining weight of a good harvest: "))#example using 1.5
fail_weight = np.float32(input("input a float number(number with decimal e.g. 0.7) as the lose weight of a bad harvest: "))#example using 0.7

np.random.seed(seed1) #seeding the random generator for reproducibility
a = np.random.rand(array_size)
np.random.seed(seed2)
a1 = np.random.rand(array_size)

b = np.arange(array_size)
# print(a,b)
True_array =  a>=0.5
False_array = np.invert(True_array)

#showing the distribution of randomness, as the distribution ranges from [0,1), 0.5 or above is considered to be a successful attempted
plt.plot(b[True_array],a[True_array],"go",label = "good harvest")
plt.plot(b[False_array],a[False_array],"ro",label = "bad harvest")
plt.legend()
plt.xlabel("Harvest attempt,counting from 0")
plt.ylabel("result")
plt.title("seed 1 random distribution plot")
plt.show()

def independent_outcome(result, starting_number = 1):
    #some initializations
    good_attempts = result>=0.5
    crops = starting_number
    history = np.zeros(array_size + 1)
    history[0] = starting_number
    i = 1
    #simulation
    for attempt in  good_attempts:
        if attempt:
            crops *= success_weight
        else:
            crops *= fail_weight
        history[i] = crops*1
        i += 1
    print(f"final number of crops independent is {history[-1]:.4f}")

    return history

def sharing_outcome(result1,result2,initial_crops = 1):
    history = np.zeros(array_size + 1)
    history[0] = initial_crops
    crops = initial_crops * 1
    True_outcome1 = result1 >= 0.5
    True_outcome2 = result2 >= 0.5
    i = 1
    for j in np.arange(array_size):
        if True_outcome1[j]:
            crops1 = crops*success_weight
            # Here is a line of code to check the conditional statement is checked for every loop, problem can easily happen in structured if-else statement in python
            # print("outcome1 is checked")
        else:
            crops1 = crops*fail_weight
            # print("outcome1 is checked")
        if True_outcome2[j]:
            crops2 = crops*success_weight
            # print("outcome2 is checked")
        else:
            crops2 = crops*fail_weight
            # print("outcome2 is checked")
        crops = np.mean([crops1,crops2])
        history[i] = crops*1
        i += 1
    return history

#now let's try
growing = np.arange(array_size+1) # now zero is the initial amount of crops 
result1 = independent_outcome(a)
result2 = independent_outcome(a1)
plt.plot(growing,result1,"r-",label = "farmer 1(independent)")
plt.plot(growing,result2,"g-",label = "farmer 2(independent)")
# plt.legend()
# plt.ylabel("crops")
# plt.xlabel("attempt")
# plt.show()

#now we share the risk and reward
shared_result = sharing_outcome(a,a1)
print(f"final outcome of collaborated farming is {shared_result[-1]:.4f}")
plt.plot(growing,shared_result,"k-",label = "shared result")
plt.legend()
plt.ylabel("crops")
plt.xlabel("attempt")
plt.show()

input("press enter to exit.....")

#proceed to make multiple cycles of simulation