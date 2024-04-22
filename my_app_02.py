import typer
from colorama import just_fix_windows_console
# from termcolor import colored
import sys

from termcolor import colored, cprint


def my_app_02():
    # first_name = typer.style("Bonevy", bold=True)
    first_name = typer.style("Bonevy", bg=typer.colors.BLUE, fg=typer.colors.BRIGHT_RED, underline=True)
    typer.echo(f"Hello {first_name} !")

    # termcolor
    print(colored('Hello, World!', 'green', 'on_red'))

    text = colored("Hello, World!", "blue", attrs=["reverse", "blink"])
    print(text)
    cprint("Hello, World!", "green", "on_red")

    print_red_on_cyan = lambda x: cprint(x, "blue", "on_cyan")
    print_red_on_cyan("Hello, World!")
    print_red_on_cyan("Hello, Universe!")

    for i in range(10):
        cprint(i, "magenta", end=" ")

    cprint("Attention!", "blue", attrs=["bold"], file=sys.stderr)


if __name__ == "__main__":
    typer.run(my_app_02)
