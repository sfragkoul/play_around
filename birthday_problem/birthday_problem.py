import math
import numpy as np
import matplotlib.pyplot as plt

#initiate final probabilities
prob_no_share_all = np.array([]) 
prob_2_share_all = np.array([]) 
people=range(1,41)

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
plt.plot(people, prob_no_share_all, label='No shared birthday', marker='o', color='#009a4d', markersize=5)
plt.plot(people, prob_2_share_all, label='Shared birthday', marker='x', color='#9a009a', markersize=5)

#x-axis range
plt.xticks(ticks=range(1, len(people) + 1), labels=people)

# Draw a vertical line at 'Person 23'
plt.axvline(x=23, color='#9a0000', linestyle=':', alpha = 0.4)

# Adding labels and title
plt.xlabel('Number of people', fontsize=12)
plt.ylabel('Probability', fontsize=12)
plt.title('The Birthday Problem', fontsize=16)

# Move the legend to the upper right corner
plt.legend(loc='upper right')



#Save plot
plt.savefig('plot_probabilities.png', dpi=300, bbox_inches='tight')

# Display the plot
plt.tight_layout()
plt.show()