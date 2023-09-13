---
title: Tree Thinking
module: 1
session: 2
day2022: M/9/12/2022
day2023: M/9/11/2023
---

# Tree thinking and Evidence for evolution
Quantifying and describing biodiversity now and in the past.

---
## Assignments due for this class (9/11/23)
- read **Evolution 5th edition, Chapter 1** (Evolutionary Biology; 26 pages)
- read **Evolution 5th edition, Chapter 2** (Tree of Life; 30 pages)
- complete Courseworks Quiz 1
- complete [interactive exercise 0](https://mybinder.org/v2/gh/eaton-lab/fundamentals/HEAD?labpath=notebooks%2Fnb-0-jupyter.ipynb) (Introduction to Jupyter)
- complete [interactive exercise 1](https://mybinder.org/v2/gh/eaton-lab/fundamentals/HEAD?labpath=notebooks%2Fnb-6-tree-thinking.ipynb) (Python tree reading exercise)


## Assignments due before next class (9/13/23)
<!-- - (NOT REQUIRED) **Evolution 5th edition, Chapter 17** (The History of Life; 26 pages) -->
- **Evolution 5th edition, Chapter 18** (The Evolution of Biological Diversity; 22 pages)
- complete Courseworks Quiz 2
- [Pyron, A. 2017. “Perspective | We Don’t Need to Save Endangered Species. Extinction Is Part of Evolution.” Washington Post, November 22, 2017](https://www.washingtonpost.com/outlook/we-dont-need-to-save-endangered-species-extinction-is-part-of-evolution/2017/11/21/57fc5658-cdb4-11e7-a1a3-0d1e45a6de3d_story.html). A controversial essay arguing
for the constancy of extinction throughout history and the relevance of deep
evolutionary thinking towards our goals in conservation.
- [Safina, C. 2018. "In Defense of Biodiversity: Why Protecting Species from Extinction Matters" YaleEnvironment360](https://e360.yale.edu/features/in-defense-of-biodiversity-why-protecting-species-from-extinction-matters). A
response to the first article, arguing for the immediate importance of
preventing human-mediated species extinction.


--- 

## Class session outline
- Lecture: review of chapter 1 (Definitions, History, Theory, Impact)
- Lecture: review of chapter 2
	- Interpreting phylogenies
	- Review of quiz and exercise/assignment
- **break**
- Lecture: short review of chapter 17 (history of life; not assigned to read)
	- Dates/scale to understand approximate rates of evolution
- Lecture: preview of chapter 18 (biological diversity)

----

## Slides
<a href="placeholder.com" target="_blank"></a>
[:material-presentation-play: *Link to Slides*: **Tree Thinking and Biodiversity**](../lectures/biodiversity/)

----

## Notes/Review

### Evidence for Evolution 

!!! warning "Important"

    **Box 2.3** of your textbook summarizes many of the strongest examples of evidence for Evolution. As described, this box does not even include the abundant and strong evidence from the fossil record, but focuses instead on the ample evidence we can observe from patterns among extant organisms. I would study this.

### Definitions
**Common Ancestry**: Darwin extrapolated from the relationships among 
organisms like finches with similar morphologies, to relationships among 
major orders, to relationships among phyla, all the way to the idea of a 
universal common ancestor. 

**Most recent common ancestor (MRCA)**: All organisms share a most common 
ancestor at some time in their evolutionary history, representing the ancestor
from which they diverged. Closely related species have more recent common 
ancestors than more distant relatives. 

**Universal Common Ancestry**: All life is related by common ancestry, 
i.e., descended from a last universal common ancestor (LUCA).

**Phylogeny**: A tree-like structure representing the evolutionary
relationships of organisms related by common ancestry. A phylogeny should
be read from the tips towards the root. Those sharing more recent common
ancestors are more closely related. The order/rotation/distance between names 
along the tips of a phylogeny is not informative. It is the joining
(coalescing) of ancestors backwards in time into a common ancestor on a
phylogeny that provides information about relatedness.

**Taxonomy**: Linnaen taxonomy is a hierarchical classification system used 
originally to group organisms by morphological similarities. It was developed
before the theory of evolution. It was not originally a quantitative method 
like modern phylogenetic inference, but rather a subjective classification 
system. It was not intended to represent phylogenetic relatedness (since this
idea did not yet exist), however, it often happened to do so pretty well. 
Modern taxonomies still use the Linnaen naming system, but use phylogenetic 
evidence to update how organisms are grouped. This is one reason that many 
names change over time (e.g., named groups are found to not be monophyletic: 
descended from a common ancestor to the exclusion of others not in the group.)

### Common ancestry and homology
Darwin's theory of evolution proposed that organisms descend from shared
common ancestors, and that all organisms descended from a long-past universal
common ancestor. There is now overwhelming evidence to support this. **The** 
key evidence of common ancestry is **homology**, the inheritance of ancestral
features that become modified in descendants.

Homology is abundantly evident in the fossil record as gradual changes
over time among descendant lineages from a common ancestor's phenotype. 
Similarly, homology is evident in the features of extant
organisms in the similarity of structures among organisms
despite differences in function. For example, the same modified ancestral 
bones make up the limbs of divergent organisms like whales, birds, and 
primates despite the fact that they have been greatly modified into very 
different functions like swimming, flying, or grasping. This makes no sense 
at all from a design perspective, but is precisely what we expect in an 
evolutionary process of descent with modification. 
<!-- Vestigial structures representing a non-functional leftover of a prior ... -->

#### Homology in genetics
The genome is a molecular encoding of huge amounts
of information and each site or gene represents a homologous character 
inherited from a common ancestor. Close relatives have had less time for 
mutations (modifications) to occur since diverging from a common ancestor,
while more distant relatives have had more time to accumulate differences.
These differences underlie their many morphological and functional 
differences.

#### Homology of all genetic information
In fact, we can model the origin of 
all parts of the genome as arising from duplication of some previous
ancestral gene segments. We can build phylogenies not only of organisms, 
but also for gene families and even individual copies of genes. We will revisit
this concept in a later unit.
<!-- (e.g., Fig-2.13-2.15) -->

#### Universality of arbitrary codes. 
Universality in the codes of translation 
involved in the central dogma of genetics (DNA->RNA->Proteins), 
such as the genetic code for how mRNA sequence codons are translated into 
amino acids, represent an arbitrary encoding. Why do all organisms share this
same code? It makes no sense except in light of the theory of evolution, 
which predicts that once the code was established it was inherited by all 
descendant organisms, among which, it would be very hard (maladaptive)
to evolve an alternative implementation.

#### The molecular clock
The accumulation of increasing numbers of mutations 
between diverged lineages over time acts like a clock from which we can 
infer the relative and/or absolute time of divergence between organisms. 
This evidence coincides with similar estimates of when different lineages
first appear in the fossil record, providing independent lines of evidence
for the same order and timing of evolution in the history of life on Earth.
<!-- (This is most accurate for divergences on the scales of millions of 
years, not hundreds, due to the law of large numbers, the mean is better 
approximated when there are many more observations / less sampling error). 
 -->

### Convergence and parallelism
Both within the fossil record, and using inferred phylogenetic relationship 
among extant organisms, we can study patterns of trait evolution. Given the
process of common ancestry, we expect organisms to diverge over time from 
each other and from their common ancestral phenotype. But diverge in what ways?
Random evolution among descendant lineages is unlikely to have given rise to 
the diversity of organisms we see today, particularly in terms of their 
apparent fit to their environments. Instead, evidence of Darwin's other
main thesis, natural selection, is abundantly evident in nature through 
patterns of trait evolution.

#### Parallel evolution
A key signature of natural selection is patterns of repeated evolution of 
similar structures among distantly related organisms by convergence or 
parallelism, representing repeated adaptations to similar selection pressures.
Famous examples of **parallel evolution** involve the *repeated evolution* 
of similar ecological traits among geographically isolated species of 
Anolis Lizards on different Carribean islands, or of Viburnum plants in 
disjunct montane cloud forests. Here the same homologous traits evolved
similar character states repeatedly, and in ways that were correlated with
their environment.

#### Convergent evolution
By contrast, many organisms also exhibit **convergent evolution**, where 
similar functions/traits evolve from *non-homologous* origins. Examples 
include the *independent* evolution of a camera-type eye in both vertebrates
and cephalopods. These traits function similarly but are derived from distinctly
different structures and genetic and developmental origins. They represent
two different scenarios where evolution led to an adaptive solution that 
increased in frequency due to its benefit on fitness. 

#### Testing homology
The concept of homology is clear, however, identifying
homology among biological structures can in some cases be quite challenging. 
For example, although the genetic and developmental basis by which eyes 
evolved in cephalopods versus vertebrates are very different, it has 
also been found that they share *some* homologous genetic basis. For example,
genes involved in light capture trace all the way back to single-celled 
archeael ancestors. Thus, *deep homology* at this very ancient level may 
still have influenced their likelihood of evolving these convergent features.
This idea will be revisited in the topic of *evolutionary development* later 
in class.

### Phylogenetic trees
Famously, the only figure in the Origin of Species is a hand-drawn depiction
of a phylogenetic tree next to the words "I think". Darwin used this image
to demonstrate descent from common ancestors. The use of a tree image to
depict evolutionary relationships is now common-place in biology. 
In fact, it has even been argued that "It is impossible to really understand 
evolution without an ability to accurately interpret phylogenetic trees". 
This is true, and important, as there are several common pitfalls that 
even practiced researchers often make when reading phylogenetic trees that
can lead them to mis-intepret their meaning.

Phylogenetic trees represent branching events in the evolutionary history of 
a set of samples. The samples (e.g., populations, species) are represented 
at the tips and their ancestors at interior **nodes** in a tree. Any set of
samples shares a **most recent common ancestor (mrca)** at some point in time.
A group of samples that share a MRCA to the exclusion of all other samples in 
a tree are defined as a clade, or **monophyletic clade**. A tree is composed 
of many clades that are nested within each other. The branches/edges
of a phylogeny typically represent the magnitude of divergence between 
lineages, and can be measured in various units such as time or number of DNA
substitutions. 

#### Reading phylogenetic trees
See also exercise 1 (link at top of page). A number of common mistakes 
made when reading phylogenetic trees are listed below.

- Misinterpreting the tip order as meaningful about evolutionary relationships
as opposed to tracing back from tips to find shared ancestors (trees should be
read in the direction from to tips to root, not along the axis of the tips). 
- Not recognizing the meaning or possible lack of meaning in branch lengths.
Often branch lengths may be artifically lengthened simply to show relationships
more clearly.
- Not recognizing whether a tree is rooted or not. Sometimes we do not know
the rooting of a tree, in which case directionality of evolution is not known.
However, rates and patterns of change along branches of a tree can still be 
measured on unrooted trees.
- Referring to one extant clade or organism as an ancestor of another is 
incorrect. For example, to say that Humans evolved from apes is wrong. 
Rather, Humans are a member of the extant clade of apes. In terms of a 
specific ape lineage, like a Chimpanzee, humans diverged from a common ancestor 
with chimps at some time in the past (i.e., not from chimps directly), and
both lienages have evolved for equal amounts of time since.
- Referring to an extant clade as "basal" or "ancient" based on its level 
of diversity or appearance. Your textbook makes this mistake, referring to 
Ginkgo as both a basal and ancient lineage. While it is true that the lineage
that includes extant ginkgos diverged from the clade that includes extant 
angiosperms long ago, both lineages have diverged from their common ancestor
for the same amount of time. The fact that one has diversified into a greater
number of extant species currently than the other has nothing to do with
whether one of the other is "ancient". It is accurate, however, to
describe that the MRCA of extant and extinct ginkgos (as known from
the fossil record) is older than the most recent common ancestor of
all angiosperms.

<!-- The observation of ginkgo-like fossils 
much longer ago than many plant lineages that did not evolve until much later
also does not indicate  -->

#### Phylogenetic Inference
The field of phylogenetics concerns the inference of phylogenetic relationships
(trees) from data. In most cases we cannot directly observe extinct ancestors and 
so we instead apply statistical approaches to infer a phylogenetic tree
that is most consistent with the data we can observe: differences among extant
samples. Phylogenetic methods examine homologous characters to fit models of
transitions in character states. For example, each site of a DNA sequence is
a character with possible states A, C, T or G. Although DNA is overwhelmingly
the most common type of data analyzed in modern phylogenetics, trees can also
be inferred from morphological characters. We will revisit phylogenetic 
methods in a later lecture.

One goal of phylogenetics is to infer the tree-of-life -- a phylogeny for all
extant species. However, this is not the only goal of phylogenetics, instead
there are countless subfields concerned with topics such as naming lineages
on trees (taxonomy); advancing statistical models of DNA subsitutions (molecular
phylogenetics); improving computational efficiency of tree inference algorithms
(computational phylogenetics); refining divergence time estimates using fossil 
calibrations (paleo or relaxed clock phylogenetics); investigating 
non-bifurcating patterns arising from hybridization (phylogenetic network
inference); investigating the consequences of gene duplication and 
loss (comparative and functional genomics); and many many more topics 
concerning phylogenetic trees.

#### Using Phylogenies to study evolution
We previously introduced patterns of parallelism and convergence in trait
evolution as evidence of adaptations in nature. To identify such patterns
necessarily requires a phylogenetic hypotheses on which to examine the 
direction, order, and timing of trait evolution. Phylogenies are commonly
used as a model on which to study patterns of evolution. 

We will learn later about models of how quantitative traits evolve along 
the edges of phylogenies that are used to test hypotheses about the role
of selection versus genetic drift in the evolution of traits such as body
size. We will also learn about models of discrete traits, such as transitions
in sexual systems, and how these are used to test hypotheses about rates and
patterns of evolution such as the reversibility of evolution (Dollo's law). 
We will also learn more later about methods for studying the distribution 
of branch lengths on phylogenies to infer rates of speciation and extinction
to test hypotheses about the history of diversification of lineages. Finally,
many of these models can be applied in combination to test complex evolutionary
hypotheses, such as whether certain patterns of trait evolution affect rates
of diversification. All of these methods rely on phylogenetic trees as their
basis.

<!-- ********************************************************************* -->


---
## Additional resources referenced in lecture (not required reading)

- [Baum DA and S Offner "Phylogenics & Tree-Thinking," The American Biology Teacher, 70(4), 222-229](https://bioone.org/journals/The-American-Biology-Teacher/volume-70/issue-4/0002-7685(2008)70[222:PT]2.0.CO;2/Phylogenics-amp-Tree-Thinking/10.1662/0002-7685(2008)70[222:PT]2.0.CO;2.full)
A didactic article about how to read and interpret evolutionary trees representing
evolutionary relationships across a range of scales, from genes, to individuals,
to populations/species. 
<!-- - **Evolution 5th edition, Chapter 17.** The geographic distribution of 
present day diversity on Earth. Species richness and diversity is 
distributed across different latitudes, biomes, and communities of 
interacting species. The latitudinal diversity gradient is the most 
conspicuous macro-ecological pattern. What causes this pattern?   -->

<!-- - Rosenberg "Decline of Avifauna"  
- Pyron: "Extinction"  
- Safina: "Extinction" 
 -->