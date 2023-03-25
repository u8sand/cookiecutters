import re
import pathlib

cookiecutter_path = pathlib.Path("{{ cookiecutter.filename }}").absolute()
local_ssh_config = pathlib.Path("~/.ssh/config").expanduser()
local_ssh_config_orig = local_ssh_config.with_suffix('.orig')
print(f"Add {cookiecutter_path.name} to {local_ssh_config} (current config will be saved as {local_ssh_config_orig})? [y/N]")
if input().lower() == 'y':
  local_ssh_config.rename(local_ssh_config_orig)
  with local_ssh_config.open('w') as fw:
    with local_ssh_config_orig.open('r') as fr:
      current_host = False
      for line in fr:
        if line.startswith(f"Host {{ cookiecutter.host }}"):
          current_host = True
        elif current_host and not re.match(r'^\s+', line):
          current_host = False
        elif current_host:
          continue
        else:
          fw.write(line)
    if line != '\n': fw.write('\n')
    with cookiecutter_path.open('r') as fr:
      for line in fr:
        fw.write(line)
    if line != '\n': fw.write('\n')
  cookiecutter_path.unlink()
else:
  cookiecutter_path.rename(
    cookiecutter_path.parent.parent / cookiecutter_path.name
  )

cookiecutter_path.parent.rmdir()
