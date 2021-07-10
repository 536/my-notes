# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021/7/12 21:14
# @Author  : https://github.com/536
from pathlib import Path
from urllib import parse

BASE_DIR = Path(__file__).with_name('docs')


def parse_index(p):
    with open(p / 'README.md', 'w', encoding='utf-8') as f:
        for ff in p.glob('*'):
            if ff.is_dir():
                f.write(f'* [*{ff.stem}](./{parse.quote(ff.stem)})\n')
                parse_index(ff)
            if ff.suffix.upper() == '.MD' and ff.stem.upper() != 'README':
                f.write(f'* [{ff.stem}](./{parse.quote(ff.stem)})\n')


if __name__ == '__main__':
    parse_index(BASE_DIR)
