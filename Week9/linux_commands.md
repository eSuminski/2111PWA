### Global Regular Expression Print(GREP)
Global Regular Expression Print (GREP) is a way to search for a specific string in one or more files. All you need to do this is use the grep command, the string you want, and the files you want to search through
```cli
grep word file1 file2 file3 etc
```
You can put your string in quotes to get an exact phrase
```cli
grep "my phrase here" file1 file2 file3 etc
```
You can use an * to indicate you want to look for your string in all files within the current directory
```cli
grep word *
```
You can appened -w to the grep command to only find whole words (can't be a substring)
```cli
grep -w word file1 file2 file3 etc
```
you can appened -i to the grep command to ignore case
```cli
grep -1 word *
```
you can append -r to also search sub directories of the currrent directory
```cli
grep -r word *
```
### Manual (man)
You can use the man command, along with another command, to see the user manual for the selected command. This includes name, the synopsis, options for the command, a description, exit status, possible return values, fil, possible errors, authors, and examples.
### Yellowdog Update modifier (yum)
Yellowdog Update Modifier (YUM) is a Redhat Package Manager (RPM) that we use with Linux. Similar to pip and maven, yum handles package installations and updates for our linux machine. The basic commands you are going to use with yum are install, update, list, and search.
## Unix Basics (basic shell scripting)
Working inside the EC2 instance requires some basic shell scripting knowledge. Note that some commands may require you to use the sudo keyword (superuser do). This allows for you to run commands only the administrator or root user could normally do. Here are some of the commands we will constantly be using
- ls lists contents of the current directory (different linux systems have different colors for directories and files). You can also us ls -R to list the subdirectories within the ls results, and you can use ls -a to see hidden files
```cli
ls
ls -R
ls -a
```
- the cat > command is used to create a new file. Once you create the file you will be prompted to fill it with text. When finished you click ctr + d to return to command prompt
```cli
cat > filename.extension
```
```cli
can add text to file if you wish, ctr + d to exit
```
you can just use the cat command to view a file
```cli
cat filename
```
you can use the rm command to remove a file (no confirmation or warning provided)
```cli
rm file
```
you can use the mv command to move a file to a new location
```cli
mv file /new/location/path
```
you can also use the mv command to rename a file
```cli
mv oldfilename newfilename
```
you can use mkdir to create a new directory, or indicate a path to where the new directory will be
```cli
mkdir newdirectory
mkdir /path/to/new/directory
```
you can use the rmdir command to delete a directory. May fail if there are subdirectories
```cli
rmdir mydirectory
```
the clear command removes all the previous entries in the terminal, giving you a clean screen to work with
```cli
clear
```
the history command will print a list of all the commands entered in the current session
```cli
history
```