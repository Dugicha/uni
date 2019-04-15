# Makefile

CC = gcc
CFLAGS = -Wall -Werror

.PHONY: all
all: itoa_pad

itoa_pad: itoa_pad.c
	$(CC) $(CFLAGS) itoa_pad.c -o itoa_pad

debug:	itoa_pad.c
	$(CC) -Wall -g itoa_pad.c -o debug
	gdb -tui debug
