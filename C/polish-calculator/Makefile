#
#
#
CC=gcc
CFLAGS=-Wall


all : polish_calc
.PHONY : all

polish_calc : polish_calc.o getop.o stack.o getch.o
	$(CC) $(CFLAGS) -o polish_calc polish_calc.o getop.o stack.o getch.o

polish_calc.o : main.c 
	$(CC) $(CFLAGS) -c -o polish_calc.o main.c	

getop.o : getop.c
	$(CC) $(CFLAGS) -c -o getop.o getop.c
	
stack.o : stack.c
	$(CC) $(CFLAGS) -c -o stack.o stack.c
	
getch.o : getch.c
	$(CC) $(CFLAGS) -c -o getch.o getch.c

debug : clean main.c
	$(CC) $(CFLAGS) -g -o test main.c getop.c stack.c getch.c
	gdb -tui  test

	
	
.PHONY: clean
clean : 
	rm -rf *.o test
	

