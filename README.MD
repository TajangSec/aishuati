fork自：https://github.com/moke8/aishuati

在此感谢[moke8](https://github.com/moke8)大佬，我已顺利入职白马会所运维岗

由于原作者已不更新，issue荒废，所以我fork了仓库

相关特色，界面，功能可以去源仓库查看

生成json后，在主目录直接起个http服务就可以刷题，起服务的话，python最简单，直接`python -m http.server`



修复了一些bug，比如题干中包含空格和字母，他会解析错误，把题干部分字母解析到选项里，比如把：

```
TCP/IP 的第四层有两个协议，分别是 TCP 和 UDP，TCP 协议的特点是什么？
UDP 协议的特点是什么？______( 1 分 )
A：TCP 提供面向连接的路服务，UDP 提供无连接的数据报服务
B：TCP 提供面向连接的路服务，UDP 提供有连接的数据报服务
C：UDP 提供面向连接的路服务，TCP 提供有连接的数据报服务
D：UDP 提供面向连接的路服务，TCP 提供无连接的数据报服务
答案： A
```

解析成：

```
"id": "202506060948393552",
        "title": "TCP/IP 的第四层有两个协议，分别是 TCP 和 UDP，TCP 协议的特点是什么？UDP 协议的特点是什么？______( 1 分 )",
        "option": [
            "P/IP",
            "P",
            "P，TCP",
            "P",
            "：TCP",
            "P",
            "：TCP",
            "P",
            "：UDP",
            "P",
            "：UDP",
            "P"
        ],
        "answer": "A",
        "analysis": ""
```

把：

```
下列哪一个是常用的防范（）NetBIOS 漏洞攻击的方法( 1 分 )
A：利用 ICP/IP 筛选
B：卸载 NetBIOS
C：绑定 NetBIOS 与 TCP/IP 协议
D：用防病毒软件
答案： A
```

解析成：

```
"id": "202506060948637221",
        "title": "下列哪一个是常用的防范（）NetBIOS 漏洞攻击的方法( 1 分 )",
        "option": [
            "IOS",
            "：利用",
            "P/IP",
            "：卸载",
            "IOS",
            "：绑定",
            "IOS",
            "P/IP",
            "：用防病毒软件"
        ],
        "answer": "A",
        "analysis": ""
```

