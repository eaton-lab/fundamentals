---
title: Ancestry
module: 2
session: 9
day2022: M/10/5/2022
day2023: W/10/4/2023
---

# Ancestry and Coalescent

----


## Assignments due for this class (W: 10/4/2023)
- **Evolution 5th edition, Chapter 6** (Genetic drift and neutral theory)
- GCBias: [How much of your genome do you inherit from a particular grandparent?](https://gcbias.org/2013/10/20/how-much-of-your-genome-do-you-inherit-from-a-particular-grandparent/)
- complete Courseworks Quiz
- complete [interactive exercises 0, 1, **2**, and 6](https://pinky.eaton-lab.org) (Hardy-Weinberg Equilibrium)


## Assignments due for next class (M: 10/9/2023)
- **Evolution 5th edition, Chapter 16 ** (phylogeny)
- GCBias: https://gcbias.org/2017/12/19/1628/
<!-- - GCBias: https://gcbias.org/2013/11/11/how-does-your-number-of-genetic-ancestors-grow-back-over-time/ -->
- Complete Courseworks Quiz
- complete [interactive exercises 0, 1, 2, **3, 4, 5**, and 6](https://pinky.eaton-lab.org) (gene trees and species trees)
<!-- - https://www.amacad.org/publication/genetic-ancestry-testing-tribes-ethics-identity-health-implications -->

----

## Outline
<!-- 
- pass back the exam
- go over quiz for textbook ch. 6
- review questions about the exercise, and check who did it.
-->
- Review of WF and Neutral theory
<!-- continue lecture through neutral theory -->
- *Break*
- Genetic and Genealogical ancestry
- The Coalescent

----

## Slides

- [:material-presentation-play: *Link to Lecture Slideshow*: **Ancestry**](../lectures/ancestry-coalescent/)

----

## Lecture notes

### Genealogical versus Genetic Ancestry

Each chromosome represents a mosaic of segments inherited from different
ancestors, however, over many generation, many true ancestors may eventually 
contribute 0% of DNA to some of their descendant's genomes. How should this 
influence how we use "genetic ancestry" (DNA sequencing and statistics) to 
identify "genealogical ancestry" (who were the ancestors of a given person)?

<iframe width="560" height="315" src="https://www.youtube.com/embed/t9clljkF31Y?si=7mvqFFRiqxwwj6uT" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


### Discuss in lecture
- GCBias: [How lucky was the genetic investigation in the Golden State Killer case?](https://gcbias.org/2018/05/07/how-lucky-was-the-genetic-investigation-in-the-golden-state-killer-case/)



## Lecture notes


### Inheritance
Just as every individual organism is a descendant of an ancestor that lived
before it, so too, every copy of a gene that exists in a population (two 
copies for every diploid individual) is a descendant of an ancestral gene 
copy that came before it. Today we will focus on ancestor-descendant
relationships (genealogies). Specifically, the relationship between 
genealogies of diploid individuals, and genealogies of gene copies at
different parts of their genomes.

To start, let's revisit Mendel's rules of inheritance. The first two
are most relevant to use here. (1) there are two alleles at every locus
that segregate with equal probability into gametes. (2) when examining
alleles at two unlinked regions, alleles are sorted independently into
gametes. 
<!-- Mendel's rules of inheritance -->
<img src="https://ib.bioninja.com.au/_Media/meiosis-and-mendel_med.jpeg" style="width:60%">https://ib.bioninja.com.au/_Media/meiosis-and-mendel_med.jpeg</img>

### Meiosis and Recombination
Today we will also need to discuss linked parts of a genome (on the same
chromosome) and so we must understand a bit about meiosis and 
recombination.

Meiosis is the process by which a genome is duplicated (S phase),
creating 2 connected chromatids for each chromosome (thus 4 total copies of 
every gene). The two homologous chromosomes then separate (meiosis I) and
align (metaphase I), during which they can arrange into two equally 
probable arrangements (e.g., chr1-1 with chr2-1 or chr1-2 with chr2-1).
(This is independent assortment). 
<!--  -->
<img src="https://ib.bioninja.com.au/_Media/random-gene-assortment_med.jpeg" style="width:60%">https://ib.bioninja.com.au/_Media/random-gene-assortment_med.jpeg</img>

### Crossovers
As homologous chromosomes align in synapsis non-sister chromatids may break 
and *recombine* with their homologous partner
 <!-- (crossing over).https://ib.bioninja.com.au/_Media/chiasmata_med.jpeg -->

Recombination is a somewhat stochastic biological process. Although the 
average rate of recombination can be estimated based on studying thousands
of outcomes, recombination on a specific chromosome in a specific germline 
cell in a specific round of meiosis will always be different from the next.
Crossing-over may or may not happen (once or multiple times) on each 
chromosome, and its position will vary. Consequently, a gamete genome may
contain variable proportions of its two parental diploid genomes.

This analogy from the [GCBias blog](https://gcbias.files.wordpress.com/2017/12/parents_grandparents.png?w=768) is quite useful: "You have two copies of your 22 autosomal chromosomes, one you inherited from your biological mother and one from your father (we’ll ignore for the moment the small subset of our genomes that are inherited in a different manner, i.e., the mitochondria, and the Y chromosome, and the X chromosome). Your mother in turn had two copies of each of these chromosomes; one she received from your maternal grandfather and one from your maternal grandmother. Your mother can only pass on a single copy of each of these chromosome into the egg (through the process called meiosis). When she comes to pass on a particular chromosome, sometimes she transmits you a copy of your maternal grandmother’s chromosome, and sometimes she passes you a copy of your maternal grandfather’s chromosome. In those cases, your entire copy of that particular chromosome traces to either your maternal grandmother or your maternal grandfather. However, frequently when she copies out her chromosome she takes big chunks* from her mum’s copy and then switches to her dad’s copy. Imagine that each of these chromosomes are books — now you could have inherited page 1-253 from your maternal grandmother and 254-600 from your maternal grandfather. In that way, the copy of the chromosomal book you receive from your mother will be a mosaic of the copies in your maternal grandfather and grandmother. The mosaic you receive was bound together carefully so that you aren’t missing any pages and so you get the entire story (no annoying bits where you’re missing the page where the murderer isnrevealed). The process of forming the mosaic is called recombination, and the switch points in the story are called recombination events (or crossovers)."



### Reproduction and Genetic Inheritance
A diploid individual's genome may be replicated thousands, or even 
millions of times, through meiosis (e.g., production of sperm or eggs), 
but few of these gametes are likely to successfully mate to form a 
new diploid zygote. Of the zygotes that make up the next generation, each
is formed by two gametes, and thus inherits two copies at every 
gene, one inherited from its mother and one from its father.

It is interesting, then, to look across each chromosome and examine which 
gene copy was inherited from each of *their* parents (your grandparents)
at each genomic region. Each of your parents could only pass on one copy, 
and thus at each gene you did not inherit a copy from 2/4 of your grandparents.

In other words, at every gene, the sperm gamete could have carried one of
two possible copies that existed in your dad. And the egg gamete could have 
carried one of two possible copies that existed in your mom. Let's refer
to these as coming from your paternal side grandparents, or your maternal 
side grandparents. This was the topic of one of our readings for today:
[https://gcbias.org/2013/10/20/how-much-of-your-genome-do-you-inherit-from-a-particular-grandparent/](https://gcbias.org/2013/10/20/how-much-of-your-genome-do-you-inherit-from-a-particular-grandparent/)

"what is the probability that by chance your parent entirely failed to pass 
any autosomal DNA from a grandparent to you?" We can estimate this using some
simple probability calculations.

### How much of your genome do you inherit from a particular ancestor?
Using probability we can similarly compute an expectation for how much of
your genome is inherited from any given ancestor. For your two parents it
is 50%, and for each grandparent 25%, but this proportion becomes smaller and
smaller as the ancestor occurs farther and farther back in time. This is because
each generation you was a chance that their gene copy could not be inherited into
one of your ancestors. Recombination thus plays a very important role in the
concept of ancestry. It is because of this process that you inherit many small
bits of your genome from many many ancestors.

#### Mitochondrial Eve
The story is different in your mitochondrial genome because this genome occurs
separate from your nuclear genome, and is haploid, circular, and non-recombining.
Thus you inherit your mitochondrial genome as one entire unit through your matrilineal lineage (your mum, your mum’s mum, your mum’s mum’s mum and so one). 

There are fewer copies of mito genomes -- lower Ne -- and thus genetic 
drift occurs faster. This means a shorter time until you share a most 
recent common ancestor (same gene copy) with other humans. This makes 
mitochondrial DNA sequences a highly informative locus for phylogenetics and
phylogeography.
<img src="https://ib.bioninja.com.au/_Media/mtdna_med.jpeg">
- https://en.wikipedia.org/wiki/Mitochondrial_Eve

#### Autosomes
But let's focus on the 22 autosomes for now, because we are interested in
the process by which recombination breaks up chromosomes into a mosaic of
different ancestors over time.

<!-- interpretation of this -->
<img src="https://gcbias.files.wordpress.com/2017/12/parents_grandparents.png?w=768" style="width: 50%">
source: https://gcbias.files.wordpress.com/2017/12/parents_grandparents.png?w=768

As we look at ancestors farther and farther back in time, we find that 
we have inherited less and less of their DNA. In this case we find an 
ancestor only 7 generations back that has contributed *NO DNA* to our 
genome! 

<!-- interpretation of this -->
<img src="https://gcbias.files.wordpress.com/2017/12/male_line.png">
source: https://gcbias.files.wordpress.com/2017/12/male_line.png

Whereas we computed earlier that this is very unlikely for a grandparent, 
it is not that unlikely for a great-great-great-great grandparent. 
"Despite being your genealogical ancestor, he is not your genetic 
ancestor, none of their story has been passed down to you."


### Genetic versus genealogical ancestors
- <img src="https://gcbias.files.wordpress.com/2013/11/num_genetics_vs_genealogical_ancs.png">
source: https://gcbias.org/2013/11/11/how-does-your-number-of-genetic-ancestors-grow-back-over-time/
- Each generation back your number of ancestors double.
- Each generation we go back is expected to halve the amount of autosomal genetic material an ancestor gives to you.
- We only have to go back \~9 generations until it is quite likely that a specific ancestor contributed zero of your autosomal material to you.
- Your number of genealogical ancestors, in generation k, is growing exponentially; Your number of genetic ancestors eventually settles down to growing linearly back over the generations


### Ancestry databases
Genotyping of DNA a crime scenes of the Golden State Killer did not turn up
any hits in the CODIS database -- the largest DNA database used by US 
Law Enforcement, based on 13-20 microsatellite markers (short repeat loci).
This database is made up of samples collected by law enforcement through
enforced or coerced methods over many years. Although quite large, the 
amount of information pales in comparison to that available in *private*
DNA databases, collected by ancestry companies such as 23andme or 
ancestryDNA.

These private databases genotype samples at thousands of SNPs, thus providing
a more dense sampling of information across the genome. In addition, users 
volunteer their information to these databases, as opposed to being coerced,
and thus presence in the database is not associated with a prior criminal 
record or investigation, like in CODIS.

Police do not have access to these private databases, however, many users 
upload their SNP data to public websites that offer additional analyses 
not available on commercial sites. (Some of these additional analyses are 
not offered on the commercial sites for legal, ethical, or privacy reasons.)
Some of these third party sites, such as GEDmatch, save and share the data 
publicly.

Because you share genetic ancestry with your relatives, it is possible to 
identify you, and to make probabilistic guesses about your genotype, based
on the genetic information of your relatives. And this is true even for 
fairly distant relatives. Making your genome publicly available in some ways
exposes/violates the privacy of many of your relatives. Interestingly, this
was the case for the Golden State Killer, who was identified based on a 
partial match to one of his relatives in the public GEDmatch database.


<!-- BREAK Maybe -->

### Review: modeling evolution
Under our simple definition of evolution as "changes in allele frequencies
in a population over time", we can model evolution as a result of 
five simple processes (mutation, selection, genetic drift, gene flow, and 
recombination). In the absence of these processes (i.e., in an idealized 
population) allele frequencies do not change (they will be in HW equilibrium). 

We first relaxed one assumption of the HW model by making population size
finite instead of infinite. This introduces a *random* process in the form of genetic drift, which arises from the chance probability that some gene copies
are or are not replicated from one generation to the next. The strength of
genetic drift is measured as 1/N; it is stronger in smaller populations.

Genetic drift can be visualized in a WF model (see notebooks), where 
evolution over many generations causes changes in allele frequencies.
Eventually, genetic drift leads to fixation or loss of an allele, and thus 
always to a loss of genetic diversity. 

By selecting several samples at the end of a WF simulation, we can trace back
the history connecting their ancestors to create a genealogical tree. This 
genealogy of gene copies contains *coalescence events*, when viewed backwards
in time, which represent two gene copies merging into a common ancestor. 


### Genealogical ancestry
<!-- review exercise -->
In the case of Wright-Fisher model with finite population size, the WF model:

- yields genealogies of ancestor-descendant relationships.  
- coalescent times can be predicted by Ne.
- these times (branch lengths) represent the opportunity over which 
mutations mutations can occur.
- Thus, we have a model where: Population model <-> genealogies <-> sequence variation.


### The coalescent
- WF simulations are very slow, we can instead approximate this same process MUCH faster by using probability statements alone which are derived from the same model assumptions.
- The Kingman coalescent calculates the expected time until the next coalescence event in a samples of k gene copies.
- Repeating this process from when there are k copies, to k-1, k-2, ... until the final 2 copies coalesce results in a series of waiting times between coalescent events. By randomly joining samples at each of these waiting times we can build a coalescent genealogy.
- This coalescent genealogy is a random variable -- a stochastic outcome that
*could* represent the history of a set of gene copies in a population of size
Ne. A different value of Ne would predict a coalescent genealogy with 
different average coalescent times.

### Applications of the coalescent
- Allows for fast simulations under evolutionary models.
- Can generate null expectations for genetic diversity and divergence of populations under different demographic model.
- Can derive probability statements for 

Estimate effective population sizes from genetic data.
- Model the 


----

## References

- [List of articles on ethics of using genetic genealogy for forensics](https://cruwys.blogspot.com/2018/04/gedmatch-ysearch-and-golden-state-killer.html)
- https://www.proquest.com/docview/207665908?parentSessionId=TFt0fRdCYes2z%2FPBp7XLAupQmo83dZ6eoiMupjdXjhk%3D
- https://www.amacad.org/publication/genetic-ancestry-testing-tribes-ethics-identity-health-implications
----	