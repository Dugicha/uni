# Makefile

CC = gcc
CFLAGS = -Wall -Werror

.PHONY: all
all: expand

expand: expand.c
	$(CC) $(CFLAGS) expand.c -o expand

debug:	expand.c
	$(CC) -Wall -g expand.c -o debug
	gdb -tui debug
