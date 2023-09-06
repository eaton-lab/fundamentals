---
title: Selection and Fitness
module: 1
session: 3
day2022: W/9/14/2022
day2022: W/9/15/2022
---

# Selection and Fitness

Recap biodiversity through time, discuss extinction debate, and introduce
natural selection and the genetical theory of of natural selection.

---
## Assigned and due for this class (9/15/23)
- **Evolution 5th edition, Chapter 17** (The History of Life; 26 pages)
- **Evolution 5th edition, Chapter 18** (The Evolution of Biological Diversity; 22 pages)
- **Pyron extinction opinion**: A short article arguing for the constancy
of extinction throughout history and its relevance to conservation.
- **Safina extinction response**: A response to the article above.
- complete Courseworks Quiz 2


## Assignments due before next class
- **Evolution 5th edition, Chapter 3** (Natural Selection and Adaptation; 21 pages)
This chapter delves into the process of *natural selection* how to define 
adaptations, and how adaptation has shaped the diversity of life.
- **Evolution 5th edition, Chapter 5** (Genetical Theory of Natural Selection;
32 pages) A mathematical framework for measuring selection and fitness.

---


## Class session outline
- Lecture: review of chapters 17-18
	- Major evolutionary transitions
	- Uncertainties in the fossil record
	- Biogeography and diversity through time.
- Discussion: Pyron vs. Safina
**break**
- Lecture: preview of chapter 3 (natural selection and adaptation)
	- ...
- Lecture: preview of chapter 4 (mutation and variation)
	- ...


---

## Class session outline
- [:material-presentation-play: *Link to Lecture Slideshow*: 
**Selection and Fitness**](/docs/lectures/selection-and-fitness/)
- Review chapter 3 natural selection.
- Introduce topics from ch. 5-6
		- Fitness landscapes
		- Evolutionary Optima
		- Measuring selection coefficients
		- Fitness measurements
		- Adaptation/spandrels
- *Break*
- Discussion:
	- Orr (2009). “Fitness and Its Role in Evolutionary Genetics.” 

----


----

<!-- TODO: decide on breakdown of topics between sessions 
	 3 Natsel and 4 GeneticalTheory. How much quantitative genetics, how
	 much can we do while having not yet delved into inheritance, should
	 we just do mini-inheritance session? ...no.
-->

## Lecture notes
This lecture focuses on the quantitative methods for describing and measuring
phenotypic variation, additive genetic variance, fitness, and selection. It
is largely a review of foundational work from the Modern Synthesis, with 
updated examples from more modern implementations.

TODO...

### Phenotypic variation
...

### Additive genetic variance
*Additive genetic variance* is the proportion of variance in phenotype
that can be explained by genetic variation, and not by the environment.
...

### Absolute fitness
The concept of fitness is fundamental to evolutionary biology.

If the mean absolute fitness in a population increases due to adaptative
evolution this can increase the population density, geographic range, 
or growth rate in ways that may reduce the probability of population 
extinction due to random fluctuations or environmental change.

The rate of evolution of the mean absolute fitness of a population 
(i.e., the change in fitness in response to selection) provides a 
meaningful approach of measuring the rate of adaptation. 

## Fisher's fundamental theorem of natural selection
*The rate of increase in fitness of any organism at any time is equal
to its genetic variance in fitness at that time*. In other words, 
there must be variation in fitness for selection to ...

In Fisher's most famous work on evolution, *The genetical Theory of 
Natural Selection* (1930), he described a model for the rate of 
adaptive evolution that has since come to be called Fisher's fundamental
theorem.

This shows that the change in mean *relative fitness* due to selection 
(...) equals the additive genetic variance in relative fitness in a population
($\sigma^2_A$), making the additive genetic variance in relative fitness 
arguably the most important evolutionary parameter for a population.




$$ w = \sigma^{2}_{A}(s) $$




### Adaptations
Nature is full of apparant design: a fit between an organism's phenotype 
and a specific function (3.1, 3.2). Darwin's theory of natural selection 
provides an explanation for this apparent design. It is the outcome of a 
mindless process, natural selection. It does not require an intelligent designer.

This had an enormous impact on the way in which we understand the natural
world... Transformed societies through the way we see the world, and the 
way in which we view humans to be part of it (We also evolved). 

Evidence of adaptations is used widely to support the theory of evolution
by natural selection, since adaptations are an expected outcome of natural 
selection. But how exactly do you define an adaptation, and how can 
hypotheses about adaptations be tested?


### Definitions
**Adaptation:** *a characteristic that enhances (or enhanced) the survival 
or reproduction of organisms that bear it, relative to alternative character
states.*

Adaptive evolution may be slow as Darwin proposed, but nevertheless we now 
have many examples where it has been clearly observed and measured within 
our lifetimes.
	- Soapberry example (Fig.-3.x)
	- resistance to insecticide, herbicide, antibiotics (Fig-3.x)
	- response to overexploitation (Fig.-3.5)

**Natural selection:** *any consistent difference in fitness among 'different 
classes' (e.g., genotypes) of biological entities based on their 
phenotypes.*

**Fitness:** (reviewed in our article discussion today) *The number of 
offspring an individual leaves in the next generation.* Or, measured
as multiple components of fitness for multiple life stages. 

**Important Note**: Natural selection can occur without causing evolution 
(e.g., no heritability of selected trait), and similarly, evolution 
can occur without natural selection (e.g., genetic drift changes allele
frequencies by chance). Natural selection happens anytime that a 
non-random set of entities differ in fitness. For evolution to happen, 
the non-random variation affecting their fitness must be heritable.

### Levels of selection
We used the term 'entities' for natural selection earlier, why? 
Because not only individuals experience selection. Genotypes or, 
b/c of recombination, individual genes (in sexual organisms), can 
also have differences in success/fitness (replication to next 
generation). Thus selection can act on gene copies in a population, 
combination of gene copies in a population (genotypes), individuals
in a population (classic concept of selection), or even on different
populations (group selection; thought to be less common).

Selfish genetic elements: Segments of DNA or RNA that can replicate
*within* genomes. This is beneficial because when the genome is 
replicated this leads to further replication of the copies
of this element in the genome. Examples are **transposable elements**
(TEs). These often have either no effect on fitness, or only slightly
deleterious effects, and thus accumulate in genomes.

TODO Reference: transposable element diversity and distribution in genomes.

### Adaptive/Fitness landscape:

A bivariate or multivariate plot showing fitness x phenotype(s), or 
fitness x genotypes(s). It is often easier to envision and measure
for phenotypes, which may vary continuously in a population, than 
for genotypes, which vary discretely. One should thus think of 
genotypes as composing allelic combinations at many loci, such that
you could imagine continuous-like variation.

An adaptive landscape can show both local and global optima, 
represented as *peaks* on the landscape, surrounded by *valleys*
with lower fitness. Movement between fitness peaks on a landscape
is a major topic of interest in evolution. Do populations get
stuck on suboptimal peaks? How easy is it to move between peaks
of similar fitness? How does the depth of valleys influence the
probabilities of shifts?


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

### On adaptations
How to talk about adaptations/selection. We often use shorthand but this
can sound teleological or anthropomorphic in ways that can be misleading
to the general public. It is important to be aware of this and thus when
and where it is appropriate to further define your meaning.
	- selection 'favors' this...
	- selection is a force...
In the end, natural selection is a "statistical differences in 
reproductive success among genes, organisms, or populations, 
based on variation among them".

### Evidence of adaptations
Why are adaptation hard to identify? We will examine this in greater
detail in a later chapter when we describe methods for detecting 
adaptations from signatures in genomes. However, it is useful to 
introduce some of these ideas now as well.

1. A trait may be necessary due to physics, chemistry, constraints. Hemoglobin 
is red b/c of chemistry, not due to selection for blood to be red in color. 
(3.15 exaptation)
2. Trait may have evolved by random genetic drift.
3. May be correlated with another character that evolved by 
	selection, drift, developmental constraint, etc.
4. Phylogenetic history. Why do humans have live birth instead of laying eggs? 
The reason is not because live birth evolved *in humans*, relative to an 
egg-laying ancestor, rather, long ago an ancestor with a variable 
egg-laying/live-birth transition likely experienced selection for one versus 
the other. 

Inconclusive, but suggestive evidence for adaptations
**Complexity**: why does a complex trait exist and not something simpler? 
Example: peacock's feathers. More complex features likely involve costs 
to fitness. Non-functional complexities will usually degrade by 
genetic drift if not maintained by selection.

**Design**: corresponds with optimized models: aerodynamics, heat dissipation, 
camouflage. Similarity with a theoretical optimum model
is highly unlikely to evolve by random genetic drift. 

**Experiments**: show that a trait is better than a modified 
version of it. You could paint a peacock's feathers white and measure
its relative fitness. This shows evidence that the trait is 
more fit in this population than *this alternative*, but does not test
many other alternatives, and does not test whether the alternative 
trait could have evolved in this population's history, and if, whether
it would then be more fit.

**Comparative method**: Phylogenetic patterns can reveal repeated evolution 
that is unlikely by random chance. (e.g., Anoles, Sticklebacks, 
[Viburnum](https://www.nature.com/articles/s41559-022-01823-x)).

**Imperfections and constraints**: Selection acts on existing organisms,
not from scratch, and thus often finds imperfect pathways to solutions.
For example, selection can increase the frequency of genetic variants
in a particular population at a particular time. It cannot fix the best 
of all conceivable variants because that combination may be very 
unlikely to arise by chance. We will return to this in sessions on LTEE 
and in development.


## Additional resources referenced in lecture (not required reading)
- [Orr, H. Allen. 2009. “Fitness and Its Role in Evolutionary Genetics.” Nature Reviews. Genetics 10 (8): 531–39](https://doi.org/10.1038/nrg2603). *This article reviews the many challenges associated with measuring fitness, and the complex ways in which we can conceptualize this relatively simple yet unbounded metric.*
- [Hereford, Joe. 2009. “A Quantitative Survey of Local Adaptation and Fitness Trade‐Offs.” The American Naturalist 173 (5): 579–88.](https://doi.org/10.1086/597611) *A meta-study that compiles results from many individual studies that measured the strength of 
selection coefficients in natural populations.*
- [Kingsolver, J. G., H. E. Hoekstra, J. M. Hoekstra, D. Berrigan, S. N. Vignieri, C. E. Hill, A. Hoang, P. Gibert, and P. Beerli. 2001. “The Strength of Phenotypic Selection in Natural Populations.” The American Naturalist 157 (3): 245–61](https://doi.org/10.1086/319193). *Another similar study to above.*
- Lande and Arndold: ...
- Wright, S. Evolution in Mendelian populations. Genetics 16, 97–159 (1931). *This classic paper introduces the concept of a fitness landscape.*
- Wagner GP. 2010. The measurement theory of fitness. Evolution. 64:1358–1376.