import typer


def my_app(delete: bool = typer.Option(..., help="Delete files found"),
           extension: str = typer.Argument("txt", help="extension to search")):
    """
     Show Files with  data extension file
    """
    typer.echo(f"Re-search file with extension {extension}")
    print(delete)


if __name__ == '__main__':
    typer.run(my_app)
