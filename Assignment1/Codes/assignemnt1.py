import numpy as np 
from scipy.stats import binom

#number of simulations 
simlen = 400000000

#number of articles produced in single simulation(sample space)
n = 12

#probabilty of a defective article occuring
p = 0.1

#binomial distrubution
data_binom = binom.rvs(n,p,size = simlen)

#calculating proabilty for 9 defective articles to be produced

count = 0

for i in range(simlen):
    if data_binom[i] == 9:
        count+=1
prob_sim = count/simlen


#calculating theoretical probabilty using probability mass function
prob_theo = binom.pmf(9,n,p)


#formatting probabilities to scinetific notation
    
formatted_prob_sim =  format(prob_sim,"e")
formatted_prob_theo =  format(prob_theo,"e")

print("The simulated probabilty is "+formatted_prob_sim)
print("The theorietical probability is "+formatted_prob_theo)