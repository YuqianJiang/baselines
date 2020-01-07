from baselines.deepr import models  # noqa
from baselines.deepr.build_graph import build_act, build_train  # noqa
from baselines.deepr.deepr import learn, load_act  # noqa
from baselines.deepr.replay_buffer import ReplayBuffer, PrioritizedReplayBuffer  # noqa

def wrap_atari_dqn(env):
    from baselines.common.atari_wrappers import wrap_deepmind
    return wrap_deepmind(env, frame_stack=True, scale=False)
