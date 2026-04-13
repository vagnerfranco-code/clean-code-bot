import click
from clean_code_bot.analyzer import analyze_code
from clean_code_bot.refactorer import refactor_code
from clean_code_bot.sanitizer import sanitize_input

@click.command()
@click.argument("file_path", type=click.Path(exists=True))
@click.option("--diff", is_flag=True, help="Show diff output")
def main(file_path, diff):
    """Clean and refactor a code file using AI."""

    with open(file_path, "r") as f:
        raw_code = f.read()

    safe_code = sanitize_input(raw_code)

    analysis = analyze_code(safe_code)
    improved_code = refactor_code(safe_code, analysis)

    click.echo("\n=== REFACTORED CODE ===\n")
    click.echo(improved_code)

if __name__ == "__main__":
    main()
