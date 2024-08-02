FROM ubuntu:20.04


RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    libtool \
    pkg-config \
    autoconf \
    automake \
    libssl-dev \
    libevent-dev \
    bsdmainutils \
    libzmq3-dev \
    libdb-dev \
    libdb++-dev \
    libboost-all-dev


WORKDIR /app


RUN git clone https://github.com/syscoin/syscoin.git . && \
    git checkout master && \
    git submodule update --init --recursive && \
    ./autogen.sh && \
    ./configure --without-gui --disable-tests --disable-bench && \
    make && \
    make install


EXPOSE 8369 18369 28369 8370


CMD ["syscoind"]
