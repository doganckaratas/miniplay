TARGET=miniplay-ng
INSTALL=_install
CC=gcc
MAKE=make
CFLAGS=-I./include -g -ggdb -O0
SRCS+=$(wildcard ./src/*.c)
SRCS+=$(wildcard ./*.c)
OBJS=$(SRCS:.c=.o)
DEPS=$(OBJS:.o=.d)

.PHONY: all
all:	$(TARGET)

.PHONY: clean
clean:
	$(MAKE) -C src clean V=1
	find -name '*.gch' -delete
	rm -rf $(TARGET).o
	rm -rf $(TARGET)

.PHONY: distclean
distclean: clean
	rm -rf $(TARGET)
	rm -rf $(INSTALL)

.PHONY: install
install: all
	mkdir -p $(INSTALL)
	cp -frv $(TARGET) $(INSTALL)

$(TARGET): 
	$(MAKE) -C src all V=1
	$(CC) $(CFLAGS) -c $@.c
	$(CC) $(CFLAGS) -o $@ ${OBJS}
