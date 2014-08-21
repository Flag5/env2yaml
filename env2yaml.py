from argparse import ArgumentParser
from os import environ
from yaml import safe_dump


def env2yaml(env, env_key='_env', anchor_template='_env_%s'):
    """
    Convert an environment into a yaml string
    """
    lines = ['%s:' % env_key]
    for key in env:
        value = safe_dump(env[key], indent=2, default_style='"')[:-1]
        lines.append('  %s: &%s %s' % (key, anchor_template % key, value))
    return '\n'.join(lines)


def main():
    """
    Emit the current environment as a YAML structure
    """
    # Build the parser
    parser = ArgumentParser()
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    parser.add_argument('-a', '--anchor-template', default='_env_%s',
                        help='YAML anchor to be used (default: %(default)r)')
    parser.add_argument('-k', '--key', default='_env',
                        help=('Top-level key for structure '
                              '(default: %(default)r)'))

    # Parse arguments
    args = parser.parse_args()

    # Render the environment
    print(env2yaml(environ, env_key=args.key,
                   anchor_template=args.anchor_template))
