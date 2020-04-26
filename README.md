# Image based OpenAI Gym environment

This is a custom Gym environment [FetchReach-v1](https://gym.openai.com/envs/FetchReach-v1/) implementation following this [tutorial](https://medium.com/@apoddar573/making-your-own-custom-environment-in-gym-c3b65ff8cdaa).

## Motivation

I am working on sophisticated robotics solutions for Smart Manufacturing use-cases. In my experience, I have observed that simpler solutions often work better in production than more sophisticated, think OpenCV vs Machine Learning. Supervised Machine Learning methods are very hard to implement in the factory because you almost never have enough nor right data to feed for algorithms. While solutions implementing classical Computer Vision algorithms (OpenCV) work well in many cases, they introduce other challenges such as calibration requirements, longer robot setups, more complex development, engineering pipelines, etc.

Note that I have specific robotics use-cases in mind which I would like to replicate in simulator therefore just any simulator with or without robot will not work and this is why I am motivated to create something working for my specific needs and not the approach which would work with multiple environments.

When looked through the vast resources and possibilities to set up the simulator for Robotics use-cases I stumbled upon a few major obstacles:

1. I am not planning to create an environment from scratch therefor most environments did not fit the bill just because they way off from what I want.
2. Most environments are not suitable for Reinforcement learning because it's hard or impossible to speed them up.
3. Even if the environment supports speed up its the interface is complicated to use and integrating Reinforcement learning algorithms are rather unpleasurable

So I settled on OpenAI Gym which seems to bring the best balance. Once I'll need something which will reflect the real world in more detail, I will revisit this topic.

## Installation

Install custom Gym environment:

1. `pip install gym`
2. `git clone https://github.com/Naurislv/image_based_fetch_gym_env.git`
3. `cd image_based_fetch_gym_env`
4. `pip install -e .`

## Usage

```python
import gym

env = gym.make("image-based-robot-env-v0")

# These steps are required as workaround because of different bugs experienced during testing
obs = env.reset()
env.render('rgb_array')
_, _, _, _ = env.step([0, 0, 0, 0])
```

## Spaces

1. `env.observation_space['observation']`: Box(RGB uint8 array consisting of 2 images stiched together. These are two different camera views in environment.)
2. `env.observation_space['desired_goal']`: Box(x, y, z coordinates of desired goal)
3. `env.observation_space['achieved_goal']`: Box(x, y, z coordinates of achieved goal)
4. `env.action_space`: Box(actions)

## My Approach

From [here](https://github.com/openai/gym/tree/master/gym/envs/robotics) I copied and adjusted following files:

1. Environment: `fetch_env.py`
2. Assets (MuJoCo) description: `reach.xml`, `robot.xml` and `shared.xml`
3. Stls and textures for fetch environment
