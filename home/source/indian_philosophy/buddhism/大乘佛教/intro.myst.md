# 大乘出现与之后


## 印度大乘佛学基本历史

```{uml}
state "经量部" as a1
state "说一切有部" as a2
state "唯识派" as a {
    state "唯识派经典来源" as a_1 <<inputPin>>
}
state "中观派" as b {
    state "中观派经典来源" as b_1 <<inputPin>>
}
state "般若经" as c1
state "解深密经" as c2
state "楞伽经" as c3 
state "阿毗达摩论" as c4
state "如来藏派" as d
state "密宗" as e

a2 --> a1
a2 -down-> a
c1 -down-> b_1
a1 -down-> a

c2 -down-> a_1
c3 -down-> a_1
c4 -down-> a_1

a --> d
b --> d

d -down-> e
a -down-> e
```

## 一些澄清

### 大乘优于小乘？

现在是被普遍质疑的结论，大部分的证据是：在印度大小乘基本在一个寺庙进行修行，不同人可以做不同的选择。

### 大乘是否是印度显学？

有观点认为，大乘在印度的兴盛时期很多，而正好因为玄奘取经时的时机恰逢大乘以及那烂陀寺最兴盛的时候，使得对于「大小乘」以及大乘的发展这种史学观念被带到中国。
