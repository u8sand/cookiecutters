import pathlib
cookiecutter_path = pathlib.Path("{{ cookiecutter.filename }}.py").absolute()
script_path = (cookiecutter_path.parent.parent/cookiecutter_path.name).with_suffix('')
cookiecutter_path.rename(script_path)
cookiecutter_path.parent.rmdir()
script_path.chmod(0o755)