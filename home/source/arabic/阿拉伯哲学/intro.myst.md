---
html_meta:
    "description": "阿拉伯哲学概述"
    "author": "黄宝臣, 3gee, threecifanggen"
    "keywords": "intro.myst.md, 3gee, threecifanggen, 哲学百科, 黄宝臣, 哲学史, 宗教, 宗教史, 科学哲学, 科学史"
    "property=og:locale": "zh_CN"
---
# 阿拉伯哲学

## 基本历史

```{uml}


state "译经时代" as translate_era {
    state "亚里士多德传统" as aristotle
    state "新柏拉图主义传统" as neoplatonic
    state "希腊医学传统" as greek_medicine
}

state "经典时代" as classic_era {
    state "Kalam" as kalam
    state "al-Farabi" as farabi
    state "al-Kindi" as kindi
    kalam -down-> ghazali
    state "al-Ghazali" as ghazali
    state Avicenna
    farabi -down-> Avicenna
    ghazali -down-> Avicenna
    kindi -down-> Avicenna
}

state "后阿维森纳传统" as post_avicennian {
    state "Ibn Tufayl" as tufayl
    state "神秘主义/光明主义" as sophist
    state "晚期光明主义" as post_illum
    sophist -down-> post_illum
}

aristotle -down--> farabi

neoplatonic -down--> farabi
neoplatonic -down--> kindi

neoplatonic -down----> sophist

Avicenna -down--> tufayl


```