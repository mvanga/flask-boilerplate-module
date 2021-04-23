from flask.cli import AppGroup

# =============================================================================
# Custom CLI Commands
# =============================================================================

app_cli = AppGroup('app')

@app_cli.command('hello')
def cli_hello():
    print('Hello!')

# NOTE: SECTION:CLI: Your custom CLI commands go here...
