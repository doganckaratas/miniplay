CC=gcc
CFLAGS=-I../include -Wall -Werror -Wextra -pedantic -g -ggdb -O0
SRCS=$(wildcard *.c)
OBJS=$(SRCS:.c=.o)
DEPS=$(OBJS:.o=.d)

.PHONY: all
all:	$(OBJS)

$(DEPS): %.d:%.c
	$(CC) $(CFLAGS) -MM $< >$@

$(OBJS): $(SRCS)
	$(CC) $(CFLAGS) -c $^

-include $(DEPS)

.PHONY: clean
clean:
	rm -rf $(OBJS) $(DEPS)
