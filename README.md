Ansible Role APC UPS Daemon
=========

:warning: This role is under development, some important (and possibly breaking) changes may happend. Don't use it in production level environments but you can eventually base your own role on this one :hammer:

:grey_exclamation: Before using this role, please know that all my Ansible roles are fully written and accustomed to my IT infrastructure. So, even if they are as generic as possible they will not necessarily fill your needs, I advice you to carrefully analyse what they do and evaluate their capability to be installed securely on your servers.

**This roles configure the apcups daemon to monitor an UPS of APC brand.**

## Features

Currently this role provide the following features :

  * apcupsd installation
  * minimal configuration
  * monitoring items for
    * Zabbix
  * [local facts](#facts)

## Requirements

### OS Family

This role is available for Debian only

### Dependencies

If you use the zabbix monitoring profile you will need the role [ansible-zabbix-common](https://github.com/Turgon37/ansible-zabbix-common)


## Role Variables

The variables that can be passed to this role and a brief description about them are as follows:

| Name                     | Types/Values | Description                                                                                                                                              |
| -------------------------| -------------|--------------------------------------------------------------------------------------------------------------------------------------------------------- |
| apcupsd__facts           | Boolean | Install the local fact script                                                                                                                                 |
| apcupsd__monitoring      | String  | The name of the monitoring "profile" to use. Available 'zabbix')                                                                                              |
| apcupsd__service_enabled | Boolean | Enable or not the service                                                                                                                                     |
| apcupsd__nis_enabled   | Boolean | Boolean to enable or not the nis server, it allow network client to query the UPS status                                                                       |
| apcupsd__nis_address   | String  | The network address on which the nis server will listen to                                                                                                     |
| apcupsd__nis_port      | String  | The network port on which the nis server will listen to                                                                                                        |
| apcupsd__custom_header | String  | A optional string to put in the first line of the configuration file. Usefull to set to '## apcupsd.conf v1.1 ##' only is you use apcupsd with Jeedom appliance|

## Facts

By default the local fact are installed and expose the following variables :


* ```ansible_local.apcupsd.version_full```
* ```ansible_local.apcupsd.version_major```


## Example Playbook

To use this role create or update your playbook according the following example :


```
    - hosts: servers
      roles:
         - apcupsd
```


## License

MIT