import click


@click.command()
@click.option('--desc', prompt='Enter a Image Description')
def user_input(desc):
    click.echo(f'This is the image: {desc}')


def main():
    print(user_input())


if __name__ == '__main__':
    main()
