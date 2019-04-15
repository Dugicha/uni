# Makefile

CC = gcc
CFLAGS = -Wall -Werror

.PHONY: all
all: itob

itob: itob.c
	$(CC) $(CFLAGS) itob.c -o itob

debug:	itob.c
	$(CC) -Wall -g itob.c -o debug
	gdb -tui debug
