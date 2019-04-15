# Makefile

CC = gcc
CFLAGS = -Wall -Werror

.PHONY: all
all: itoa

itoa: itoa.c
	$(CC) $(CFLAGS) itoa.c -o itoa

debug:	itoa.c
	$(CC) -Wall -g itoa.c -o debug
	gdb -tui debug
