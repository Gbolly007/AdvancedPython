# Advanced Python Programming - Assignment 1

# 1. 'Shell creator'.
Write a program that runs "shell" commands within your program and immediately throws what's on its stdout; line-by-line. Once command is done, it waits for another command to be typed. (hint: cd will not change your working directory in the most simple implementation).

# 2. 'Path screwer'.
Extend your shell so that cd works as expected (hint: cd might not support any ags or options, just "keep it simple, stupid"). Current working directory should appear in your shell prompt where each dirname is shortened to one character (or two, if dir's name start with .

# 3. 'Hard-boiled sysadmin'.
Extend your shell so that it logs all the actions and useful information back into myshell.log. That includes: timestamp, command name, its arguments, lines of output, pid and exit code.

# 4. 'CCleaner'. (first C from CLI)
Again, extend your shell so that if a command encounters any error it wouldn't put it back into stdout. Instead, pipe the error stream into myshell.stderr file and keep stdout clean.

# 5. 'Pedant coder'
Whatever you've written or googled on the web, rewrite your shell using subprocess module which is (obviously) part of the standard library and supposed to replace several older modules for process management. 
