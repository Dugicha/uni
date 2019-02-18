# Makefile

CC=gcc
CFLAGS=-Wall -o2

.PHONY: all
.PHONY: clean

all: occurences

occurences: occurences.o
	$(CC) $(CFLAGS) -o occurences occurences.o

occurences.o: occurences.c
	$(CC) $(CFLAGS) -c -o occurences.o occurences.c

debug: clean occurences.c
	$(CC) -Wall -g -o test occurences.c
	gdb -tui test

clean:
	rm -rf *.o
