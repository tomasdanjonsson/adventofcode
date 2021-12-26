# Aliases
alias v := venv
alias f := format
alias d := day
alias m := mypy

_default:
    @just --list --unsorted

# Create virtual environment
venv:
    python -m venv --prompt aoc .venv

# Create dir with solution template
day num:
    @mkdir 2021/day{{num}}
    @echo -e mkdir 2021/day{{num}}
    @cp template/solution.py 2021/day{{num}}/day_{{num}}.py
    @echo -e cp template/solution.py 2021/day{{num}}/day_{{num}}.py

# Format all py & ipynb files
format:
    @echo -e Formating with Black
    @black ./**/**/*.py ./**/**/*.ipynb

# Typecheck all py files
mypy:
    @mypy

