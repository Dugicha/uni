# Makefile

CC = gcc
CFLAGS = -Wall -Werror

.PHONY: all
all: escape

escape: escape.c
	$(CC) $(CFLAGS) escape.c -o escape

.PHONY: debug
debug: escape.c
	$(CC) -Wall -g escape.c -o debug
	gdb -tui debug

clean:
	rm -rf debug
