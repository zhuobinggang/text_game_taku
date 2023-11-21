def init_env():
    from jericho import FrotzEnv
    env = FrotzEnv("z-machine-games-master/jericho-game-suite/zork1.z5")
    initial_observation, info = env.reset()
    done = False
    return env



