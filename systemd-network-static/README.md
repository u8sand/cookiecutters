# Systemd Networkd: Static IP Address

Create a `.network` file for setting up a static ip on an interface.
This can be used after configuring a `.link`, see `systemd-network-link`

After installing this configuration file, you can: `systemctl enable --now systemd-networkd`
