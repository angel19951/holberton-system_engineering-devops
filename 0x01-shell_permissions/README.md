Tutorial on shell permissions.

su - changes your user ID
whoami - prints the effective userid
groups -  prints all the groups
chown [new owner] [filename] -  changes the owner of the file
touch - create an empty file
chmod u+x - makes a executable file
chmod ug+x,o+r [filename] - execute permission to the owner and the group owner, and read permission to other users
chmod ugo+x [filename] - adds execution permission to the owner
chmod 007 [filename] -  sets the mode of the file
chmod 753 [filename] -  sets the mode of the file
chmod --reference=[new mode] [oldfile] -  sets the mode of the file to olleh
chmod a+x */ - adds execute permission to all subdirectories
