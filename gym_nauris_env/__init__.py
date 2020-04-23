from gym.envs.registration import register

register(
    id='nauris-env-v0',
    entry_point='gym_nauris_env.envs:NaurisEnv',
)