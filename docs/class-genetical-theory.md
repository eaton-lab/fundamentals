---
title: Genetical Theory
module: 1
session: 5
day2022: M/9/19/2022
day2023: M/9/20/2023
---


<!-- NOTES FOR FUTURE SELF:
	- How do students deal with chapter 5 without knowledge of genetics?
	- Types of selection and Quantgen is now in Chapter 7...
	- Does the textbook adequately introduce fitness landscapes?
	- Does the textbook overlap too much with Orr Fitness article?
	- Which Hereford or Kingsolver?
	- Should assign Pangloss.
-->


# Genetical Theory of Natural Selection

Review genetical theory of natural selection. Discuss fitness landscapes, 
optima, measuring selection, and defining fitness. 
<!-- Introduce quant gen from chapter 6, but we will not assign it as reading. -->

## Assignments due for this class (9/20/23)
- **Evolution 5th edition, Chapter 5** (The Genetical Theory of Natural Selection; 30 pages)
This chapter introduces statistical methods for measuring changes in allele
frequencies over generations, and measuring natural selection.
- complete Courseworks Quiz 4

## Assignments due before next class (9/25/23)
- [Hendry, Andrew P., and Andrew Gonzalez. 2008. “Whither Adaptation?” Biology 
& Philosophy 23 (5): 673](https://doi.org/10.1007/s10539-008-9126-x).  
*A debate among two embattled perspectives on whether
our observations from nature and experiments support the idea that most organisms
are well adapted to their environment, or that they are not well adapted 
(maladapted).*
- [Bonnet, Timothée, Michael B. Morrissey, Pierre de Villemereuil, Susan C. Alberts, Peter Arcese, Liam D. Bailey, Stan Boutin, et al. 2022. “Genetic Variance in Fitness Indicates Rapid Contemporary Adaptive Evolution in Wild Animals.” Science 376 (6596): 1012–16.](https://doi.org/10.1126/science.abk0853).  
*A study measures variance in relative fitness within many populations showing that many populations
have a great potential for adaptation*
<!-- 
- [Hereford, Joe. 2009. “A Quantitative Survey of Local Adaptation and Fitness
Trade‐Offs.” The American Naturalist 173 (5): 579–88.](https://doi.org/10.1086/597611).  
*A meta-study that compiles results from many individual studies that measured the strength of 
selection coefficients in natural populations.*
-->

<!-- - [Schluter, Dolph. 1996. “Adaptive Radiation Along Genetic Lines of 
Least Resistance.” Evolution 50 (5): 1766–74](https://doi.org/10.1111/j.1558-5646.1996.tb03563.x).
*An empirical study that predicts the response to selection based on variation 
in multiple phenotypic traits in a population.*
- [Orr, H. Allen. 2009. “Fitness and Its Role in Evolutionary Genetics.” Nature Reviews. Genetics 10 (8): 531–39](https://doi.org/10.1038/nrg2603). *This article reviews the many challenges associated with measuring fitness, and the complex ways in which we can conceptualize this relatively simple yet unbounded metric.*
- [Kingsolver, J. G., H. E. Hoekstra, J. M. Hoekstra, D. Berrigan, S. N. Vignieri, C. E. Hill, A. Hoang, P. Gibert, and P. Beerli. 2001. “The Strength of Phenotypic Selection in Natural Populations.” The American Naturalist 157 (3): 245–61](https://doi.org/10.1086/319193). *Another similar study to above.*
- Bonnet "Variance in Fitness". *A study of variation in fitness...*
- Pangloss...
 -->
----

## Outline

- Review chapter 3 natural selection.
- Review ch. 5 part I
	- absolute and relative fitness
	- selection coefficients
	- dominance effects
- *Break*
- Review ch. 5 part II
	- linkage disequilibrium and hitchhiking
	- selective sweep and denovo vs standing variation
	- selection that preserves diversity
	- population mean fitness and adaptive landscapes
	- mutation-selection balance and genetic load
<!-- - Discussion: Orr (2009). “Fitness and Its Role in Evolutionary Genetics.”  -->

---
## Class session outline
- [:material-presentation-play: *Link to Lecture Slideshow*: 
**Genetical Theory of Natural Selection**](../lectures/genetical-theory/)

----

## Lecture notes
Introduction to the genetical theory of natural selection.
Natural selection is manifest by the differential survival and reproduction
of some units over others based on variation in their heritable phenotypes. 
This differential *success* can be measured, and is termed *fitness*. 
In most cases, evolutionary biologists are interested in *relative fitness*
but in some cases we may also examine *absolute fitness*. Each can be 
measured in numerous different ways, and at different scales. We 
start with models for changes in the frequencies of alleles
in a population in response to selection.


### Genetics
In this section we introduce genetic analysis, but only in a relatively 
simple form. You do not yet need to know molecular biology, or 
bioinformatics, or coalescent theory, or genomics. Instead, we are still 
working within the realm of "beanbag genetics", where we concern ourselves
mainly with theoretical models of one or a few genes at a time, each usually
with at most two alleles (variants) present within a single population.

Our simple models throughout this section will assume that individuals are 
diploid, meaning they have two copies of each gene. The copies in a population
can all be the same, in which case there is no genetic variation. If a 
mutation introduces a new allele (variant) into the population and it spreads,
then any individual might have two copies of the original allele, one copy
of the original and one of the new, or two new alleles. These possible 
combinations are called **genotypes**. Thus we can say that there are two
alleles and three genotypes in this population.


### Absolute fitness
The concept of fitness is fundamental to evolutionary biology.

An individual's absolute fitness is the number of offspring that it produces
over its lifetime. It is often represented by the symbol `W`. While this
value is of interest, it is only relevant for *predicting evolution* when 
it is compared to the fitness of other units; i.e., it is the *relative 
differences* in fitness among different units (alleles, individuals, etc) 
that matter. Relative fitness is represented by the lower case symbol `w`.

This is measured by defining a reference against which you will compare 
other units. For example, it is common practice to set the fitness of the 
most common allele (sometimes called the wild-type allele) to 1.0, and to 
measure the fitness of other alleles relative to this (>1 indicates higher
fitness, <1 indicates lower fitness).


### Positive selection
When one allele has higher fitness than another natural selection will 
favor its spread through a population (increase in frequency). It is not
guaranteed to increase though, because chance effects (genetic drift) 
still plays a role in evolution.

We can study the *rate* of evolution in a simple model of a single gene as
the rate of change in allele frequencies. This rate is determined by the 
relative fitness advantage of one allele relative to another, which is
called the **selection coefficient** (s). This determines the strength of
selection. Therefore, we can say that the strength of selection is determined
by differences in relative fitness.

A selection coefficient is not a fixed property of an allele. It can change
over time either because the environment changed, or because the fitness
of other alleles changed for some reason, or because it interacts with other
alleles (epistasis).

A selection coefficient is the difference in relative fitness of one allele 
($A_1$) versus another ($A_2$). If $A_1$ has a 20% higher fitness
than $A_2$ then s=0.2; if $A_1$ has 0.1% higher fitness then s=0.001. 
Note, this is a measure of the effect of an individual allele ($A_1$ versus
$A_2$) not of genotypes ($A_1A_1$, $A_1A_2$, or $A_2A_2$). 
In practice, however, we usually measure the fitness of genotypes (because
the organisms are diploid) and then try to infer the selection coefficient
based on the relative fitness of genotypes. 


### Change in allele frequency
(Note: You do not need to memorize the math involved with calculating changes
in allele frequencies. But, you should be familiar enough with the terms 
involved to be able to look at the equations and verbally describe their 
meaning.)

In a simple model with only two alleles, $A_1$ and $A_2$, we can focus on 
the frequencies of these two alleles rather than worrying about their total
numbers, since the latter depends on the population size. These frequencies
will usually be denoted $p$ and $q$. Because there are only two alleles, and 
their two frequencies must sum to 1, we know that $p = (1 - q)$. 
Therefore, if we know $p$ we know $q$. This is why many equations for a 
two-allele model will focus only on $p$.

To find the change in frequency of $p$ from one generation to the next 
($\Delta p$) we multiply each genotype frequency times its relative fitness. 
(How to calculate expected genotype frequencies in a population is related 
to Hardy-Weinberg equilibrium, a topic we cover later.) Then for each genotype
we divide this value by the population mean fitness, defined below. 

This leads to the simple approximation below. The change in $p$ is the 
product of s (selection coefficient) and $p(1-p)$ (genetic variation): 
$\Delta p = sp(1-p)$

The frequency of an allele one generation in time forward ($p'$) is thus
simple $p' = p + \Delta p$. By repeating this process over many subsequent
generations we can calculate trajectories for the rate of fixation of an
allele under positive selection (e.g., Fig. 5.6). 

!!! tip "Key conclusion"

    The rate of evolution is proportional to the strength of selection and 
    the amount of genetic variation.


### Genetic Variation
See Figure 5.7. Genetic variation at a single locus with two alleles can
be measured as $p(1-p)$. Recall that $(1-p)$ is the frequency of the 
alternative allele ($q$). If either $p$ or $q$ is zero, then the genetic 
variation is zero (one allele has become fixed). Genetic variation is maximized
when both alleles are present at a frequency of 0.5. 


### Population mean fitness
The population mean fitness is involved in the calculation of rate of
evolution. It is the sum of the genotype frequency times the relative fitness
for each of the genotypes in a population:

$\bar w$ = $(1 - p)^2 + 2p(1-p)(1-s) + p^2 (1 + 2s)$

This simplifies into a much simpler term that is easier to describe:

$\bar w = 1 + 2sp$

In other words, the population mean fitness ($\bar w$) is measured 
starting from 1 (the relative fitness we are comparing against) and
adds two times the selection coefficient times the frequency of the 
$p$ allele. If this allele is more common it will have a greater
effect on the *magnitude* of deviation of the mean fitness away from 1, and 
if the selection coefficient is greater it will also have a greater effect
on the *magnitude* of deviation of the mean fitness away from 1, and finally, 
whether the selection coefficient is positive or negative will determine 
the *direction* of deviation of the mean fitness away 1.

### Terminology
An allele with a higher relative fitness relative to a reference allele
has a positive selection coefficient and experiences positive selection. 
It may be called a "beneficial allele", in contrast to a "neutral allele"
(s=0) or a "deleterious allele" (s<0).
More casually we could also say that "selection favors this allele". 

### Rate of evolution
Fig. 5.6 and 5.8: The rate of evolution is faster when $s$ is greater. If
we simulate the trajectory of an allele towards fixation at a frequency of
either 1 or 0, we expect to see an S-shaped curve. This is because the
rate of change of an allele frequency ($\Delta p$) per generation is 
greatest when genetic diversity is greatest and slowest when genetic diversity
is lowest (close to 1 or close to 0).

### Dominance
We will revisit this in our genetics lecture.

Dominance describes an allele's effect on the phenotype (and therefore usually
also the relative fitness) of a diploid heterozygote genotype (i.e., in combination 
with an alternative allele). The three most common scenarios are 
(1) no dominance; (2) dominant; or (3) recessive. 
When there is no dominance then the fitness is typically intermediate such 
as the mean relative fitness of the two alleles. When an allele is dominant 
its overrides the alternative allele in heterozygotes. When an allele is 
recessive the other allele overrides its effect on phenotype.

It is important to note dominance here because of its effect on the rate of
evolution. If an allele is dominant it will change in frequency in response
to selection much more rapidly than if it is recessive. This is because when
an allele first arises by mutation it is very rare, and will thus mostly 
exist within heterozygotes. If heterozygotes express the same phenotype as
a homozygote for this new allele, then selection can act on it. If it is
intermediate, then selection will act only half as strong it. If it recessive
then selection will not act on it, because it has no effect on heterozygote
phenotypes, only on homozgyous ones. (See Fig. 5.9).

<!-- If the mean absolute fitness of individuals in a population increases, 
then we also say that the population's absolute fitness has increased. This
can lead to changes in population density, geographic range, or growth rate
in ways that may reduce the probability of population extinction due to 
random fluctuations or environmental change.

The rate of evolution of the mean absolute fitness of a population 
(i.e., the change in fitness in response to selection) provides a 
meaningful approach of measuring the rate of adaptation. 
 -->


### Fisher's fundamental theorem of natural selection
In Fisher's most famous work on evolution, *The genetical Theory of 
Natural Selection* (1930), he described a model for the rate of 
adaptive evolution that has since come to be called Fisher's fundamental
theorem.

Fisher showed mathematically that, by definition, natural selection causes
the population mean fitness ($\bar w$) to increase over time. This 
means that each generation, to the extent there is variance in relative 
fitness, and selection remains constant, natural selection will lead to a 
reduction in the variance in fitness, which also shifts the mean fitness 
higher. Because variance can never be negative, natural selection causes 
populations to evolve in a way that makes them better adapted (to have higher
fitness).

*The rate of increase in fitness of any organism at any time is equal
to its genetic variance in fitness at that time*. 

*Additive genetic variance* is the proportion of variance in phenotype
that can be explained by genetic variation, and not by the environment.
This can be measured using experiments that control the environment, such
as a common garden.

This shows that the change in mean *relative fitness* due to selection 
equals the additive genetic variance in relative fitness in a population
($\sigma^2_A$), making the additive genetic variance in relative fitness 
arguably the most important evolutionary parameter for a population.

$$ w = \sigma^{2}_{A}(s) $$


### Adaptive/Fitness landscape
Sewall Wright came to a similar conclusion as Fisher using different math
and analogy. He described a fitness landscapes (or adaptive landscapes)
to visualize the relationship between genotypes and fitness. 


This can be a bivariate, or high-dimensional landscape. In the simplest case
fitness is the y-axis or "height" of the landscape and genotypes are x-axis
or base of the landscape (See Fig. 5.23).

In a higher dimensional case, genotypes can represent multiple axes, where
those that are more similar are closer together, and those that more different,
requiring more mutations to reach each other, are further. 
The set of all possible genotypes, their degree of similarity, and their
related fitness values together form a landscape. Natural selection is 
expected to move the population mean fitness "up hill".

An adaptive landscape can show both local and global optima, 
represented as *peaks* on the landscape, surrounded by *valleys*
with lower fitness. Movement between fitness peaks on a landscape
is a major topic of interest in evolution. Do populations get
stuck on suboptimal peaks? How easy is it to move between peaks
of similar fitness? How does the depth of valleys influence the
probabilities of shifts?


### Selective sweep

**Linkage disequilibrium** (LD) describes a statistical association (correlation)
between two different loci in the genome. If they were unlinked/uncorrelated,
then knowing the allele at one locus would tell you nothing about the likely
allele at the other locus. LD can occur either because two loci are physically
linked by being very close together in the genome, or, it can also arise due
to a history of correlated selection.

When two loci are in LD then selection on an allele at one locus can cause
the frequency of a particular allele at the other locus to also change. This
is called "genetic hitchhiking". When selection is strong, it can cause rapid
fixation of an allele such that there is not enough time for recombination to
occur and unlink the new allele from the random neutral alleles around it. This
leads to a loss of diversity surrounding the adaptive allele (Fig. 5.14).

### Most mutations are deleterious
Selection that removes deleterious mutations from a population is called
"purifying selection". Deleterious mutations may persist in populations for
several reasons that we have learned about (correlated evolution, trade-offs,
linkage disequilibrium, recessiveness). But the most likely reason of all
is that they are very common and frequently re-introduced into a population.
The re-introduction and purging of deleterious alleles is called "mutation-selection
balance."






<!-- 
### Shifting Balance Theory
Wright developed the ["shifting balance theory"](https://www.nature.com/scitable/topicpage/sewall-wright-and-the-development-of-shifting-30508/).
This proposed that the effects of pairs of alleles should not always be 
modeled as simply being *additive* (sum of their individual effects), but 
should also include the potential for *non-additive* effects, such
as epistasis. Epistatic effects such as dominance were well known 
from Mendel's earlier work, but later work revealed many additional
forms of epistasis, including incomplete dominance (intermediate
phenotypes due to interactions, not just additive effects; 
e.g., pink). Wright examined what would happen under theoretical models
where these different modes of heterozygote phenotypes have different
fitness consequences (e.g., lower than either homozygote, intermediate, 
or greater).

Wright developed the concept of adative landscapes to describe the 
predicted evolution of populations given a relationship between 
genotypes and fitness. Selection will push populations upward toward
genotypes of higher fitness, whereas genetic drift or random mutations
will cause populations to disperse around regions of similar fitness

At its core, the shifting balance theory is a process that permits populations
to hold onto selective gains (i.e., local fitness peaks in the adaptive 
landscape) while still being able to randomly explore neighboring genotype 
space for possibly superior peaks. Wright's solution to these conflicting 
aims was population subdivision. He thought that many, if not most, species
were subdivided into small populations that exchanged only a few migrants 
with each other but were not completely isolated (Wright, 1931, 1932, 1977, 
1978). Because of the small size of each of these populations, genetic drift 
would have a significant effect on the genetic composition of each, thus 
allowing the populations to differentiate genetically by an appreciable amount. 
In this way, each of the populations would act as a small experiment in 
evolution (Wade & Goodnight, 1998).

- Phase 1, the exploratory phase, is characterized by the action of genetic 
drift. As a result, the small populations move around in genotypic space.
Most stay on the suboptimal fitness peak, but some get caught in adaptive valleys.
- In phase 2, natural selection causes the populations that are in the adaptive
valleys to move through genotypic space toward new, higher-fitness peaks.
- Finally, in phase 3, those populations that are at higher fitness peaks send 
off migrants to the other populations, and these migrants cause the other 
populations to move to the higher fitness peaks. Eventually, all of the 
populations (the metapopulation) move to the higher fitness peak as a result 
of this process.

Remains controversial. 

Fisher argued that ecological factors would change the adaptive landscape 
faster than populations could shift between peaks via the shifting balance 
theory. In other words, according to Fisher, hills would become valleys and 
valleys would become hills faster than populations could move from one hill
to the next (Fisher, 1958).

 -->


<!-- ## Additional resources referenced in lecture (not required reading) -->
<!-- - Wright, S. Evolution in Mendelian populations. Genetics 16, 97–159 (1931).  -->
<!-- *This classic paper introduces the concept of a fitness landscape.* -->
<!-- - Wagner GP. 2010. The measurement theory of fitness. Evolution. 64:1358–1376. -->

<!-- 
- Gould Panglossian paradigm. *This classic paper questions the common practice
of assigning an adaptationist hypotheses to every biological observation. In 
many cases, non-adaptive processes may explain organismal features.*

 -->