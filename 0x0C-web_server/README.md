# 0x0C. Web server

In this project, some of the tasks will be graded on 2 aspects:

1. Is your web-01 server configured according to requirements.
2. Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention).

For example, if I need to create a file /tmp/test containing the string hello world and modify the configuration of Nginx to listen on port 8080 instead of 80, I can use emacs on my server to create the file and to modify the Nginx configuration file /etc/nginx/sites-enabled/default.

But my answer file would contain:

```bash
vagrant@ubuntu-xenial$: cat 88-script_example
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world > /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
vagrant@ubuntu-xenial$:
```

As you can tell, I am not using emacs to perform the task in my answer file. This exercise is aiming at training you on automating your work. If you can automate tasks that you do manually, you can then automate yourself out of repetitive tasks and focus your energy on something more interesting. For an SRE, that comes very handy when there are hundreds or thousands of servers to manage, the work cannot be only done manually. Note that the checker will execute your script as the root user, you do not need to use the sudo command.

>> Some Bash scripts were created and tested in a docker environment.
>> - Ubuntu: 16.04 Docker container

## Learning Objectives:
### General:
 - What is the domain role of a web server.
 - What is a child process.
 - Why web servers have parent process and child processes
 - What are the main HTTP requests
### DNS:
 - What DNS stands for.
 - What is DNS main role.
### DNS Record Types:
 - A
 - CNAME
 - TXT
 - MX

### Requirements:
 - Editor: Nvim.
 - Files created, tested and managed in a Ubunutu 16.04 LTS.
 - All files end in new line.
 - Read me file is present on root.
 - Bash script must pass shellcheck (version 0.3.7) without errors.
 - First line of Bash script is exactly #!/usr/bin/env bash.
 - Second line of Bash script is a comment of what each script is doing.
 - ___Systemctl___  is not permitted to restart a process.

## Shellcheck install:
- Debian based distros:
```bash
$ apt-get install shellcheck
```
- For a Docker hub:
```bash
docker run --rm -v "$PWD:/mnt" koalaman/shellcheck:stable myscript
# Or :v0.4.7 for that version, or :latest for daily builds
```
>> For more information on [Shellcheck](https://github.com/koalaman/shellcheck) click [here](https://github.com/koalaman/shellcheck)
## Tasks:
### 0. Bash script that transfers a file from client to a server
- [Task 0]()
### 1. Install nginx in a web server
- [Task 1]()
### 2. Set up a domain name
- [Task 2]()
### 3. Configure Nginx server so that is redirected to another page
- [Task 3]()
### 4. Configure your Nginx server to have a custom 404 page that contains the string "_Ceci n'est pas une page_".
- [Task 4]()
