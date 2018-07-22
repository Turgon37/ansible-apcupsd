Ansible Role APC UPS Daemon
=========

[![Build Status](https://travis-ci.org/Turgon37/ansible-apcupsd.svg?branch=master)](https://travis-ci.org/Turgon37/ansible-apcupsd)
[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Ansible Role](https://img.shields.io/badge/ansible%20role-Turgon37.apcupsd-blue.svg)](https://galaxy.ansible.com/Turgon37/apcupsd/)

:warning: This role is under development, some important (and possibly breaking) changes may happend. Don't use it in production level environments but you can eventually base your own role on this one :hammer:

## Description

:grey_exclamation: Before using this role, please know that all my Ansible roles are fully written and accustomed to my IT infrastructure. So, even if they are as generic as possible they will not necessarily fill your needs, I advice you to carrefully analyse what they do and evaluate their capability to be installed securely on your servers.

This roles configure the apcups daemon to monitor an UPS of APC brand.

## Requirements

Require Ansible >= 2.4

### Dependencies

If you use the zabbix monitoring profile you will need the role [ansible-zabbix-agent](https://github.com/Turgon37/ansible-zabbix-agent)

## OS Family

This role is available for Debian

## Features

At this day the role can be used to :

  * install apcupsd packages
  * perform a minimal configuration (advanced one is planned)
  * monitoring items for
    * Zabbix
  * [local facts](#facts)

## Configuration

All variables which can be overridden are stored in [defaults/main.yml](defaults/main.yml) file as well as in table below. To see default values please refer to this file.

| Name                          | Types/Values | Description                                                                              |
| ----------------------------- | -------------|------------------------------------------------------------------------------------------|
| `apcupsd__facts`              | Boolean      | Install the local fact script                                                            |
| `apcupsd__monitoring`         | String       | The name of the monitoring "profile" to use. Available 'zabbix')                         |
| `apcupsd__service_enabled`    | Boolean      | Enable or not the service                                                                |
| `apcupsd__net_server`         | Boolean      | Boolean to enable or not the nis server, it allow network client to query the UPS status |
| `apcupsd__net_server_address` | String       | The network address on which the nis server will listen to                               |
| `apcupsd__net_server_port`    | String       | The network port on which the nis server will listen to                                  |

## Facts

By default the local fact are installed and expose the following variables :


* ```ansible_local.apcupsd.version_full```
* ```ansible_local.apcupsd.version_major```

## Example

### Playbook

Use it in a playbook as follows:

```yaml
- hosts: all
  roles:
    - turgon37.apcupsd
```

### Inventory

```
apcupsd__net_server_address: 127.0.0.1
```