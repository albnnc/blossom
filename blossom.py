#!/usr/bin/env python


import argparse
import configparser
import os
import shutil


def clean_path(path):
    if not os.path.isdir(path):
        return
    for i in os.listdir(path):
        i = os.path.join(path, i)
        if os.path.islink(i):
            os.remove(i)


def link_paths(a, b, isForce):
    if isForce and os.path.lexists(b):
        if os.path.isdir(b) and (not os.path.islink(b)):
            shutil.rmtree(b)
        else:
            os.remove(b)
    os.symlink(a, b)


def main():
    DIR = '~/dotfiles'
    CFG = 'blossom.cfg' # relative to the DIR

    parser = argparse.ArgumentParser(epilog='''\
    Blossom is a file management utility. It is ususally used to install
    various dotfiles by creating symbolic links. To configure this tool
    you need to create a file called blossom.cfg in a directory which would
    serve as home for your configuration files. By default, this directory
    is ~/dotfiles.\
    ''')

    parser.add_argument(
        '-c',
        '--clean',
        action='store_true',
        help='perform cleanup'
    )

    parser.add_argument(
        '-l',
        '--link',
        action='store_true',
        help='perform linking'
    )

    parser.add_argument(
        '-f',
        '--force',
        action='store_true',
        help='remove existing destination files if linking'
    )

    parser.add_argument(
        '-d',
        '--dir',
        metavar='D',
        default=os.path.expanduser(DIR),
        help='specify working directory (default is ~/dotfiles)'
    )

    args = parser.parse_args()

    config = configparser.ConfigParser(allow_no_value=True)
    config.optionxform = str
    config.read(os.path.join(args.dir, CFG))
    config = config._sections

    clean = {os.path.expanduser(i) for i in config.get('clean', {}).keys()}
    link = {
        os.path.join(args.dir, os.path.expanduser(k)) : os.path.expanduser(v)
        for k, v in config.get('link', {}).items()
    }

    if args.clean:
        for i in clean:
            clean_path(i)
    if args.link:
        for k, v in link.items():
            try:
                link_paths(k, v, args.force)
            except FileExistsError:
                print('failed to create symbolic link: file exists')
            except FileNotFoundError:
                print('failed to create symbolic link: not a directory')


if __name__ == "__main__":
    main()

