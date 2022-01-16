# 希腊哲学

## 主要历史传承

```{graphviz}
digraph GreekPhilosophy {
    newrank=true;
    node [shape=box];

    clusterrank="global"
    subgraph cluster_presocrates {
        label="前苏格拉底哲学"

        subgraph cluster_nature {
            label="自然哲学"

            米利都学派 -> 赫拉克利特
            米利都学派 -> 埃利亚学派
            毕达哥拉斯派
            原子派
            埃利亚学派 -> 多元论派
        }
        智者派
    }

    智者派 -> 苏格拉底
    苏格拉底 -> 柏拉图
    毕达哥拉斯派 -> 柏拉图
    柏拉图 -> 亚里士多德
    原子派 -> 希腊化时期原子派
    智者派 -> 希腊化时期智者派
    苏格拉底 -> 犬儒主义
    赫拉克利特 -> 斯多亚主义
    柏拉图 -> 斯多亚主义
    柏拉图 -> 柏拉图主义
    亚里士多德 -> 逍遥派
    多元论派 -> 斯多亚主义
    原子派 -> 皮浪主义

    subgraph cluster_post {
        label="希腊化时代哲学"
        
        皮浪主义 -> 希腊化时期原子派
        希腊化时期智者派
        逍遥派
        犬儒主义
        享乐主义  -> 伊壁鸠鲁主义
        希腊化时期原子派 -> 伊壁鸠鲁主义
        皮浪主义 -> 柏拉图怀疑主义
        柏拉图主义 -> 柏拉图怀疑主义
        柏拉图怀疑主义 -> 新柏拉图主义
        斯多亚主义
    }

    {rank=same 新柏拉图主义 伊壁鸠鲁主义 犬儒主义 斯多亚主义 逍遥派}    
    {rank=same 埃利亚学派 赫拉克利特 毕达哥拉斯派}
    {rank=same 原子派 多元论派 智者派}
    {rank=same 柏拉图}
    {rank=same 亚里士多德}
    {rank=same 柏拉图主义 享乐主义 皮浪主义 希腊化时期原子派 希腊化时期智者派}
}
```

## 前苏格拉底

## 苏格拉底 - 柏拉图 - 亚里士多德

```{toctree}
---
maxdepth: 1
---

plato
```