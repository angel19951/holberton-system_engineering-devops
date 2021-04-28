# 0x14. MySQL

Setting up mysql database on servers web-01 and web-02

## Requirements
### General:
- Editor: Nvim
- All files interpreted on Ubuntu 16.04 LTS.
- All files end with a new line.
- A README.md file, at the root of the folder of the project, is present.
- All Bash script files are executable.
- Bash script pass Shellcheck (version 0.3.7-5~ubuntu16.04.1 via apt-get) without any error.
- The first line of all Bash scripts is exactly #!/usr/bin/env bash.
- The second line of all Bash scripts is a comment explaining what is the script doing.

### Shellcheck
#### Installation:
```bash
apt-get update
apt-get install shellcheck
```

#### Usage:

```bash
shellcheck script_test
```

## Tasks
 __** Task 0 - 3 are configurations inside of the provided server **__ 
- Task 0 - Install MySQL in a server
    - [Task 0]()
- Task 1 - Create a user and password for both MySQL databases which will allow the checker access to them.
    - [Task 1]()
- Task 2 - Create a database named ___tyrell_corp___  and within a table named ___nexus6___.
    - [Task 2]()
- Task 3 - Create ___replica_user___ and granting the correct privileges.
    - [Task 3]()
- Task 4 - MySQL config for primary and replica.
    - [Task 4 (Primary)](https://github.com/angel19951/holberton-system_engineering-devops/blob/master/0x14-mysql/4-mysql_configuration_primary)
    - [Task 4 (Replica)](https://github.com/angel19951/holberton-system_engineering-devops/blob/master/0x14-mysql/4-mysql_configuration_replica)
- Task 5 - Bash script that generates a MySQL dump and creates a compressed archive out of it.
    - [Task 5]()
