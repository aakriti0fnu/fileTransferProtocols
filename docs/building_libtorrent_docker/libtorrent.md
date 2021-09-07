#### Not in use!
Tried to implement libtorrent, but put it for future developement.

- building libtorrent python bindings on ubuntu20.04
    
    Note:
    1. install libssl
    (libssl is the portion of OpenSSL which supports TLS ( SSL and TLS Protocols ), and depends on libcrypto, 
    OpenSSL is a toolkit for supporting cryptography. The openssl-devel package contains include files needed 
    to develop applications which support various cryptographic algorithms and protocols.)
    `sudo apt-get install -y wget libssl-dev`
    2. install [Boost provides C++ Libraries](https://github.com/boostorg/boost)
    - Download it `wget https://dl.bintray.com/boostorg/release/1.75.0/source/boost_1_75_0.tar.bz2`, untar it `tar --bzip2 -xf boost_1_75_0.tar.bz2`
    - navigate to `boost/tools/build` run `sh bootstrap.sh` 
    - `sudo mv boost /usr/local/lib` then Setup environment variable, it will tells b2 where it can find boost-build, your configuration file and all the toolsets (descriptions used by boost-build to know how to use different compilers on different platforms).
    put it in `vi ~/.bashrc` or `vi ~/.zshrc`(depending on which shell you're using) file
    ```shell
    export PATH="/usr/local/lib/boost_1_75_0/tools/build:$PATH"
    export BOOST_BUILD_PATH="/usr/local/lib/boost_1_75_0/tools/build"
    export BOOST_ROOT="/usr/local/lib/boost_1_75_0/"

    ```
    You can check whether the environment variables have been set `printenv BOOST_BUILD_PATH BOOST_ROOT`. Now you have b2 installed.
    - Create a file `touch ~/user-config.jam` in your home directory.   

    3. install [libtorrent: C++ library implementing the BitTorrent protocol](https://github.com/arvidn/libtorrent)
    Note:(You'll need at least version 1.66 of the boost library in order to build libtorrent)
    - Setup the python interpreter in `user-config.jam`
    `using python : 3.8 : /home/aakriti/anaconda3/bin/python ;`
    - Download `git clone --depth 1 --single-branch --branch RC_2_0 --recurse-submodules https://github.com/arvidn/libtorrent.git`
    - Navigate to `/home/aakriti/Documents/github/libtorrent/bindings/python`, and invoke `b2`
    
    `b2 libtorrent-link=static boost-link=static stage_module`
    `b2 install_module python-install-path=/home/aakriti/anaconda3/lib/python3.8/site-packages`
    
    it's not building!

    - Alternative way is to build libtorrent using docker by switching to `libtorrent/` using command `docker build -f Dockerfile -t libtorrent:latest .`
    ```shell
    REPOSITORY                          TAG       IMAGE ID       CREATED         SIZE
    libtorrent                          latest    6a320c0e3eb7   6 hours ago     5.21GB
    ```
    The running container using command `docker run --name libtorrent-container -it libtorrent:latest /bin/bash`
    ```shell
    root@15e2a9778f03:/src/libtorrent# pwd
    /src/libtorrent
    ```


    - setting up VMs


# Reference:
- https://github.com/arvidn/libtorrent/blob/RC_2_0/docs/building.rst
- https://github.com/arvidn/libtorrent/blob/RC_2_0/docs/python_binding.rst#using-libtorrent-in-python

- https://github.com/KimiNewt/pyshark/

Docker
- https://github.com/google/oss-fuzz/tree/master/projects/libtorrent
