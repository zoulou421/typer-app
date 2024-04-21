import typer

app = typer.Typer()


def my_app(delete: bool = typer.Option(False, help="Delete files found"),
           extension: str = typer.Argument("txt", help="extension to search")):
    """
     Show Files with  data extension file
    """
    typer.echo(f"Re-search file with extension {extension}")
    # print(delete)
    if delete:
        typer.echo("Files deletion with command")

    # same like input of python
    # extension = typer.prompt("which extension are you gonna wish ?")
    # print(extension)
    # if delete:
    # confirm = typer.confirm("Do you really wanna delete files ?", abort=True)
    #    typer.confirm("Do you really wanna delete files ?", abort=True)
    '''if not confirm:
            typer.echo("Operation cancelled...")
            raise typer.Abort()'''
    #    print("Files deletion...")


@app.command("search")  # rename function with search
def search_py():
    my_app(delete=False, extension="py")


@app.command("delete")
def delete_py():
    my_app(delete=True, extension="py")


# python my_app.py --help

if __name__ == '__main__':  # python my_app.py --delete
    # typer.run(my_app)
    app()
