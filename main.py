import typer
from typing import Optional


def main(extension: str,
         directory: Optional[str] = typer.Argument(None, help="file in which you have to search"),
         delete: bool = typer.Option(False, help="Deletion of files")):
    """
    Displays files found with given extension.
    """
    print(extension, directory, delete)


if __name__ == "__main__":
    typer.run(main)
