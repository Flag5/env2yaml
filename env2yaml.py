from argparse import ArgumentParser
from os import environ
from yaml import safe_dump

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

    # Read the environment
    print('%s:' % args.key)
    for key in environ:
        value = safe_dump(environ[key], indent=2, default_style='"')[:-1]
        print('  %s: &%s %s' % (key, args.anchor_template % key, value))
