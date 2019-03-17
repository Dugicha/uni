CC=gcc
CFLAGS=-Wall -Werror

.PHONY: all
all: setbits

.PHONY: g
g: all
	./setbits

setbits: setbits.c
	${CC} ${CFLAGS} setbits.c -o setbits
