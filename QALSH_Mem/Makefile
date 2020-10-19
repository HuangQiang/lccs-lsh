SRCS=random.cc util.cc pri_queue.cc kd_rect.cc kd_node.cc kd_tree.cc \
	qalsh.cc qalsh_plus.cc ann.cc main.cc
OBJS=${SRCS:.cc=.o}

CXX=g++ -std=c++11
CPPFLAGS=-w -O3

.PHONY: clean

all: ${OBJS} libqalsh.a
	${CXX} ${CPPFLAGS} -o qalsh ${OBJS}


libqalsh.a: random.o pri_queue.o kd_rect.o kd_node.o kd_tree.o  qalsh.o qalsh_plus.o ann.o
	ar rcs -o libqalsh.a $^ ${LIBS}

random.o: random.h

util.o: util.h

pri_queue.o: pri_queue.h

kd_rect.o: kd_rect.h

kd_node.o: kd_node.h

kd_tree.o: kd_tree.h

qalsh.o: qalsh.h

qalsh_plus.o: qalsh_plus.h

ann.o: ann.h

main.o:

clean:
	-rm ${OBJS} qalsh
