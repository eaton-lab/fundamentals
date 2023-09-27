---
title: Genetic Variation
module: 2
session: 7
day2022: W/9/28/2022
day2023: W/9/27/2023
---

# Genetic Variation and Inheritance
Introduce Mendel and genetics

----

## Assignments due for this class (W: 9/27/2023)
- None. Exam day.


## Assignments due for next class (M: 10/2/2023)
- **Evolution 5th edition, Chapter 4** (Mutation and Variation)
- complete Courseworks Quiz
- complete [interactive exercise 1](...) (Hardy-Weinberg Equilibrium)


----

## Outline
- Exam 1
- *Break*
- Introduction to Ch. 4: Inheritance, Mutation, Recombination.

----

## Lecture slides

- [:material-presentation-play: *Link to Lecture Slideshow*: **Genetic-variation**](../lectures/genetic-variation/)
<!-- **:octicons-browser-16:{ .notebook-thump } [Link to Lecture Slides](../lectures/genetic-variation/)** -->

----

## Lecture notes


### Evolutionary Modeling
During the Modern synthesis Wright, Fisher, and Haldane developed 
mathematical models that built upon the new understanding of genetic 
(Mendelian) inheritance to predict changes in alleles frequencies in a 
population over time. 

These models are based on a number of important assumptions that describe 
an *idealized population*: a populatin in which allele frequencies will not 
change unless at least one of **five evolutionary processes** (below) are acting. 

- selection  
- mutation  
- recombination  
- genetic drift  
- migration (pop-structure and gene flow)

The unchanging state that exists when these processes are absent is 
called *Hardy Weinberg* equilibrium. Today we will focus on Mendel's 
rules of inheritance, the assumptions of the mathematical models of 
the Modern Synthesis, and how together these define how these five 
processes cause evolution.

<!-- , and how the importance of these five main evolutionary
processes is defined on the basis that they represent violations of the 
simple assumptions of these model.
 -->

### Genetics Terms
First, let's review some (challenging) genetics terms. Thus far, we have used
terms like *locus, allele, gene, gene copy, genotype, haplotype, and genome,*
but we haven't been very precise in our definitions of them. 
This is in part because some of these terms can be used in multiple ways, 
and also because their meanings have changed over time as they evolved from 
being abstract terms for talking about inherited material, to more precise 
definitions corresponding to physical DNA. 

**Discussion**: What are the limits that define a locus? What is the 
difference between a gene and locus. 

- Gene & Locus: The terms gene and locus are often used interchangeably to 
refer to a region of the genome.
- Gene: In the strict sense, genes have more definitive boundaries, referring
to regions of the genome that code for proteins, and which have defined
transcriptional start and end positions. 
- Locus: By contrast, a locus more often refers to an arbitrary region of 
a genome which may or may not contain one or more genes. 
<!-- - Gene & Locus: Their meanings have evolved with sequencing technologies,
fi rst referring to DNA, RNA, or proteins that could be isolated 
Later, with DNA sequencing, it often referred to the region that 
was targeted between sequencing primers. More recently, with increasing 
availability of genome data, it is used to refer to a non-recombined block 
of ancestry along a genome. -->
- Allele: A variant at a locus, gene, or site.
- Genotype: A combination of alleles at multiple loci (or entire genome).
Usually referring to a diploid genome, whereas a haploid genome will be 
referred to as a haplotype.
- Gene copy: One of a number of copies of a gene/locus in a population. For a 
population of N=1000 diploid individuals there are 2N gene copies. Many
evolutionary models are focused on how the genetic composition of these 2N
gene copies change over multiple generations as a way of tracking changes in
allele frequencies. One gene copy may leave more descendants (copies) to the
next generation than another (differential fitness) either due to selection 
or chance. The two gene copies of a diploid individual segregate with equal
probability into their many gametes.


### Measuring genetic diversity
How do we measure genetic diversity in theory and in practice? What do we 
mean by genetic diversity? Diversity at a single site, locus, or across the
whole genome? For whole genomes, should we average across sites, or across
loci or genomic windows? Do we expect genetic diversity to vary spatially
along the genome? Why?

To quantify diversity at a single locus requires us to first define the 
boundaries of the locus. This is usually done with respect to (1) gene or 
exon/intron boundaries; or (2) the positions of primers designed to target
a region; or (3) with respect to estimated recombination break points; or
(4) using an arbitrary window size.

How do we count how many alleles are in a population at a given locus? 


### Mendel's Rules of Inheritance

<img src="https://ib.bioninja.com.au/_Media/meiosis-and-mendel_med.jpeg">



### Gene mixing by segregation
**Segregation** is the transmission (copying) of one of the two copies of a
locus to a gamete during meiosis. A diploid organism usually makes many 
thousands or millions of gametes. Mendel identified that the two copies of
a locus have equal probability of being inherited by any gamete.

Hardy-Weinberg equilibrium calculates the expected frequencies of 
diploid genotypes in an idealized population. Allele frequencies do not
change (given the idealized population assumptions) but genotype frequencies
can change if the population is not already in equilibrium. After just one
generation the population will reach HW equilibrium by segregation of 
alleles and random rejoining into genotypes.


### Gene mixing by recombination

**Recombination** refers to the joining together of alleles from two or more
different loci into the same genome, such as a copy inherited from one parent
at locus A with a copy inherited from a different parent at locus B. Recombination
occurs between loci on different chromosomes through the independent assortment
of those chromosomes (equal probability of chromosomes copies pairing 
during meiosis). Recombination between loci on the same chromosome occurs by
crossing over, which brings gene copies previously on different chromosomes 
together onto the same chromosome.


#### Independent assortment
<img src="https://ib.bioninja.com.au/_Media/random-gene-assortment_med.jpeg"  style="width: 80%; text-align: center; border: solid">

#### Crossing over
<img src="https://ib.bioninja.com.au/_Media/chiasmata_med.jpeg" style="width: 80%; text-align: center; border: solid">


### Linkage Disequilibrium
LD is a statistical association between alleles at two different loci. For 
example, locus A has alleles A1 and A2, and locus B has alleles B1 and B2. 
If we always find A1 together with B1, and A2 together with B2, but never
observe the other two combinations, then loci A and B are in linkage
disequilibrium. 

LD is a property of a population and can arise for multiple reasons. One 
reason is physical linkage, which means that the two loci are very close
together on a chromosome. Because they are close, recombination does not
occur between them very often, and so mutations at either locus are usually
co-inherited together. A second reason is selection caused by **epistasis**
(phenotype depends on the interaction among loci).  
If the two alleles provide a fitness benefit, or deficit, when they are 
together versus separate, then a history of selection can give rise to a statistical correlation between two loci, even if they are on 
different chromosomes (not physically linked). A third reason if population
structure. Alleles at two different loci can be in LD because they were 
co-inherited together for many generations in the past, and only more recently
mixed through gene flow. 

If Mendelian inheritance is the only factor at work (i.e., not selection) then
recombination is expected to breakdown patterns of LD between loci over 
successive generations until they reach linkage equilibrium. This occurs faster
between loci with higher recombination rates, such as those on different 
chromosomes (r=0.5) compared to those that are physically linked (e.g., r=0.01).


### Mutation
- What happens when there is a new mutation at a locus, does that create a new allele? (Yes)
- Point mutations, structural variation.
- Mutation rates vary among organisms.
- Pleiotropy: mutation affects multiple traits.
- Synonymous mutations (those that do not change an amino acid) are neutral.
- Most non-synonymous mutations are deleterious. (Fig. 4.20)
- Mutation rates vary among different genomic regions, and in the types of 
changes that occur (e.g., transitions versus transversions).
- **Mutations occur randomly with respect to their impact on fitness.**



<!-- 
- So far, we have assumed that (genetic) variation exists in a population
and discussed how selection can act on phenotypic variation to cause changes in allele frequencies.
	- Chapter 5?: selection on a single locus.
	- Chapter 6?: quantitative genetic models (many loci of small effects).
	- We discussed adaptations. 
		- Often clearly observed in experiments / human impacts / nature
		- But cannot be assumed for every observed feature of organisms:
			- Spandrels, various ways in which features can evolve for non-adaptive reasons.

- One of your recent readings explored the origins of genetic variation 
(mutation and recombination).
	- Let's explore the history of this a bit...
		- A key concept of mutations is that they are *random*.
		- Classic experiment in evolution class, petri dish. Do not arise by need.
		- LTEE
		- Recent paper

	- Key concept of recombination is linkage (correlation).
		- linkage disequilibrium: "relationship is not random."
		- Example, correlation coefficient between alleles.
			- Classic experiment here at Columbia, discovery of chromosomes.
		- Hunt Morgan: In a paper published in Science in 1911, he concluded that (1) some traits were sex-linked, (2) the trait was probably carried on one of the sex chromosomes, and (3) other genes were probably carried on specific chromosomes as well. 


SKIPPED FOR NOW...
- Why recombination?
	- Breaks up associations between loci.
	- Figure from textbook.
	- Figure from textbook.
	- We will return to the topic/effects of recombination several times.

- Hardy Weinberg...

 
- Genetic Drift
	- Definition
	- Random walk analogy
	- Often the first assumption that we violate of the 5. It can provide the
	simplest explanation for evolution (change in allele frequencies).
		- Let's consider study of allele frequencies at a single locus in a single population:
			- selection (of interest)
			- mutation (rare compared to existing variation)
			- recombination (not relevant if we only care about 1 locus)
			- 
- Neutral Theory
 -->