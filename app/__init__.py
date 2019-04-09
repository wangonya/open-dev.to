import click
import webbrowser


@click.command()
@click.option('--tag', '-t', help='add a tag')
def main(tag):
    """
    Open a new dev.to browser tab on the browser
    """
    if tag:
        url = 'https://dev.to/t/{}'.format(tag)
    else:
        url = 'https://dev.to'

    webbrowser.open(url, new=2)


if __name__ == "__main__":
    main()
