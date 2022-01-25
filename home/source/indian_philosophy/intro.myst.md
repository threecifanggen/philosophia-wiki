---
html_meta:
    "description": "印度哲学"
    "author": "黄宝臣, 3gee, threecifanggen"
    "keywords": "印度哲学, 3gee, threecifanggen, 哲学百科, 黄宝臣, 哲学史, 宗教, 宗教史, 科学哲学, 科学史"
    "property=og:locale": "zh_CN"
---
# 印度宗教及哲学


## 基本历史

```{uml}
state "吠陀时代" as vedas {
    state "早期吠陀" as early_vedas
    state "奥义书" as upanisads
    state "摩诃婆罗多" as mahabharata
    state "婆罗门教" as brahmanism
    early_vedas -down-> upanisads
    upanisads -down-> brahmanism
    early_vedas -down-> brahmanism
}


state "轴心时代" as hero_era {
    state "释迦摩尼" as buddha
    state "耆那教" as jaina
    jaina -down--> buddha
}

state "经典时代(Age of the Sutra)" as sutra {
    state "印度教体系" as indian {
        state "数论派(Samkhya)" as samkhya
        state "瑜伽行派(Yoga)" as yoga
        state "正理派(Nyaya)" as nyaya
        state "胜论派(Vaisesika)" as vaisesika
        state "弥曼差派(Mimamsa)" as mimamsa
        state "吠檀多派(Vedanta)" as vedanta
    }
    
    state "佛教体系" as buddhism {
        state "中观宗(Madhyamaka)" as madhyamaka
        state "说一切有部(Sarvastivada)" as sarvastivada
        state "上座部(Theravada)" as theravada
        state "唯识宗(Yogacara)" as yogacara
        state "因明学" as yinming

        theravada -down-> sarvastivada
        sarvastivada -down-> yogacara
        yogacara -down-> yinming
    }
    
    state "耆那教体系" as jainism {
        state "天衣派(Digambara)" as digambara
        state "白衣派(Svetambara)" as svetambara
    }

    yoga -down--> yogacara
    
}

upanisads -down--> jaina

brahmanism -down--> buddha
brahmanism -down---> samkhya
brahmanism -down---> yoga
brahmanism -down---> nyaya
brahmanism -down---> vaisesika
brahmanism -down---> mimamsa
brahmanism -down----> vedanta

samkhya -down-> yoga
jaina -down--> yoga
buddha -down--> yoga

nyaya -down-> vaisesika
mimamsa -down-> vedanta

buddha -down--> theravada

jaina -down--> digambara
jaina -down--> svetambara
```

```{toctree}
---
maxdepth: 1
---

buddhism/intro
vedanta/intro
```