CC=gcc
CFLAGS=-Wall -Werror

.PHONY: all
all: invert

.PHONY: g
g: all
	./invert

invert: invert.c
	${CC} ${CFLAGS} invert.c -o invert
