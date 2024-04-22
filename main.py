import typer
from typing import Optional

from pathlib import Path


def main(extension: str,
         directory: Optional[str] = typer.Argument(None, help="file in which you have to search"),
         delete: bool = typer.Option(False, help="Deletion of files")):
    """
    Displays files found with given extension.
    """
    # print(extension, directory, delete)
    if not directory:
        directory = Path(directory)
    else:
        directory = Path.cwd()  # current working directory
    if not directory.exists():
        typer.secho(f"Directory {directory} not exits", fg=typer.colors.RED)
        raise typer.Exit()

    files = directory.rglob(f"*.{extension}")
    if delete:
        typer.confirm("Do you want to delete all files found ?",abort=True)
        for file in files:
            file.unlink()
            typer.echo(f"Deletion of file {file}",fg=typer.colors.RED)
    else:
        typer.echo(f"Files found extension: {extension}", fg=typer.colors.BLUE)
        for file in files:
            typer.echo(file)



if __name__ == "__main__":
    typer.run(main)
