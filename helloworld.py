import click


@click.command()
@click.option('-c', '--case', type=click.Choice(['upper', 'lower']))
@click.argument('person', default='you')
def hello(case, person):
    respone = "Hello World! Also, hey {} ".format(person)

    if case == 'upper':
        click.echo(respone.upper())
        #click.echo('You selected {} case.'.format(case))
    elif case == 'lower':
        click.echo(respone.lower())
    else:
        click.echo(respone)
