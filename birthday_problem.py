import math
import numpy as np
import matplotlib.pyplot as plt

#initiate final probabilities
prob_no_share_all = np.array([]) 
prob_2_share_all = np.array([]) 
people=range(1,30)

for n in people:
    #calculate probabilities
    prob_no_share = math.factorial(365) / ( math.factorial(365-n)*pow(365,n))
    prob_2_share = 1-prob_no_share
    
    #append final probabilities
    prob_no_share_all = np.append(prob_no_share_all,  prob_no_share)
    prob_2_share_all = np.append(prob_2_share_all,  prob_2_share)    


# Create the plot
plt.figure(figsize=(10, 6))

# Plotting both sets of data
plt.plot(people, prob_no_share_all, label='No shared birthday', marker='o')
plt.plot(people, prob_2_share_all, label='Shared birthday', marker='x')

#x-axis range
plt.xticks(ticks=range(1, len(people) + 1), labels=people)

# Draw a vertical line at 'Person 23'
plt.axvline(x=23, color='red', linestyle=':')

# Adding labels and title
plt.xlabel('Number of people')
plt.ylabel('Probability')
plt.title('The Birthday Problem')

# Move the legend to the upper right corner
plt.legend(loc='upper right')

plt.show()