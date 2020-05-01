"""This is an example showing how to run the custom environment using OpenAI Gym."""

# Standard imports
import time
import os

# Dependency imports
import cv2

import gym
import image_based_robot_env


def make_env():
    """Create environment object"""
    env = gym.make("image-based-robot-env-v0")

    # These steps are required as workaround because of different bugs experienced during testing
    env.reset()
    env.render('rgb_array')
    env.step([0, 0, 0, 0])

    return env


def main():
    """Run example."""
    if not os.path.exists('frames'):
        os.makedirs('frames')

    env = make_env()

    for idx in range(20):
        # Rendering support only mode=human and should be used for testing purposes
        # env.render(mode='human')

        observation, _, _, _ = env.step(env.action_space.sample())

        cv2.imwrite(f'frames/{idx}_frame.png', observation['observation'])


if __name__ == "__main__":
    main()