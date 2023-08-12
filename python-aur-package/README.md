# python-aur-package

This cookiecutter makes AUR packages (buildable and pacman installable) for python packages on pypi. It automatically fills in basically everything with the help of the pypi API. Once done, the directory can be built with:

```bash
# build the package, syncing any dependencies
makepkg -s
# install the package
sudo pacman -U *.tar.xz
```

If you want to publish it, you should replace
```
sha256sums=('SKIP')
```
with whatver you get from
```
makepkg --geninteg
```

...and add author/maintainence information.
