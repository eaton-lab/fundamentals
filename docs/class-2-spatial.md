---
title: Spatial genetics
module: 2
session: 11
day2023: M/10/16/2023
---


# Spatial genetics

----

## Assignments due for this class (M: 10/16/2023)
- Walsh, Jennifer, Shawn M Billerman, Vanya G Rohwer, Bronwyn G Butcher, and Irby J Lovette. 2020. “Genomic and Plumage Variation across the Controversial Baltimore and Bullock’s Oriole Hybrid Zone.” The Auk 137 (4): ukaa044. https://doi.org/10.1093/auk/ukaa044.
- **Evolution 5th edition, Chapter 8** (Geographic diversity)


## Assignments due for next class (W: 10/18/2023)
- **Evolution 5th edition, Chapter 9** (speciation)
- Courseworks quiz

----


## Outline

- Fst and population divergence
- *break*
- Discussion of article

----

## Slides

- [:material-presentation-play: *Link to Lecture Slideshow*: **Adaptation**](../lectures/Fst-lecture.pdf)

## Lecture Notes

### Terminology
- Population, deme, subgroup
Many terms can be used to describe the grouping of individuals into discrete
groups. Populations are often delimited by geographic location. 

- Gene flow, migration, admixture, introgression
All of these terms refer to the exchange of alleles between populations. 

- Panmictic
Refers to a randomly mating population. We almost always apply the assumption
that individuals *within* a population are randomly mating.


### Fst (fixation index)
Fst is a measure of population structure. It measures how genetic variation is
partitioned into subgroups relative to treating all samples as a single group.

- Fst == 0; no population structure.
- 0 > Fst < 1; some population structure (non-random mating)
- Fst ~ 1; very highly diverged populations.


### Isolation by distance (IBD)
- How can we tell whether spatial variation is a result of genetic drift versus
selection?

Fst variation can arise from *neutral evolution* over space with limited 
dispersal. Appears as a positive correlation between geographic distance 
and Fst.

Because environmental variables also vary across space, IBD can cause patterns
that make it *appear* as if a correlation exists between an environmental
variable and genetic divergence. Thus, IBD is often a null hypothesis that must
first be refuted before you can detect an association with environment.

### Gene flow
- Gene flow between populations can limit the genome-wide divergence (Fst).
- Gene flow can result in maladaptation if new alleles that are not locally
beneficial are continually introduced to a population.


### Selection
- Gene flow affects genome divergence (Fst) fairly equally across the entire 
genome. By contrast, selection acts locally on a variation at a specific locus.
- Selection reduces diversity within populations, and thus increases Fst between populations.
- Thus, local Fst patterns that show a strong deviation from the genome-wide Fst
can provide evidence of selection.
- Example: Heliconius butterfly paper shows strong deviations in Fst at selected
loci relative to a genome-wide Fst between populations that is relatively high, since
these population exchange a lot of gene flow.


### Clines
Evidence of adaptation can also be found in clinal patterns of variation. Given
a narrow hybrid zone between two populations with different phenotypic means, 
examine variation in genotypes to find alleles that follow the same cline. 


### Range expansion and dispersal
- Why do individuals dispserse? Competition, Habitat volatility, finding mates.


### Applied Methods

- Genetic Principal Components Analysis (PCA): Dimensionality reduction analysis
to visualize population structure. Given many SNPs measured among many 
individuals, it is likely that of these SNPs will be correlated due to population
structure. Find the 2 (or more) axes that explain the greatest proportion of 
variation in allele sharing among samples. Visualize as 2 or 3d plots.

- Genetic STRUCTURE analysis: Clustering analysis to assign ancestry of individuals
to k discrete groups. User must define the value of k ahead of time. Results are
usually shown for several values of k, and tests can be performed to identify the
best fitting k. Results are shown as barplots with colors showing proportion of
ancestry of each sample assigned to a different population group.

