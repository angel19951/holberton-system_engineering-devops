# 0x0A Configuration management

## General:
 - All files created, updated and managed on Ubuntu 14.04LTS.
 - All file end in new line.
 - Puppet manifests must pass puppet-lint version 2.1.1 without any errors.
 - puppet manifests must run without errors.
 - Puppet manifests first line must be a comment explaining what the Puppet manifest is about.
 - Puppet manifests files must end with the extension .pp.

## Installing puppet-lint:

Use the package manager [puppet](https://joachim8675309.medium.com/installing-puppet-5-427ca7a68f02) to install puppet-lint.

```bash
$ sudo apt-get install -y ruby
$ sudo gem install puppet-lint -v 2.1.1
```
 >> Note: use sudo commands only when necessary or at your risk

## Usage example:

```shell
$ puppet-lint --version
puppet-lint 2.1.1

$ puppet-lint manifest_name.pp

$ puppet apply manifest_name.pp
Notice: Compiled catalog for d391259bf577.hsd1.ca.comcast.net in environment 
production in 0.01 seconds
```

## Tasks:
### 0. Create a file using puppet
 - [Task 0](https://github.com/angel19951/holberton-system_engineering-devops/blob/master/0x0A-configuration_management/0-create_a_file.pp)

### 1. Install puppet-lint using puppet
 - [Task 1](https://github.com/angel19951/holberton-system_engineering-devops/blob/master/0x0A-configuration_management/1-install_a_package.pp)

### 2. Kill a specific process using puppet
 - [Task 2]()
