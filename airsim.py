# Reinforcement Learning model for AirSim simulator by Microsoft.
# This model implements DQN in AirSim using CNTK.

# First, we need to get the images from simulation and transform them
# appropriately. Below, I've obtained a depth image from the ego camera
# and transformed to an 84X84 input to the network. 
# (You can use other sensor modalities, and sensor inputs as well.
# Ofcourse you’ll have to modify the code accordingly).