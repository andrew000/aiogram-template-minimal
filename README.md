# aiogram-template-minimal

This is a minimal template for creating Telegram bots using the aiogram library.

#### ❗️ Read [HELP.md](HELP.md) if something is unclear ❗️

### Template uses:

* aiogram 3
* uv

***

## Installation

### Step 1: Clone the repository

```shell
git clone https://github.com/andrew000/aiogram-template-minimal.git
cd aiogram-template-minimal
```

### Step 2: Install dependencies

I recommend using [UV](https://docs.astral.sh/uv/) to manage your project.

```shell
# Create virtual environment using UV
uv venv --python=3.13

# Install dependencies
make sync
```

### Step 3: Create `.env` file

Create a `.env` file in the root of the project and fill it with the necessary data.

```shell
cp .env.example .env
```

### Step 4: Start project

```shell
uv run --env-file .env app/bot/main.py
```

### Step 5: Bot is ready and running

Bot is ready to use. You can check the logs in terminal.

***

## Explanation

### Project structure

The project structure is as follows:

```
AIOGRAM-TEMPLATE
├───app (main application)
│   ├───bot (bot)
│   │   ├───errors (error handlers)
│   │   ├───filters (custom filters)
│   │   ├───handlers (event handlers)
│   │   ├───main.py (bot entrypoint)
│   │   ├───middlewares (event middlewares)
│   │   ├───pyproject.toml (bot workspace configuration)
│   │   ├───settings.py (bot settings)
│   │   └───utils (utility functions)
├───pyproject.toml (project configuration)
├───.env.example (example environment file)
├───.pre-commit-config.yaml (pre-commit configuration)
└───Makefile (make commands)
```

The bot is located in the `app/bot` directory. The bot is divided into modules, each of which is responsible for a
specific functionality. `handlers` are responsible for processing events, `middlewares` for preprocessing events,
`filters` for own filters, `errors` for error handling.

### Pre-commit

The project uses pre-commit hooks. To install pre-commit hooks, run the following command:

```shell
uv run pre-commit install
```

### Webhooks

Bot may use webhooks. To enable webhooks, set `WEBHOOKS` environment variable to `True` in the `.env` file. Also, set
`WEBHOOK_URL` and `WEBHOOK_SECRET_TOKEN` environment variables.
