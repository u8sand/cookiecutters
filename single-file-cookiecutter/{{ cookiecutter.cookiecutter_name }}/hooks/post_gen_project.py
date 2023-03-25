import pathlib
p = pathlib.Path("{{ '{{' }} cookiecutter.filename {{ '}}' }}{{ cookiecutter.extension }}").absolute()
p.rename(p.parent.parent/p.name)
p.parent.rmdir()