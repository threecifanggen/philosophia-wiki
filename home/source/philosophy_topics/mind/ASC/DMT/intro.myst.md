# DMT

## DMT的化学合成

```{figure} assets/img/2022-01-21-15-52-18.png
---
name: DMT合成
---

DMT合成

Biosynthesis: Tryptophan (2) is converted to tryptamine (TA, 3) by aromatic amino acid decarboxylase (AADC). TA is dimethylated to first yield N-methyltryptamine (NMT, 4) and then DMT (1) by indole-N-methyltransferase (INMT), using S-adenosyl-methionine (SAM) as the methyl source. Metabolism: TA, NMT and DMT are all substrates for monoamine oxidase, yielding indole-3-acetic acid (5, IAA) as both a common precursor metabolite and the most abundant metabolite of DMT itself. DMT is also converted to DMT-N-oxide (6) as the second-most abundant metabolite. Two 1,2,3,4-tetrahydro-beta-carbolines (THBCs) have also been identified as metabolites; 2-methyl-THBC (7, MTHBC) and THBC (8)[^1].
```

```{uml}
state Tryptophan as "色氨酸"
state TA as "色胺(TA)"
state NMT
state DMT


state metabolite as "生化反应" {
    state IAA as "吲哚乙酸(生长激素, IAA)"
    state DMTNO as "二甲基色胺-N-氧化物"
    state THBCs
}

Tryptophan -down-> TA : AADC
TA -down-> NMT : INMT SAM
NMT -down-> DMT : INMT SA

TA -right--> IAA : MAO
NMT -right--> IAA : MAO
DMT -right--> IAA : MAO

DMT -right--> DMTNO : N-oxidation

TA -right--> THBCs
NMT -right--> THBCs
DMT -right--> THBCs 
```

### DMT与褪黑色素的关系

```{figure} assets/img/2022-01-21-16-20-12.png
---
name: DMT与褪黑色素的关系
---

DMT与褪黑色素的关系[^2]
```

## 详细目录

```{toctree}
---
maxdepth: 1
---

religion
```


[^1]: Barker, Steven A. "N, N-Dimethyltryptamine (DMT), an Endogenous Hallucinogen: Past, Present, and Future Research to Determine Its Role and Function." *Frontiers in neuroscience* 12 (2018): 536.
[^2]: Gomes, Melissa M, Janine B Coimbra, Renan O Clara, Felipe A Dörr, Ana Carolina R Moreno, Jair R Chagas, Sérgio Tufik, et al. "Biosynthesis of N, N-Dimethyltryptamine (Dmt) in a Melanoma Cell Line and Its Metabolization by Peroxidases." *Biochemical pharmacology* 88, no. 3 (2014): 393-401.
