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

Require Ansible >= 2.5

### Dependencies

* roles

| Name                                                                                   | Description                                  |
| -------------------------------------------------------------------------------------- | -------------------------------------------- |
| [ansible-zabbix-agent](https://github.com/Turgon37/ansible-zabbix-agent)               | If you use the zabbix monitoring profile     |
| [ansible-prometheus-exporter](https://github.com/Turgon37/ansible-prometheus-exporter) | If you use the prometheus monitoring profile |

## OS Family

This role is available for Debian

## Features

At this day the role can be used to :

  * install apcupsd packages
  * perform a minimal configuration (advanced one is planned)
  * monitoring items for
    * Zabbix
    * Prometheus
  * [local facts](#facts)

## Configuration

All variables which can be overridden are stored in [defaults/main.yml](defaults/main.yml) file as well as in table below. To see default values please refer to this file.

| Name                         | Types/Values | Description                                                                  |
| ---------------------------- | ------------ | ---------------------------------------------------------------------------- |
| `apcupsd__facts`             | Boolean      | Install the local fact script                                                |
| `apcupsd__monitoring`        | String/List  | The name of the monitoring "profile" to use. Available 'zabbix','prometheus' |
| `apcupsd__service_enabled`   | Boolean      | Enable or not all instances' services                                        |
| `apcupsd__instances`         | Boolean      | Dict of apcupsd instances (see below)                                        |
| `apcupsd__instance_defaults` | Dict         | Hash of default variables for all instance                                   |

* Per instance variables

To declare an apcupsd instance, use the apcupsd__instances variable (refer to [exemple below](#example))

| Name                 | Types/Values    | Description                                                                              |
| -------------------- | --------------- | ---------------------------------------------------------------------------------------- |
| `net_server`         | Boolean         | Boolean to enable or not the nis server, it allow network client to query the UPS status |
| `net_server_address` | String          | The network address on which the nis server will listen to                               |
| `net_server_port`    | String          | The network port on which the nis server will listen to                                  |
| `upscable`           | String          | see apcupsd.conf doc                                                                     |
| `upstype`            | String          | see apcupsd.conf doc                                                                     |
| `device`             | String          | see apcupsd.conf doc                                                                     |
| `polltime`           | String          | see apcupsd.conf doc                                                                     |
| `upsclass`           | String          | see apcupsd.conf doc                                                                     |
| `upsmode`            | String          | see apcupsd.conf doc                                                                     |
| `eventsfilemax`      | String          | see apcupsd.conf doc                                                                     |
| `scripts`            | List of scripts | Define events handlers scripts(see below)                                                |

* Scripts handlers

Each apcupsd instance supports multiple scripts handlers, using the `scripts` variable in instance configuration you can define spec like this

```
scripts:
- name: http_hook
  event: all
  content: |
    [script content]
```

The `name` is free form but must be unique per event value.
Content is the script's raw `content`, this will be put in an executable file and will be called each time `event` is triggered.
`event` must be a single string with one of availables event

As an exemple, the following events exists
`killpower commfailure commok powerout onbattery offbattery mainsback failing timeout loadlimit runlimit doreboot doshutdown annoyme emergency changeme remotedown startselftest endselftest battdetach battattach`

### Monitoring

You can enable one or more monitoring backend using `apcupsd__monitoring` variable.

#### Zabbix

#### Prometheus

| Name                                | Types/Values | Description                                                                   |
| ----------------------------------- | ------------ | ----------------------------------------------------------------------------- |
| `apcupsd_exporter__version`         | String       | Which exporter version do you want                                            |
| `apcupsd_exporter__web_listen_host` | String       | Hostname on which prometheus exporter per instance will listen on             |
| `apcupsd_exporter__web_listen_port` | Integer      | Starting port number on which prometheus exporter per instance will listen on |
| `apcupsd_exporter__web_path`        | String       | Url prefix on which prometheus exporter will serve metrics                    |
| `apcupsd_exporter__network`         | String       | Network stack to use in prometheus exporter                                   |

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
apcupsd__instances:
  ups01:
    polltime: 10
    scripts:
      - name: http_hook
        event: all
        content: |
          #!/bin/bash
          curl --output - \
            https://api.net/ \
            --data-urlencode 'api=key'
```
