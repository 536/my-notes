# bat设置路由

需要以`管理员权限`执行命令

+ 假设

  网关是`192.168.20.1`，需要添加`10.10.3.0`网段的路由，掩码是24位

+ 命令

    ```text
    删除路由
    route delete 0.0.0.0 mask 0.0.0.0

    添加临时路由
    route add 10.10.3.0 mask 255.255.255.0 192.168.20.1
    或者
    route add 10.10.3.0/24 192.168.20.1

    添加永久路由
    route add -p 10.10.3.0 mask 255.255.255.0 192.168.20.1
    或者
    route add -p 10.10.3.0/24 192.168.20.1
    ```

    当路由需要绑定指定网卡时

    ```text
    route print
    ```

    > ```text
    > Interface List
    >  15...xx xx xx xx xx xx ......Microsoft Wi-Fi Direct Virtual Adapter
    >  19...xx xx xx xx xx xx ......Netease UU TAP-Win32 Adapter V9.21
    >  21...xx xx xx xx xx xx ......VMware Virtual Ethernet Adapter for VMnet1
    >  16...xx xx xx xx xx xx ......VMware Virtual Ethernet Adapter for VMnet8
    >  10...xx xx xx xx xx xx ......Intel(R) Dual Band Wireless-AC 8265
    >  14...xx xx xx xx xx xx ......Bluetooth Device (Personal Area Network)
    >   1...........................Software Loopback Interface 1
    > ...
    > ```

    如果要绑定到网卡`Intel(R) Dual Band Wireless-AC 8265`（网卡ID：10）

    ```text
    添加临时路由
    route add 10.10.3.0/24 192.168.20.1 if 10
    添加永久路由
    route add -p 10.10.3.0/24 192.168.20.1 if 10
    ```
