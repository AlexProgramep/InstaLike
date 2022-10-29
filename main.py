import click
from instapy import InstaPy


@click.group()
def mycommands():
    pass


@click.command()
@click.option("--username", prompt="Введіть нiкнейм", help="Нiкнейм користувача.")
@click.option("--password", prompt="Введіть пароль", help="Пароль користувача.")
def insta(username, password):
    try:
        session = InstaPy(username=username, password=password)
        session.login()

        session.like_by_tags(["food", "cars", "bloger"])
        session.set_dont_like(["nsfw", "18+"])
        session.set_ignore_users(['user', 'bot'])
        session.end()
    except Exception:
        click.echo("Невірний логін або пароль")


mycommands.add_command(insta)

if __name__ == "__main__":
    mycommands()
