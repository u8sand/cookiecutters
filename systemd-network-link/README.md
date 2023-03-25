# Systemd Networkd: Link

Create a `.link` file for setting up an interface.
This is useful to ensure your interface is always assigned the same name by the kernel and can be used to configure mac randomization & wake on lan.

After installing this configuration file, you'll typically want to configure the link, see `systemd-network-static` or `systemd-network-dhcp`.
