# Oven

Oven is a simple program that allows you to place a file in the input folder and have a command automatically executed on it as soon as the file is placed in the folder, the file is then deleted.

E.g:
>["cat ","'{fullPath}'"]

Placeholders include:

{filename} - Gives the raw name of the input file

{fullPath} - Gives the relative path to the input file


This program is especially useful for things such as compile farms (you could just drop a file onto a server and have it spit out a compiled version into the output folder) by doing something like:
>["nasm ","{fullPath} -f bin -o ./output/{filename}.bin"]

The syntax being

>["COMMAND NAME","ARGUMENTS"]

To set the command to use just change the line "cmdToExec               =..." to "cmdToExec               ="YOUR COMMAND" "
