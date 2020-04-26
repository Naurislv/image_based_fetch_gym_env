from gym.envs.registration import register

register(
    id='image-based-robot-env-v0',
    entry_point='image_based_robot_env.envs:ImRobotEnv',
)