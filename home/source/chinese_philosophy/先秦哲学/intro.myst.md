# 先秦哲学


## 先秦哲学基本历史


```{graphviz}
digraph philosophy_before_qin {
    node [shape=box]
    newrank=true;
    
    subgraph cluster_ru {
        label="儒家"
        孔子 -> 儒家其他七派
        孔子 -> 子思曾子派
        子思曾子派 -> 孟子
        孟子 -> 荀子
    }

    孔子 -> 管子
    鬼谷子

    subgraph cluster_dao {
        label="道家"
        老子 -> 列子
        列子 -> 庄子

        列子 [style="dashed"]
    }

    subgraph cluster_mo {
        label="墨家"
        墨子 -> 后期墨家学派
    }

    subgraph cluster_debate {
        label="辩家"
        公孙龙子
        惠施
    }

    老子 -> 韩非子
    老子 -> 荀子


    subgraph cluster_fa {
        label="法家"
        韩非子
    }

    subgraph cluster_yinyang {
        label="阴阳家"
        邹衍
    }

    {rank=min 老子 孔子 墨子}
    {rank=same 公孙龙子 惠施 庄子 后期墨家学派 孟子}
    {rank=same 韩非子 荀子 邹衍}
}
```