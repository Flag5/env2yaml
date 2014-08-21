from argparse import ArgumentParser
from os import environ
from yaml import dump, SafeDumper
from uuid import uuid4
from functools import partial

class ReferenceDumper(SafeDumper):
    """
    A Dumper that allows the first anchor to be overridden
    """
    def __init__(self, *args, anchor=None, **kwargs):
        self._reference_dumper_anchor = anchor
        super().__init__(*args, **kwargs)

    def generate_anchor(self, node):
        self.last_anchor_id += 1
        if self.last_anchor_id == 1:
            return self._reference_dumper_anchor
        else:
            return super().generate_anchor(node)


def main():
    """
    Emit the current environment as a YAML structure
    """
    # Build the parser
    parser = ArgumentParser()
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    parser.add_argument('-a', '--anchor', default='_env',
                        help='YAML anchor to be used (default: %(default)r)')
    parser.add_argument('-k', '--key', default='_env',
                        help=('Top-level key for structure '
                              '(default: %(default)r)'))

    # Parse arguments
    args = parser.parse_args()

    # Read the environment
    environ_dict = dict(environ)
    ref_key = str(uuid4()).replace('-','_')
    env = [{args.key: environ_dict}, {ref_key: environ_dict}]

    # Output the structure
    dumper = partial(ReferenceDumper, anchor=args.anchor)
    lines = dump(env, default_flow_style=False, Dumper=dumper).split('\n')
    print('\n'.join(line[2:] for line in lines if ref_key not in line))
