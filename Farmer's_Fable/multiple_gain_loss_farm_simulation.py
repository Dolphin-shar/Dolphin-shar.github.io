#this aims to give a more full scanning simulation to the problem, when I obviously do genuinely hate myself, I made this
#This simulation uses a dedicated seed for all simulation, to only focus on the effect of gain-loss factor on the result of simulation instead of randomised outcome every time

#initialising user prompt
print("This program generate an analysis on a simulation of farmer's problem with a dedicated result settings series,\n analysis result on both graphical depiction of evolutionary benefits and raw simulation data will be produced.")

import numpy as np
import matplotlib.pyplot as plt
def f(x,y):
    return x*y

#size of each simulation
array_size = int(input("input an integer value for the number of rounds of harvest will be simulated, this value must be larger than 1\ninput: "))
#range of gain
gain_min = float(input("enter the lower bound of the gain factor, note the min value must be larger than or equal to 1\ninput: "))
gain_max = float(input("enter the upper bound of the gain factor, note the step of increment is 0.01 and if you enter a huge number it will take a while to finish the simulation\ninput: "))
gains = np.arange(gain_min*100,gain_max*100 +1,1)/100 #a multiplcation is done to avoid function bug from decimal, see documentation
#print(gains)
loss_min = float(input("enter the lower bound of the loss factor, this number must be larger than 0\ninput: "))
loss_max = float(input("enter the upper bound of the loss factor, this number must be less than or equal to 1\ninput: "))
loss = np.arange(loss_min*100,loss_max*100+1,1)/100
# print(loss)
X,Y = np.meshgrid(gains,loss)
# print(X)
# print(Y)
Z = f(X,Y)#calculate the product of loss and gain factor, unity would imply balanced loss-gain potential
# print(Z)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,cmap='viridis', edgecolor='none')
ax.set_title('surface of gain-loss factor multiplcation of gain:[{},{}],loss:[{},{}]'.format(gain_min,gain_max,loss_min,loss_max))
plt.show()
plt.close()
def independent_outcome(result, success_weight,fail_weight,starting_number = 1):
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
        # print(crops)
        history[i] = crops*1
        i += 1
    # print(f"final number of crops independent is {history[-1]:.4f}")

    return history
def sharing_outcome(result1,result2,success_weight,fail_weight,initial_crops = 1):
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

def simulation(a,a1,gain,loss):
    # growing = np.arange(array_size+1) # now zero is the initial amount of crops 
    result1 = independent_outcome(a,success_weight=gain,fail_weight=loss)
    result2 = independent_outcome(a1,success_weight=gain,fail_weight=loss)
    sharedresult = sharing_outcome(a,a1,success_weight=gain,fail_weight=loss)
    return result1,result2,sharedresult

#now define the simulation pipeline
dimensions = np.shape(Z)
import csv
number_of_sims = np.prod(dimensions)
X_line = np.reshape(X,(-1))
Y_line = np.reshape(Y,(-1))
Z_line = np.reshape(Z,(-1))
# print(X_line)
# print(Y_line)


#Let's gooooo
seed1 = int(input("enter an integeral value for seed 1, a random state for farmer 1\ninput: "))
seed2 = int(input("enter an integeral value for seed 2, a random state for farmer 2\ninput: "))
with open('{}.csv'.format(input("name your output file name: (use _ instead of space please and no weird notations like %,$,& etc.)\ninput: ")), 'w', newline='') as file:
    sim_no = 0
    writer = csv.writer(file)
    writer.writerow(["sim no.","seed","product of factor" ,"progress after first harvest"])
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    for gain  in X_line:
        loss = Y_line[sim_no]
        product = Z_line[sim_no]
        np.random.seed(seed1) #seeding the random generator for reproducibility
        a = np.random.rand(array_size)
        np.random.seed(seed2)
        a1 = np.random.rand(array_size)
        result1,result2,cooperation = simulation(a,a1,gain,loss)
        coop_outcome = cooperation[-1]
        Ind_outcome_1 = result1[-1]
        Ind_outcome_2 = result2[-1]
        coop_total = coop_outcome *2 #we define, benefit from cooperation exist if coop * 2 > sum(IND1+IND2)
        if coop_total / (Ind_outcome_1+Ind_outcome_2) > 1: #evolutionary benefitial
            ax.scatter(gain,loss,product,c = "green")
        elif coop_total / (Ind_outcome_1+Ind_outcome_2) == 1: #unity, neither punished or benefited
            ax.scatter(gain,loss,product,c = "black")
        else:#punished
            ax.scatter(gain,loss,product,c = "red")
        writer.writerow([sim_no+1,seed1,product,*result1])
        writer.writerow([sim_no+1,seed2,product,*result2])
        writer.writerow([sim_no+1,"coop",product,*cooperation])
        sim_no += 1
    ax.set_title("scatter plot of qualitative result on simulation") #green for benefited,black for unity and red for punished result from cooperation
    ax.set_xlabel("gain factor")
    ax.set_ylabel("loss factor")
    ax.set_zlabel("product of gain-loss")
    plt.show()
print(dimensions,number_of_sims)