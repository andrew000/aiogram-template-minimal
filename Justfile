set shell := ["bash", "-c"]
set windows-shell := ["pwsh.exe", "-NoLogo", "-Command"]

app-dir := "app"
bot-dir := "bot"
platform := if os_family() == "windows" { "windows" } else { "unix" }

pull:
    git pull origin master
    git submodule update --init --recursive

lint:
    echo "Running ruff..."
    uv run ruff check {{ app-dir }} --show-fixes --preview

format:
    echo "Running ruff check with --fix..."
    uv run ruff check {{ app-dir }} --fix --unsafe-fixes

    echo "Running ruff..."
    uv run ruff format {{ app-dir }}

    echo "Running isort..."
    uv run isort {{ app-dir }}

mypy:
    echo "Running MyPy..."
    uv run mypy --explicit-package-bases {{ app-dir }}/{{ bot-dir }}

outdated:
    uv tree --universal --outdated

sync:
    uv sync --all-extras
