# Systemd Networkd: DHCP

Create a `.network` file for setting up dhcp on an interface.
This can be used after configuring a `.link`, see `systemd-network-link`

After installing this configuration file, you can: `systemctl enable --now systemd-networkd`
