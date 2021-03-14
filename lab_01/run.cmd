@ECHO OFF
CHCP 65001
gcc -c -Wall -Werror -Wpedantic main.c io.c calc.c
gcc -o app.exe main.o io.o calc.o