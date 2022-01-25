---
html_meta:
    "description": "近代哲学"
    "author": "黄宝臣, 3gee, threecifanggen"
    "keywords": "近代哲学, 3gee, threecifanggen, 哲学百科, 黄宝臣, 哲学史, 宗教, 宗教史, 科学哲学, 科学史"
    "property=og:locale": "zh_CN"
---
# 近代哲学

## 基本历史

```{uml}
state "文艺复兴哲学" as renaissance {
    state "培根" as bacon
    state "马基雅维利" as machiavelli 
    state "霍布斯" as hobbes
    bacon -down-> hobbes
    machiavelli -down-> hobbes
    machiavelli -down-> bacon
}

state "理性主义" as rationism {
    state "蒙田" as montaigne
    state "笛卡尔" as descartes
    state "斯宾诺莎" as spinoza
    state "莱布尼茨" as leibniz
    state "帕斯卡尔" as pascal
    state "沃尔夫" as wolff

    montaigne -down-> descartes
    montaigne -down-> pascal
    montaigne -down-> spinoza
    descartes -down-> spinoza
    spinoza -down-> leibniz
    descartes -down-> leibniz
    descartes -down-> pascal
    leibniz -down-> wolff

}

state "法国政治哲学/百科全书派" as french {
    state "卢梭" as rousseau
    state "伏尔泰" as voltaire
    state "百科全书派" as baike

    rousseau -right-> baike
    baike -left-> rousseau
}

state "经验主义" as empiricism {
    
    state "洛克" as locke
    state "休谟" as hume
    
    locke -down-> hume
}

state "德国唯心主义" as idealism {
    state "康德" as kant
    state "费希特" as fichte
    state "谢林" as schelling
    state "黑格尔" as hegel
    
    kant -down--> hegel
    kant -down-> fichte
    fichte -down-> hegel
    fichte -down-> schelling
    schelling -down-> hegel
}

montaigne -down-> bacon
bacon -down--> locke
rousseau -down--> kant
leibniz -down--> kant
hume -down--> kant
rousseau -down--> kant
hobbes -down--> rousseau
locke -down-> voltaire
pascal -down-> rousseau
leibniz -down-> rousseau
machiavelli -down--> rousseau
machiavelli -down--> hume
machiavelli -down--> spinoza
machiavelli -down--> baike
```
