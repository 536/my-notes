# libc.so.6 version `GLIBC_2.18' not found

glibc版本需要升级

+ 升级过程

    ```bash
    cd /tmp
    curl -O http://ftp.gnu.org/gnu/glibc/glibc-2.18.tar.gz
    tar zxf glibc-2.18.tar.gz
    cd glibc-2.18/
    mkdir build
    cd build/
    ../configure --prefix=/usr
    make -j2
    make install
    ```

+ 查看依赖

    ```bash
    $ ldd live555MediaServer
        linux-vdso.so.1 (0x00007ffe535e7000)
        libssl.so.10 => /lib64/libssl.so.10 (0x00007feb68278000)
        libcrypto.so.10 => /lib64/libcrypto.so.10 (0x00007feb67e15000)
        libstdc++.so.6 => /lib64/libstdc++.so.6 (0x00007feb6856e000)
        libm.so.6 => /lib64/libm.so.6 (0x00007feb67b13000)
        libgcc_s.so.1 => /lib64/libgcc_s.so.1 (0x00007feb678fd000)
        libc.so.6 => /lib64/libc.so.6 (0x00007feb67551000)
        libgssapi_krb5.so.2 => /lib64/libgssapi_krb5.so.2 (0x00007feb67304000)
        libkrb5.so.3 => /lib64/libkrb5.so.3 (0x00007feb6701b000)
        libcom_err.so.2 => /lib64/libcom_err.so.2 (0x00007feb66e17000)
        libk5crypto.so.3 => /lib64/libk5crypto.so.3 (0x00007feb66be4000)
        libdl.so.2 => /lib64/libdl.so.2 (0x00007feb669e0000)
        libz.so.1 => /lib64/libz.so.1 (0x00007feb667ca000)
        /lib64/ld-linux-x86-64.so.2 (0x00007feb684ea000)
        libkrb5support.so.0 => /lib64/libkrb5support.so.0 (0x00007feb665ba000)
        libkeyutils.so.1 => /lib64/libkeyutils.so.1 (0x00007feb663b6000)
        libresolv.so.2 => /lib64/libresolv.so.2 (0x00007feb6619f000)
        libpthread.so.0 => /lib64/libpthread.so.0 (0x00007feb65f81000)
        libselinux.so.1 => /lib64/libselinux.so.1 (0x00007feb65d5a000)
        libpcre.so.1 => /lib64/libpcre.so.1 (0x00007feb65af8000)
    ```

+ 查看动态链接库的版本

    ```bash
    # strings /lib64/libc.so.6|grep ^GLIBC_
    GLIBC_2.2.5
    GLIBC_2.2.6
    GLIBC_2.3
    ......
    ```

## 参考

<https://blog.csdn.net/huaishuming/article/details/102900254>
