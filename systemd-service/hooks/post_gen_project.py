import pathlib

cookiecutter_path = pathlib.Path("{{ cookiecutter.filename }}.service").absolute()
local_systemd_path = pathlib.Path("~/.config/systemd/user/").expanduser() / cookiecutter_path.name
print(f"Move {cookiecutter_path.name} => {local_systemd_path}{' (overwrite)' if local_systemd_path.exists() else ''}? [y/N]")
if input().lower() == 'y':
  local_systemd_path.parent.mkdir(parents=True, exist_ok=True)
  cookiecutter_path.rename(local_systemd_path)
else:
  cookiecutter_path.rename(
    cookiecutter_path.parent.parent / cookiecutter_path.name
  )

cookiecutter_path.parent.rmdir()
