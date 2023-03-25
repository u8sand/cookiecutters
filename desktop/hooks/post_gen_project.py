import pathlib

cookiecutter_path = pathlib.Path("{{ cookiecutter.filename }}.desktop").absolute()
local_applications_path = pathlib.Path("~/.local/share/applications/").expanduser() / cookiecutter_path.name
print(f"Move {cookiecutter_path.name} => {local_applications_path}{' (overwrite)' if local_applications_path.exists() else ''}? [y/N]")
if input().lower() == 'y':
  local_applications_path.parent.mkdir(parents=True, exist_ok=True)
  cookiecutter_path.rename(local_applications_path)
else:
  cookiecutter_path.rename(
    cookiecutter_path.parent.parent / cookiecutter_path.name
  )

cookiecutter_path.parent.rmdir()
