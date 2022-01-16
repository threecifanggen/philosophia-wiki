# 原始和部派佛教

## 主要历史

下图列出对大乘佛学和现代佛学有历史传承的宗部，其他展示在列表中。

```{graphviz}
digraph G {
    node [shape=box]
    subgraph cluster_before {
        label="释迦摩尼之前"
        耆那教 
        婆罗门教
    }

    耆那教 -> 释迦摩尼
    婆罗门教 -> 释迦摩尼

    释迦摩尼 -> 原始佛教
    
    原始佛教 -> 上座部 [label="第二次集结"]
    原始佛教 -> 大众部 [label="第二次集结"]

    subgraph cluster_2nd {
        label="部派佛教"
        大众部
        上座部 -> 说一切有部
        说一切有部 -> 经量部
    }
}
```