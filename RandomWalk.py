import matplotlib.pyplot as plt
import numpy as np
np.random.seed(123)
all_walks = []

# Simulate random walk 500 times based on dicerolls
for i in range(500) :
    random_walk = [0]

    #100 Steps in each walk
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)

        elif dice <= 5:
            step = step + 1

        else:
            step = step + np.random.randint(1,7)
            
        #Random chance of falling all the way down
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.title("Random Walk Outcome")
plt.xlabel("Dice Rolls")
plt.ylabel("Step")
plt.show()



# Select last row from np_aw_t: ends
ends = np.array(np_aw_t[-1])

# Plot histogram of ends(End Result of Random Walk), display plot
plt.hist(ends)
plt.title("Random Walk Distribution")
plt.xlabel("Dice Rolls")
plt.ylabel("Step")
plt.show()
