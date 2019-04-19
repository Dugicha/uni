# Makefile
CC = gcc
CFLAGS = -Wall -Werror

.PHONY: all
all: polish

polish: main.o getop.o charstack.o calcstack.o
	$(CC) $(CFLAGS) -o polish main.o getop.o charstack.o calcstack.o -lm

main.o: main.c getop.h calcstack.h
	$(CC) $(CFLAGS) -c main.c -o main.o

getop.o: getop.c getop.h charstack.h
	$(CC) $(CFLAGS) -c getop.c -o getop.o

charstack.o: charstack.c
	$(CC) $(CFLAGS) -c charstack.c -o charstack.o

calcstack.o: calcstack.c
	$(CC) $(CFLAGS) -c calcstack.c -o calcstack.o

.PHONY: clean
clean:
	rm -rf *.o
