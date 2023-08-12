import re
import json
import functools
import urllib.request
from jinja2.ext import Extension

@functools.lru_cache()
def pipinfo(name):
  with urllib.request.urlopen("https://pypi.org/pypi/{}/json".format(name)) as fr:
    return json.load(fr)

def pipdeps(deps):
  return '\n'.join(
    m.group('name')
    for dep in deps or []
    for m in (re.match(r'^(?P<name>[^ ]+)( \(.+?\))?$', dep),)
    if m
  )

def pipoptdeps(deps):
  return '\n'.join(
    '{}: for extra {}'.format(
      m.group('name'), m.group('extra')
    )
    for dep in deps or []
    for m in (re.match(r'^(?P<name>[^ ]+)( \(.+?\))? ; extra == \'(?P<extra>.+?)\'', dep),)
    if m
  )

class PipInfoExtension(Extension):
  def  __init__(self, environment):
    super(PipInfoExtension, self).__init__(environment)
    environment.filters['pipinfo'] = pipinfo
    environment.filters['pipdeps'] = pipdeps
    environment.filters['pipoptdeps'] = pipoptdeps
