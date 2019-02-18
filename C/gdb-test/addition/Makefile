# Makefile

CC=gcc
CFLAGS=-Wall -o2

.PHONY: all
.PHONY: clean

all: addition

addition: addition.o
	$(CC) $(CFLAGS) -o addition addition.o

addition.o: addition.c
	$(CC) $(CFLAGS) -c -o addition.o addition.c

debug: clean addition.c
	$(CC) -Wall -g -o test addition.c
	gdb -tui test

clean:
	rm -rf *.o
