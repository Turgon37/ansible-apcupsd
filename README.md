Ansible Role APC UPS Daemon
========

:warning: This role is under development

This roles configure an apcups daemon to monitor an UPS of APC brand

## OS Family

This role is available for Debian

## Features

At this day the role can be used to configure :

  * apcupsd installation and configuration

## Configuration

The variables that can be passed to this role and a brief description about them are as follows:

| Name                 | Description                                                                             |
| ---------------------| --------------------------------------------------------------------------------------- |
| apcupsd__nis_enabled | Boolean to enable or not the nis server, it allow network client to query the UPS status|
| apcupsd__nis_address | The network address on which the nis server will listen to                              |
| apcupsd__nis_port    | The network port on which the nis server will listen to                                 |


### Example

  * Example

```

```