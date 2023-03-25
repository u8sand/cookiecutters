import pathlib

cookiecutter_path = pathlib.Path("{{ cookiecutter.filename }}.network").absolute()
systemd_networkd_path = pathlib.Path("/etc/systemd/network") / cookiecutter_path.name
print(f"Move {cookiecutter_path.name} => {systemd_networkd_path}{' (overwrite)' if systemd_networkd_path.exists() else ''}? [y/N]")
if input().lower() == 'y':
  systemd_networkd_path.parent.mkdir(parents=True, exist_ok=True)
  cookiecutter_path.rename(systemd_networkd_path)
else:
  cookiecutter_path.rename(
    cookiecutter_path.parent.parent / cookiecutter_path.name
  )

cookiecutter_path.parent.rmdir()
