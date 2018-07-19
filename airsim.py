# Reinforcement Learning model for AirSim simulator by Microsoft.
# This model implements DQN in AirSim using CNTK.

# First, we need to get the images from simulation and transform them
# appropriately. Below, I've obtained a depth image from the ego camera
# and transformed to an 84X84 input to the network. 
# (You can use other sensor modalities, and sensor inputs as well.
# Ofcourse you’ll have to modify the code accordingly).

responses = client.simGetImages([ImageRequest(0, AimSimImageType.DepthPerspective, True, False)])
current_state = transform_input(responses)

# Define six actions: breaking, straight with throttle,
# full-left with throttle, full-right with throttle,
# half-left with throttle, half-right with throttle
# that an agent can execute.
def interpret_action(action):
    car_controls.brake = 0
    car_controls.throttle = 1

    # brake
    if action == 0:
        car_controls.throttle = 0
        car_controls.brake = 1
    # straight throttle
    elif action == 1:
        car_controls.steering = 0
    # full-right throttle
    elif action == 2:
        car_controls.steering = 0.5
    # full-left throttle
    elif action == 3:
        car_controls.steering = -0.5
    # half-right throttle
    elif action == 4:
        car_controls.steering = 0.25
    # half-left throttle
    else:
        car_controls.steering = -0.25

    return car_controls       