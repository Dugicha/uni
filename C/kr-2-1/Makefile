# Makefile

CC=gcc
CFLAGS=-Wall -o2

.PHONY: all
.PHONY: clean

all: main

main: main.o
	$(CC) $(CFLAGS) -o main main.o

main.o: main.c
	$(CC) $(CFLAGS) -c -o main.o main.c

debug: clean main.c
	$(CC) -Wall -g -o test main.c
	gdb -tui test

clean:
	rm -rf *.o main
