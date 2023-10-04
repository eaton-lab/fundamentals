---
title: Modeling Evolution
module: 2
session: 8
day2022: M/10/3/2022
day2023: M/10/2/2023
---

# Modeling Evolution

----

## Assignments due for this class (M: 10/2/2023)
- **Evolution 5th edition, Chapter 4** (Mutation and Variation)
Introduction to genetics and genetic variation
- Complete Courseworks Quiz
- complete [interactive exercises 0, **1**, and 6](https://pinky.eaton-lab.org) (Hardy-Weinberg Equilibrium)


## Assignments due for next class (W: 10/4/2023)
- **Evolution 5th edition, Chapter 6** (Genetic drift and neutral theory)
- GCBias: [How much of your genome do you inherit from a particular grandparent?](https://gcbias.org/2013/10/20/how-much-of-your-genome-do-you-inherit-from-a-particular-grandparent/)
- complete Courseworks Quiz
- complete [interactive exercises 0, 1, **2**, and 6](https://pinky.eaton-lab.org) (WF models)

-----

## Outline
- Review of Genetics
- Review of Notebook exercise 1 on Hardy-Weinberg
- Genetic Drift
- *Break*
- Wright Fisher Models
- Coalescent
- Neutral Theory

----

## Slides

- [:material-presentation-play: *Link to Lecture Slideshow*: **Modeling-evolution**](../lectures/modeling-evolution/)

----

## Lecture notes

### Genetic drift

Genetic drift is the random change in allele frequencies caused by chance events (survival, reproduction, meiosis), not selection. A "random walk". 

- Allele frequencies can change due to random events like being stepped on.
- Allele frequencies can change due to random sampling/mating, such as in 
which gametes happen to fuse to form new zygotes.

Key features of genetic drift (e.g., Fig. 6.3):

1. drift is unbiased: an allele frequency can go up or down with equal probability.
2. drift is stronger in small populations. The random fluctuation (variance)
of allele frequencies from one generation to the next is larger in small 
populations simple as a consequence of law of large numbers.
3. drift causes variation to be lost: eventually an allele will either become
fixed or lost by genetic drift.
4. drift causes divergence between populations: different populations that
inherit polymorphisms will each randomly fix or lose variation, sometimes 
leading to the fixation of different alleles. 
5. drift can cause alleles to become fixed. This can happen by chance, without
requiring natural selection. The probability that an allele becomes fixed by
genetic drift is 1 / 2N. 

Diversity and divergence (e.g., Fig. 6.4): Consider an initial population containing
genetic diversity that is divided into two, where each population inherits the
same allele frequencies. Over multiple generations, genetic drift will lead to
the random loss or fixation of alleles at each variable locus. This causes a 
loss of genetic diversity within each population. Viewed as a whole, the two
populations will exhibit a greater number of homozygotes, and a deficit of 
heterozygotes, compared to Hardy-Weinberg equilibrium. This is because the
existence of **population structure** between them causes a deviation from 
the HW model assumptions. However, within each population these assumptions
are not violated, and so each population is individually in HW equilibrium.
We will see more examples later of analyzing genetics at multiple levels, both
within and between multiple populations.


### Strength of genetic drift

The strength of genetic drift is measured by the effective population size (Ne). This is an emergent property of a population describing the probability
that two samples share the same ancestor one generation in the past. It is 
affected by the number of individuals in a population, the mating strategy, 
by separate sexes, and by selection. 

To start, however, it helps to think about
Ne in the context of a simple *model* of evolution (e.g., the Wright-Fisher process, described below). In this model, we consider the same idealized population scenario that is assumed by the Hardy-Weinberg model where 
evolution does not occur, but we then relax a single assumption of this model, introducing a finite population size, instead of infinite, so that 
genetic drift will occur. The rate of genetic drift is determined by the population size (N). In this case, and this case only, the effective 
population size (Ne) is equal to the population size (N). In most real world
scenarios the effective population size is smaller than the actual population
size.

### Population size effects

**Population bottlekneck**: An event where the population size is greatly reduced can lead to a significant loss of genetic diversity by genetic drift.

**Founder event**: When a new population is begun from a small number of individuals from a larger population. This small population experiences a 
strong bottlekneck such that is exhibits a subset of genetic diversity present
in the larger population from which it was founded. This is typical of island
populations.

Example: genetic diversity of human populations decreases with increasing
distance away from sub Saharan Africa, representing the continued stepping-stone
path of human migration through recent time as a series of sequential founder
events (e.g., Fig. 6.7)


### Wright-Fisher model

The Wright-Fisher process is considered one of the simplest models in population genetics. Compared to an idealized population, in which allele frequencies are always in HW equilibrium, and do not change, the WF process by default relaxes at least one assumption: population sizes are not infinite.

A WF process can be simulated quite easily. It is a discrete-time process where each generation 2N haploid gene copies exist in a population of census size N. Because the population is assumed to be randomly mating we can randomly assign haploid gene copies to be grouped into diploid individuals. To simulate one generation of the WF process one needs only to create a new generation of 2N haploid copies and to randomly sample 2N copies, with replacement, from the previous generation to serve as their parents.

The result of this random mating process, played out over multiple generations, creates a visual process of gene copies being inherited. The process also 
gives rise to a genealogy for any set of gene copies examined. Lines can be
drawn to connect gene copies in each generation from parent to offspring. The
expected time backwards until two gene copies share a common ancestor is 
determined only by Ne.

**Coalescence**: The joining of two gene copies into a common ancestor 
backwards in time. The probability that two copies share an ancestor one 
generation in the past is 1/2Ne. The expected time until they share a common
ancestor is 2Ne. 


### Genetic variation within species

Polymorphism (genetic variation) is spread unevenly across the genome.
It is typically higher in non-coding regions of the genome, between genes
or in introns. Within coding genes, the third codon position usually does
not cause a change to the amino acid sequence (silent mutation), and thus
has a neutral effect. These sites also exhibit greater polymorphisms.

If most of the variation within genomes results from random genetic drift
acting on genetic variation with no selective effect on fitness, then we 
can predict the expected genome-wide heterozygosity as:

$$ \pi = 4 \times Ne \times \mu $$

- $\mu$ = neutral mutation rate per-site per-generation.
- 2$Ne$ = expected time until coalescence of two gene copies.  
- $\times$ 2 = because mutation can occur on either branch.

If either the mutation rate ($\mu$) or population size (Ne) increases, then
we expect more genetic variation. This is because $\mu$ is measured in units
of per-site per-generation, and Ne has the effect that larger values lead
to longer branches on a genealogy in units of generations. Thus, longer
genealogies have more opportunity for mutations to accumulate.

Most of the genome is non-coding, and thus mostly neutral. For example, 
only \~2% of the human genome is coding. Thus, coding regions contribute 
little to average genome-wide diversity measurements.


### Across chromosomes
Polymorphisms also vary spatially across chromosomes owing to structural variation affecting processes like recombination. Regions with high recombination tend to be more polymorphic. This is because selection can act on individual sites more effectively, since recombination breaks their linkage to 
neighboring sites. This allows selection to act on one site while
maintaining variation at nearby sites.

By contrast, near centromeres, recombination is highly reduced, and selection
on one site causes linked selection on very many neighboring sites (e.g., Fig. 6.11).


### Genetic drift and natural selection
Both genetic drift and natural selection can occur simultaneously to influence
allele frequency changes in a population. In our textbook chapter 5 we examined
equations for the rate of fixation of an allele under selection *in the absence
of genetic drift*. And in chapter 6 so far we have examined the probability
that an allele becomes fixed by genetic drift. But what happens when both 
processes are acting? In this case, the math becomes an amalgamation of both
methods, where the direction of allele frequency change can be predicted by selection, but can also vary randomly from this trajectory with variance 
depending on the strength of genetic drift.

When drift is very weak (populations are large), it can be effectively ignored, whereas when drift is very strong (populations are small), even alleles with strong selection coefficients may evolve randomly because genetic drift is so much stronger.

A mutation that is strongly selected in one species may evolve as if it were
effectively neutral in another, simple because the two differ in their effective
population sizes.


### Selective constraint
Coding regions, especially at nonsynonymous sites, are under **selective
constraint**. If these genes are disrupted they usually have negative 
fitness consequences. And thus most mutations to these regions are 
deleterious. These mutations are usually removed by purifying selection.

Several methods for detecting selection are based on comparing synonymous 
and non-synonymous sites for evidence of positive or purifying selection.

<!-- 
### Haldane's "cost of selection" (1957)
Haldane was interested in the "genetic load" of a population -- 
the difference between the fitness of an average genotype in a population and 
the fitness of some reference genotype, which may be either the best present
in a population, or may be the theoretically optimal genotype. 

States that for selection to act on a single benefical allele at a locus 
long enough for it to become fixed requires that a large proportion of the 
population that does not have this allele fails to reproduce. This sets an
upper limit on the strength of selection.

The consequence of this upper limit is that selection takes a long time
to fix a benefical mutation. Also, under the assumption of unlinked loci, 
it cannot act on more than one locus at a time. Thus, a population maintains
a "mutational load" from other alleles that cannot yet experience 
selection, lowering the population's absolute fitness.

Note, Haldane (1957) made this calculation before we had any methods for 
DNA sequencing, or even measuring variation in proteins. He estimated that 
it takes 300 generations on average for a beneficial allele to become fixed,
just by assuming the rate of death/turnover in a population.
From this he estimated that it would take 300,000 generations to produce 
the type of differences that we often observe between species (estimated 
as at least one difference / 1,000 loci). 

Summarized by Val Valen as "Haldane's dilemma": Since a high number 
of deaths are required to fix one gene rapidly, and dead organisms do not 
reproduce, fixation of more than one gene simultaneously would conflict. 
Note that Haldane's model assumes independence of genes at different loci; 
if the selection intensity is 0.1 for each gene moving towards fixation, 
and there are N such genes, then the reproductive capacity of the species 
will be lowered to 0.9^N times the original capacity.
Therefore, if it is necessary for the population to fix more than one 
gene, it may not have reproductive capacity to counter the deaths.

```Python
ngenes = 10
original_fitness = 100
ngenes * 0.9 ** ngenes
# = 34.8 (The population's absolute fitness is now ~1/3 what it used to be!)
``` -->


### Neutral Theory of Molecular Evolution
With newly available data to estimate the amount of variation in protein
sequences in a population, using gel electophoresis, it was found that 
there was much higher variation than expected if selection causes the 
rapid fixation of variation (something noted earlier by Haldane). Kimura proposed that most substitutions are neutral as an explanation.

**Kimura (1968)** "Evolutionary Rate at the Molecular Level"  
Estimated the rate of protein evolution from 3 loci and agreed
with Haldane's cost of selection, that rates of protein evolution are 
**too rapid** to be compatible with natural selection driving most 
substitutions. 

- "Calculating the rate of evolution in terms of nucleotide substitutions
seems to give a value so high that many of the mutations involved
must be neutral ones." 

**Kimura and Ohta (1971)** "Protein Polymorphism as a Phase of
Molecular Evolution". Predicted that rates of substitutions causing 
divergence between species accumulate according to the neutral mutation 
rate, and are thus relatively constant. Supported by protein sequence
data. An explanation for the molecular clock.

- "Probably the strongest evidence for the theory is the remarkable uniformity
for each protein molecule in the rate of mutant substitutions in the course 
of evolution."
- "It is proposed that random genetic drift of neutral mutations in finite
populations can account for observed protein polymorphisms."

**Kimura (1977)** "Preponderance of synonymous changes as evidence for the 
neutral theory of molecular evolution". Showed that 3rd codon positions
which do not cause coding changes occur at the neutral rate, not faster,
as would be predicted if most genes experienced selection.

- "ln my opinion, various observations suggest that as the functional 
constraint diminishes the rate of evolution converges to that of the 
synonymous substitutions. If this is valid, such a convergence (or plateauing)
of molecular evolutionary rates will turn out to be strong supporting evidence
for the neutral theory"

**Kimura (1983)** published the book "The Neutral Theory of Molecular Evolution" 
which combined all of these lines of evidence together in its most
complete form. 

- Proposed that the theory could alternatively be called the
"mutation-random drift theory", since it does not enforce that all 
mutations are neutral. Deleterious mutations are removed, and nearly neutral
mutations can fix by drift. It does not reject rare beneficial mutations, 
or the possibility for balancing selection to maintain polymorphisms, but
states that these are very rare in comparison to neutral variation.

- Also predicted and showed higher rate of substitutions in pseudo-genes (duplicated copies of genes that are no longer functional). These genes evolve at a rate at or closer to neutral consistent with neutral theory.


### Genomics signatures of selection
We will return to this subject in greater detail next week.

#### MK-test
The McDonald–Kreitman (MK) test is used to measure the amount of adaptive 
evolution that has occurred within a species by measuring the proportion of
substitutions that resulted from positive selection.

To do this, it compares the amount of variation within a species 
(polymorphism) to the divergence between species (substitutions) at two 
types of sites: neutral and non-neutral. (For example, it is applied to
protein coding sequences to compare synonymous (neutral) and non-synonmyous 
(non-neutral) changes.)

- Ds: the number of synonymous substitutions per gene (fixed diff btwn spp)
- Dn: the number of non-synonymous substitutions per gene (fixed diff btwn spp)
- Ps: the number of synonymous polymorphisms per gene (variable within spp 1)
- Pn: the number of non-synonymous polymorphisms per gene (variable within spp 1)

Null hypothesis: the ratio of nonsynonymous to synonymous variation within 
a species is going to equal the ratio of nonsynonymous to synonymous variation
between species (i.e. `Dn/Ds == Pn/Ps`).

Negative selection: deleterious variants will be removed at nonsynon sites
WITHIN species, but neutral mutations will still fix between species, thus
the within species ratio will be lower than the between species ratio

- (`Dn/Ds < Pn/Ps`)
- e.g., (25/100 < 50/100)

Positive selection: The ratio of nonsynonymous to synonymous variation within
species is lower than the ratio of nonsynonymous to synonymous variation 
between species (i.e. Dn/Ds > Pn/Ps).
Since mutations under positive selection spread through a population 
rapidly, they don't contribute to polymorphism but do have an effect on 
divergence.

- (`Dn/Ds > Pn/Ps`)
- (200/100 > 100/100)


#### Selective sweeps
When strong selection causes the rapid fixation of a new allele it will cause
a simultaneous fixation of many nearby alleles that are in linkage disequilibrium
with the selected alleles. This creates a "dip" in diversity at a spatial location
in the genome, with a rapid or gradual decay back to normal levels of diversity
as you look farther away from the selected site. This pattern is temporal, and
is strongest at the time when selection is occurring of has recently occurred. 
Genetic diversity will eventually accumulate in this region again and the pattern
will disappear, leaving the substitutions that can be analyzed with MK-test, but
no longer a spatial pattern.


## Debate on neutrality versus selection

- Kern, Andrew D., and Matthew W. Hahn. 2018. “The Neutral Theory in Light of Natural Selection.” Molecular Biology and Evolution 35 (6): 1366–71. https://doi.org/10.1093/molbev/msy092. 

Argues that the neutral theory is not supported in light of newer genomic evidence.
Two main arguments are that (1) some studies have shown that >20% of genes show 
evidence of selection in Drosophila; and (2) The common correlation between
genetic diversity and recombination rates suggests that linked-selection, i.e.,
hitchhiking, is affecting diversity patterns at most places throughout the genome.

- Jensen, Jeffrey D., Bret A. Payseur, Wolfgang Stephan, Charles F. Aquadro, Michael Lynch, Deborah Charlesworth, and Brian Charlesworth. 2019. “The Importance of the Neutral Theory in 1968 and 50 Years on: A Response to Kern and Hahn 2018.” Evolution 73 (1): 111–14. https://doi.org/10.1111/evo.13650.

This group of authors respond and say that the neutral theory is alive and well.
They say that the other authors have a misunderstanding of the claims of neutral
theory, particularly in its interpretation as a "nearly-neutral" theory that
defines most mutations as effectively neutral, and most non-neutral mutations
as deleterious. The authors summarize these five points in response to Kern and
Hahn.

1. Most mutations are neutral with respect to their fitness effects.
2. Most mutations that do affect fitness are deleterious and most selection 
that occurs in the genome is purifying selection that removes these variants.
3. Demographic history (i.e., changes in population size, or the fusion and
fission of populations) can affect how drift acts on neutral variation, leading
to differences across the genome that may be misinterpreted as evidence of 
selection.
4. The joint effects of drift and purifying selection can together shape
genome-wide patterns of variation, such as a correlation between recombination
and diversity. This is consistent with neutral theory.
5. Beneficial mutations arise rarely, and when they do, can cause hitchhiking
effects that affect nearby variation. However, this occurs rarely, and the 
effects are highly localized.


<!-- 
#### Correlation of recombination rate x polymorphism 
One of the most striking impacts of natural selection on genomes is the 
near universal correlation between rates of recombination and levels of 
polymorphism... evidence of linked selection.
(Hahn 2008; Cutter and Payseur 2013; Corbett-Detig et al. 2015;

#### Sliding windows (genome scan)
Evidence for adaptation can be found by scanning the genome for signatures
of divergence between populations. An unusually high level of divergence 
between populations can show evidence of adaptation. (Fig.-7.23).

### Mutation limits versus standing variation
Does most adaptation arise from new beneficial mutations that arise at 
very low frequence (p=1/2N), or from selection acting on existing 
(standing) genetic variation when it becomes adaptive in a new environment
(p=?/2N)? There is evidence for both, but in nature, it seems selection
on standing genetic variation may be common.

Gene flow or introgression from other populations or species can also 
introduce new beneficial alleles into a population.

### Selection against introgression
A reverse pattern can also be observed, where selection acts against ...


### Wright-Fisher Models


### Genealogy


### Coalescent


### 


- WF models
- genealogy
- TMRCA leads to equation for expected heterozygosity. Eq 7.1.
- In a randomly mating population hetero is the same definition as population genetic diversity.
- Recombination means that each genome is a mosaic containing the diversity from many ancestors. We can do a lot with one genome!

### Discussion Questions

Kern and Hahn
- They provide many examples where selection has been detected from genomic
data. Does this refute the neutral theory? What level evidence would be 
convincing: selection at one gene, many genes, all genes?

- They start by arguing against two main lines of evidence by Kimura: the
'cost of selection' and the 'rate of substitutions'. Did you understand 
these arguments? Why do you think the authors presented this evidence the
way that they did?

- 'Linked selection' is the idea that most regions of the genome experience
selection, and thus reduced polymorphism, as a consequence of being in 
linkage disequilibrium with a region that did experience selection.



## References
- Wikipedia on Neutral Theory.
- Wikipedia on MK test.
- https://en.wikipedia.org/wiki/McDonald%E2%80%93Kreitman_test
- https://en.wikipedia.org/wiki/Haldane%27s_dilemma#The_cost
- https://en.wikipedia.org/wiki/Genetic_load
----
 -->