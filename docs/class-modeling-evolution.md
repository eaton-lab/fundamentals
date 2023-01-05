---
title: Modeling Evolution
module: 2
session: 8
day2022: M/10/3/2022
---

# Modeling Evolution

Note: Essays are due tonight. Share updates in response to survey.  

----

## Outline
- Lecture: **Review of Genetics** 
	- Review of neutral theory and its predictions.
	- Measuring genomic selection methods
- Discussion: Kern vs Jensen on Neutral Theory
- *Break*
- Lecture: **Extending WF Models**
	- Wright Fisher Models and evolutionary simulations
	- Genealogical vs genetic ancestry (Briefly)

----
## Assigned for next class

- GCBias: [How much of your genome do you inherit from a particular grandparent?](https://gcbias.org/2013/10/20/how-much-of-your-genome-do-you-inherit-from-a-particular-grandparent/)
- GCBias: [How much of your genome do you inherit from a particular ancestor?](https://gcbias.org/2013/11/04/how-much-of-your-genome-do-you-inherit-from-a-particular-ancestor/)
- GCBias: [How lucky was the genetic investigation in the Golden State Killer case?](https://gcbias.org/2018/05/07/how-lucky-was-the-genetic-investigation-in-the-golden-state-killer-case/)
- [notebooks 2: Wright-Fisher Models](https://mybinder.org/v2/gh/genomics-course/2020-fundamentals/1d5df3348de8a4214c81b5231a71ba3f0e3bb47d?filepath=notebooks)
<!-- - [notebooks 3: Coalescent Genealogies](https://mybinder.org/v2/gh/genomics-course/2020-fundamentals/1d5df3348de8a4214c81b5231a71ba3f0e3bb47d?filepath=notebooks) -->

Consider the following question while reading the articles above:  

Each chromosome represents a mosaic of segments inherited from different
ancestors, however, over many generation, many true ancestors may eventually 
contribute 0% of DNA to some of their descendant's genomes. How should this 
influence how we use "genetic ancestry" (DNA sequencing and statistics) to 
identify "genealogical ancestry" (who were the ancestors of a given person)?

----

## References
- Wikipedia on Neutral Theory.
- Wikipedia on MK test.
- Futuyma textbook chapter 7.
- https://en.wikipedia.org/wiki/McDonald%E2%80%93Kreitman_test
- https://en.wikipedia.org/wiki/Haldane%27s_dilemma#The_cost
- https://en.wikipedia.org/wiki/Genetic_load
----

## Lecture slides

**:octicons-browser-16:{ .notebook-thump } [Link to Lecture Slides](../lectures/modeling-evolution/)**

----

## Lecture notes

### Genetic variation within species

Polymorphism (genetic variation) is spread unevenly across the genome.
It is typically higher in non-coding regions of the genome, between genes
or in introns. Within coding genes, the third codon position usually does
not cause a change to the amino acide sequence (silent mutation), and thus
has a neutral effect. These sites also exhibit greater polymorphisms.


If most of the variation within genomes results from random genetic drift
acting on genetic variation with no selective effect on fitness, then we 
can predict the expected genome-wide heterozygosity as:

pi = 4 * Ne * mu

mu = neutral mutation rate.  
2N = expected time until coalescence of two gene copies
2 = mutation could fall on either branch.

If either the mutation rate (mu) or population size (Ne) increases, then
we expect more genetic variation.

Most of the genome is non-coding, and thus mostly neutral. For example, 
only \~2% of the human genome is coding. Thus, coding regions contribute 
little to average genome-wide diversity. 

Coding regions, especially at nonsynonymous sites, are under **selective
constraint**. If these genes are disrupted they usually have negative 
fitness consequences. And thus most mutations to these regions are 
deleterious. These mutations are usually removed by purifying selection.

### Across chromosomes

Polymorphisms also vary across chromosomes owing to structural variation 
affecting processes like recombination. Regions with high recombination
tend to be more polymorphic. (Fig.-7.9). This is because selection can 
act on individual sites more effectively, since recombination breaks their
linkage to neighboring sites. This allows selectiont to fix one site while
maintaining variation at nearby sites. 

By contrast, near centromeres, recombination is highly reduced, and selection
on one site causes linked selection on very many neighboring sites.


### Haldane's "cost of selection" (1957)
<!-- Haldane was interested in the "genetic load" of a population -- 
the difference between the fitness of an average genotype in a population and 
the fitness of some reference genotype, which may be either the best present
in a population, or may be the theoretically optimal genotype. 
 -->
States that for selection to act on a single benefical allele at a locus 
long enough for it to become fixed requires that a large proportion of the 
population that does not have this allele fails to reproduce. This sets an
upper limit on the strength of selection.

The consequence of this is upper limit is that selection takes a long time
to fix a benefical mutation. Also, under the assumption of unlinked loci, 
it cannot act on more than one locus at a time. Thus, a population maintains
a "mutational load" from other alleles that cannot yet experience 
selection, lowering the population's absolute fitness.

Note, Haldane (1957) made this calculation before we had any methods for 
estimating DNA sequencing, or even measuring variation in proteins. He 
estimated that it takes 300 generations on average for a beneficial allele
to become fixed, just by assuming the rate of death/turnover in a population.
From this he estimated that it would take 300,000 generations to produce 
the type of differences that we often observe between species (estimated 
as at least one different >1,000 loci). 

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
```

### Neutral Theory of Molecular Evolution
With newly available data to estimate the amount of variation in protein
sequences in a population, using gel electophoresis, it was found that 
there was much higher variation than expected if selection causes the 
rapid fixation of variation (agreeing with Haldane). Kimura proposed that
most substitutions are neutral as an explanation.

Kimura (1968) "Evolutionary Rate at the Molecular Level"  
Estimated the rate of protein evolution from 3 loci and agreed
with Haldane's cost of selection, that rates of protein evolution are 
**too rapid** to be compatible with natural selection driving substitutions. 
- "Calculating the rate of evolution in terms of nucleotide substitutions
seems to give a value so high that many of the mutations involved
must be neutral ones." 

Kimura and Ohta (1971) "Protein Polymorphism as a Phase of
Molecular Evolution". Predicted that rates of substitutions causing 
divergence between species accumulate according to the neutral mutation 
rate, and are thus relatively constant. Supported by protein sequence
data. 
- "Probably the strongest evidence for the theory is the remark-
able uniformity for each protein molecule in the rate of mutant
substitutions in the course of evolution."
- "It is proposed that random genetic drift of neutral mutations in finite
populations can account for observed protein polymorphisms."

Kimura (1977) "Preponderance of synonymous changes as evidence for the 
neutral theory of molecular evolution". Showed that 3rd codon positions
which do not cause coding changes occur at the neutral rate, not faster,
as would be predicted if most genes experienced selection.
- "ln my opinion, various observations suggest that as the
functional constraint diminishes the rate of evolution con-
verges to that of the synonymous substitutions. If this is valid,
such a convergence (or plateauing) of molecular evolutionary
rates will turn out to be strong supporting evidence for the
neutral theory"

Kimura (1983) published the book "The Neutral Theory of Molecular Evolution" 
which combined all of these lines of evidence together in its most
complete form. Proposed that the theory could alternatively be called the
"mutation-random drift theory", since it does not enforce that all 
mutations are neutral. Deleterious mutations are removed, and nearly neutral
mutations can fix by drift. It does not reject rare beneficial mutations, 
or the possibility for balancing selection to maintain polymorphisms, but
states that these are very rare in comparison to neutral variation.


### Genomics signatures of selection

#### MK-test
The McDonald–Kreitman test is used to measure the amount of adaptive 
evolution that has occurred within a species by measuring 
the proportion of substitutions that resulted from positive selection
To do this, it compares the amount of variation within a species 
(polymorphism) to the divergence between species (substitutions) at two 
types of sites: neutral and non-neutral. (Usually it is applied to protein
coding sequences to compare synonymous (neutral) and non-synonmyous 
(non-neutral) changes.)


- Ds: the number of synonymous substitutions per gene (fixed diff btwn spp)
- Dn: the number of non-synonymous substitutions per gene (fixed diff btwn spp)
- Ps: the number of synonymous polymorphisms per gene (variable within spp 1)
- Pn: the number of non-synonymous polymorphisms per gene (variable within spp 1)

Null hypothesis: the ratio of nonsynonymous to synonymous variation within 
a species is going to equal the ratio of nonsynonymous to synonymous variation
between species (i.e. Dn/Ds == Pn/Ps).

Negative selection: deleterious variants will be removed at nonsynon sites
WITHIN species, but neutral mutations will still fix between species, thus
the within species ratio will be lower than the between species ratio
- (Dn/Ds < Pn/Ps)
- (25/100 < 50/100)

Positive selection: The ratio of nonsynonymous to synonymous variation within
species is lower than the ratio of nonsynonymous to synonymous variation 
between species (i.e. Dn/Ds > Pn/Ps) when we observe positive selection. 
Since mutations under positive selection spread through a population 
rapidly, they don't contribute to polymorphism but do have an effect on 
divergence.
- (Dn/Ds > Pn/Ps)
- (200/100 > 100/100)

#### Selective sweep
- Chapter 5



#### Linked selection ("hitchhiking")


### Genomic Methods for Measuring Selection

#### dn/ds


#### Correlation of recombination rate x polymorphism 
One of the most striking impacts of natural selection on genomes is the 
near universal correlation between rates of recombination and levels of 
polymorphism... evidence of linked selection.
(Hahn 2008; Cutter and Payseur 2013; Corbett-Detig et al. 2015;

#### Sliding windows (genome scan)
Evidence for adaptation can be found by scanning the genome for signatures
of divergence between populations. An unusually high level of divergence 
between populations can show evidence of adaptation. (Fig.-7.23).

#### Fst (fixation index)



### Mutation limits versus standing variation
Does most adaptation arise from new beneficial mutations that arise at 
very low frequence (p=1/2N), or from selection acting on existing 
(standing) genetic variation when it becomes adaptive in a new environment
(p=?/2N)? There is evidence for both, but in nature, it seems selection
on standing genetic variation may be common.

Example, 


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
