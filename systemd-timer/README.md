# Systemd Timer

Create a `.timer` file for scheduling a service to run on a schedule. It should be named the same as the service you wish to schedule. To make the service, see `systemd-service`.

For more information on the `on_calendar` format, see <https://www.freedesktop.org/software/systemd/man/systemd.time.html>.

A `persistent` timer, is one which will be triggered when your computer turns back on or wakes back up if the on_calendar event happened while your computer was off or asleep.

Once created you'll need to enable it:
```bash
# omit --user and probably add `sudo` when working with global systemd services
systemctl --user daemon-reload
# start/stop timer
systemctl --user enable application.timer
systemctl --user disable application.timer
```
