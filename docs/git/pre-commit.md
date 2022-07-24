# pre-commit

ref:

- <https://blog.csdn.net/wuheshi/article/details/104628747>
- <https://pre-commit.com/>

## pre-config

```bash
cd <project>
touch .pre-commit-config.yaml
```

```bash
# .pre-commit-config.yaml
#
# See https://pre-commit.com for more information
# See https://pre-commit.com/hooks.html for more hooks
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.3.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
  - repo: https://github.com/psf/black
    rev: 22.6.0
    hooks:
      - id: black
        args:
          - -S
  - repo: https://github.com/pycqa/isort
    rev: 5.10.1
    hooks:
      - id: isort
        name: isort (python)
```

## Usage

```bash
pip install pre-commit
pre-commit install
```
