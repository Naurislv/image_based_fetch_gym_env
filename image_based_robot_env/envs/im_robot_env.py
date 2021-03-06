import os
from gym import utils

# Local imports
from . import gym_fetch_env


DIR_PATH = os.path.dirname(os.path.abspath(__file__))

# Ensure we get the path separator correct on windows
MODEL_XML_PATH = os.path.join(DIR_PATH, 'mujoco_world/reach.xml')


class ImRobotEnv(gym_fetch_env.FetchEnv, utils.EzPickle):
    def __init__(self, reward_type='sparse'):
        initial_qpos = {
            'robot0:slide0': 0.4049,
            'robot0:slide1': 0.48,
            'robot0:slide2': 0.0,
        }

        target_in_the_air = False  # True by default
        gripper_extra_height = 0.5  # 0.2 by default

        gym_fetch_env.FetchEnv.__init__(
            self, MODEL_XML_PATH, has_object=False, block_gripper=True, n_substeps=20,
            gripper_extra_height=gripper_extra_height, target_in_the_air=target_in_the_air,
            target_offset=0.0, obj_range=0.15, target_range=0.15, distance_threshold=0.05,
            initial_qpos=initial_qpos, reward_type=reward_type)
        utils.EzPickle.__init__(self)