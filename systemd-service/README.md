# Systemd Service

Create a `.service` file for running a program in the background on startup or on a schedule (with `systemd-timer`)

By default it can install the service as a user service but can just as easily be used to create system services which can be installed to `/etc/systemd/system/application.service`.

Once created and installed, the user service can be managed with `systemctl`--e.g.
```bash
# omit --user and probably add `sudo` when working with global systemd services
systemctl --user start application.service
systemctl --user status application.service
systemctl --user stop application.service
# start/stop on startup
systemctl --user enable application.service
systemctl --user disable application.service
```
