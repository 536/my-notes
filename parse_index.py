# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021/7/12 21:14
# @Author  : https://github.com/536
from pathlib import Path
from urllib import parse

BASE_DIR = Path(__file__).with_name('docs')


def get_level(p):
    i = 0
    while p.parent != BASE_DIR:
        p = p.parent
        i += 1
    return i


def parse_index():
    files = []
    for file in BASE_DIR.rglob('*.md'):
        if file not in files:
            files.append(file)
        while file.parent != BASE_DIR:
            file = file.parent
            if file not in files:
                files.append(file)

    with open(BASE_DIR.parent / '_sidebar.md', 'w', encoding='utf-8') as f:
        for file in sorted(files, key=lambda x: x.as_posix()):
            level = get_level(file)
            if file.is_dir():
                path = file.stem
            else:
                path = f'[{file.stem}](/docs{parse.quote(file.as_posix().replace(BASE_DIR.as_posix(), ""))})'
            print('  ' * level + f'+ {path}')
            f.write('  ' * level + f'+ {path}\n')


if __name__ == '__main__':
    parse_index()
