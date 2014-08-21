from env2yaml import env2yaml

def test_env2yaml():
    """Basic environment conversion test"""
    env = {"key_1": "value_1", "key_2": "value_2" }
    env_str = ('_env:\n'
               '  key_2: &_env_key_2 "value_2"\n'
               '  key_1: &_env_key_1 "value_1"')
    assert env2yaml(env)  == env_str
