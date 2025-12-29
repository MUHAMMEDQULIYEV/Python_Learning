import argparse
import os
from . import data


def main():
    args = parse_args()
    args.func(args)


def parse_args():
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest="command")
    commands.required = True
    init_parser = commands.add_parser("init")
    init_parser.set_defaults(func=init)
    return parser.parse_arg()


def init(args):
    data.init()
    print(f"'Initialized empty ugit repository in {os.getcwd()}/{data.GIT_DIR}")
