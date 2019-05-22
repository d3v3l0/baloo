OS = $(shell uname -s)

ifeq (${OS}, Darwin)
	LIB = libudf_c.dylib
else ifeq (${OS}, Linux)
	LIB = libudf_c.so
else
  $(error Unsupported platform: ${OS})
endif

all:
	clang++ -shared -fPIC -w udf_c.cpp -o $(LIB)

clean:
	rm -rf $(LIB)
