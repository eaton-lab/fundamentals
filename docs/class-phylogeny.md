---
title: Phylogeny
module: 2
session: 10
day2022: W/10/5/2022
day2023: M/10/9/2023
---


# Phylogeny

----

## Assignments due for this class (M: 10/9/2023)
- **Evolution 5th edition, Chapter 16 ** (phylogeny)
- GCBias: https://gcbias.org/2017/12/19/1628/
- GCBias: https://gcbias.org/2013/11/11/how-does-your-number-of-genetic-ancestors-grow-back-over-time/
- Complete Courseworks Quiz
- complete [interactive exercises 0, 1, 2, **3, 4, 5**, and 6](https://pinky.eaton-lab.org) (gene trees and species trees)


## Assignments due for next class (W: 10/11/2023)
- Degnan, James H., and Noah A. Rosenberg. 2009. “Gene Tree Discordance, Phylogenetic Inference and the Multispecies Coalescent.” Trends in Ecology & Evolution 24 (6): 332–40. https://doi.org/10.1016/j.tree.2009.01.009.
- Heliconius Genome Consortium, Kanchon K. Dasmahapatra, James R. Walters, Adriana D. Briscoe, John W. Davey, Annabel Whibley, Nicola J. Nadeau, et al. 2012. “Butterfly Genome Reveals Promiscuous Exchange of Mimicry Adaptations among Species.” Nature 487 (7405): 94. https://doi.org/10.1038/nature11041.
- Courseworks quiz
<!-- - Notebook exercise: tree sequences -->
<!-- - Notebook exercise: ABBA-BABA -->
<!-- - Notebook exercise: Fst -->

----

## Outline
- Review detecting selection and neutral vs non-neutral genomes
- Review chapter 16 quiz
- Review ancestry  <!-- more on GCBias stuff -->
- *Break*
- Review notebooks
- Lecture: Introduce population structure
<!-- - Lecture: Fst and ABBA-BABA -->
<!-- - Review notebooks -->
<!-- - Discuss articles -->

----

Slides: 
- Continuation of slides from last class: Ancestry

----

## Lecture notes

### Genealogies and sequence variation
- when mutations occur in germline cells they are passed on to descendants.
- a sample of gene copies in a population will only exhibit genetic variation
if mutations occurred since their common ancestor.
- variation in DNA sequences is linked to genealogies.

### Genealogical variation
- Different unlinked regions of the genome trace back different genealogical
histories.
- Linked regions of the genome trace back more similar genealogical histories
(i.e., they share more ancestors in common). This similarity is the cause of linkage disequilibrium. 

### The top of a population model
- We learned that the expected waiting time until all samples in a population
coalesce is approximately 4N. 
- However, coalescent models have another relevant parameter, Tau, which
the length of the model interval.
- If the interval is less than 4N generations in length, then it is expected
that many samples will not have yet coalesced by the time they reach the 
top of the population interval. At this point, we must also model what 
happens in the ancestral population, which may have a different Ne, or may
contain addition gene copies.
- See Notebook 5 on demographic models and species trees.


### Incomplete Lineage Sorting (ILS)


### Why different genomic regions have different genealogical trees


### Introgression


### Phylogenetic Inference

Evolutionary relationships are evident in patterns of **homology** -- characters that are shared among taxa and which were inherited from a common ancestor. 

It is important within an evolutionary context to consider whether a shared trait is derived in the group that shares it, versus whether it is ancestral: 
synapomorphy versus plesiomorphy. Only synapomorphies can be used as phylogenetically informative characters.

### Phylogenetic inference methods
Phylogenetic inference generally involves 3 steps:
1. Propose a phylogenetic hypothesis
2. Calculate a score (e.g., likelihood or parsimony score) of the phylogenetic
model given the data.
3. Propose a change to the tree topology and repeat from step 2.

This procedure can be repeated over many iterations to search the space of 
possible trees to try to find the best one. This is a **heuristic approach**, 
meaning that it uses algorithmic shortcuts to try to find the best tree, instead
of trying to calculate the score of every possible tree, since the number of
possible phylogenetic trees is way way way too big.


### Homoplasy
The repeated evolution of a character state. Homoplasy can occur when the rate of evolution of a character is high, or if there are few character states that it can transition between. In either case, if too many transitions occur back and forth between states, it is difficult to infer ancestral states and to accurately 
count the number of changes that have occurred.


### Methods for inferring phylogenies
Distance, Parsimony, Maximum Likelihood, Bayesian


### Using phylogenies

- Inferring divergence times (dates)
- Measuring rates of evolution
- Phylo Gene Association Tests
- Reconstructing Ancestral States
- Phylogenetic Comparative Methods

