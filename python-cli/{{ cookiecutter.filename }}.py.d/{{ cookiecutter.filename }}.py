#!/usr/bin/env python3

import click
import typing as t
import logging; logger = logging.getLogger()

def verboseOption(**kwargs):
  ''' Click option to configure logging verbosity
  '''
  class CallableFormatter:
    def __init__(self, fmt: t.Callable[[logging.LogRecord], str]):
      self._fmt = fmt

    def format(self, record):
      return self._fmt(record)

  def callback(ctx: click.Context, param: click.Parameter, value: int) -> None:
    if not value or ctx.resilient_parsing: return
    sh = logging.StreamHandler()
    sh.setFormatter(CallableFormatter(lambda r: f"{'' if r.name == 'root' else r.name}[{r.levelname.lower()}]: {r.msg}"))
    logger.addHandler(sh)
    logger.setLevel(max(logging.WARNING - value*10, logging.DEBUG))

  param_decls = ('-v', '--verbose',)
  kwargs.setdefault('count', True)
  kwargs.setdefault('type', int)
  kwargs.setdefault('default', 0)
  kwargs.setdefault('is_eager', True)
  kwargs.setdefault('help', 'Increase verbosity, more `v`s, more verbose')
  kwargs['callback'] = callback
  return click.option(*param_decls, **kwargs)

{%- if cookiecutter.comma_separated_commands.split(',')|length > 1 %}

@click.group()
@verboseOption()
def cli(**kwargs):
  ''' My CLI help
  '''
  pass

{%- for command in cookiecutter.comma_separated_commands.split(',') %}

@cli.command()
@verboseOption()
@click.option('-d', '--dry-run', type=bool, is_flag=True, default=False, help='Just show what would be done')
@click.argument('message', type=str)
def {{ command }}(message, *, dry_run, **kwargs):
  ''' My command help
  '''
  logging.info(f"{message=} {dry_run=} {kwargs=}")
{%- endfor %}

if __name__ == '__main__':
  cli()
{%- else %}

@click.command()
@verboseOption()
@click.option('-d', '--dry-run', type=bool, is_flag=True, default=False, help='Just show what would be done')
@click.argument('message', type=str)
def {{ cookiecutter.comma_separated_commands }}(message, *, dry_run, **kwargs):
  ''' My command help
  '''
  logging.info(f"{message=} {dry_run=} {kwargs=}")

if __name__ == '__main__':
  {{ cookiecutter.comma_separated_commands }}()
{%- endif %}
