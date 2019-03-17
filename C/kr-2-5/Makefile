# Makefile

CC=gcc
CFLAGS=-Wall -O2

.PHONY: all
all: any

any: any.o
	$(CC) $(CLFAGS) any.o -o any

any.o: any.c
	$(CC) $(CLFAGS) -c any.c -o any.o

.PHONY: debug
debug: clean any.c
	$(CC) -Wall -g any.c -o any.gdb
	gdb -tui any.gdb

clean:
	rm -rf *.o
