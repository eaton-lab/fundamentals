---
title: Ancestry
session: 9
module: 2
day2022: M/10/5/2022
---

# Ancestry

----

## Outline
- Lecture:
	- Review: Recombination and ancestry
	- Ancestry meaning more generally w/ examples.
	- Coalescent theory.
- Discussion: readings on ancestry
- Exercise:
	- notebooks 2-3
- Lecture
	- Extending to pop structure, phylogeny

----

## Read before class

- GCBias: [How much of your genome do you inherit from a particular grandparent?](https://gcbias.org/2013/10/20/how-much-of-your-genome-do-you-inherit-from-a-particular-grandparent/)
- GCBias: [How much of your genome do you inherit from a particular ancestor?](https://gcbias.org/2013/11/04/how-much-of-your-genome-do-you-inherit-from-a-particular-ancestor/)
- GCBias: [How lucky was the genetic investigation in the Golden State Killer case?](https://gcbias.org/2018/05/07/how-lucky-was-the-genetic-investigation-in-the-golden-state-killer-case/)
- https://www.amacad.org/publication/genetic-ancestry-testing-tribes-ethics-identity-health-implications

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

- [List of articles on ethics of using genetic genealogy for forensics](https://cruwys.blogspot.com/2018/04/gedmatch-ysearch-and-golden-state-killer.html)
- https://www.proquest.com/docview/207665908?parentSessionId=TFt0fRdCYes2z%2FPBp7XLAupQmo83dZ6eoiMupjdXjhk%3D
- https://www.amacad.org/publication/genetic-ancestry-testing-tribes-ethics-identity-health-implications
- ...
----

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
https://ib.bioninja.com.au/_Media/meiosis-and-mendel_med.jpeg

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
https://ib.bioninja.com.au/_Media/random-gene-assortment_med.jpeg

As homologous chromosomes align in synapsis non-sister chromatids may break 
and *recombine* with their homologous partner (crossing over).
https://ib.bioninja.com.au/_Media/chiasmata_med.jpeg

Recombination is a somewhat stochastic biological process. Although the 
average rate of recombination can be estimated based on studying thousands
of outcomes, recombination on a specific chromosome in a specific germline 
cell in a specific round of meiosis will always be different from the next.
Crossing-over may or may not happen (once or multiple more) on each 
chromosome, and its position will vary. Consequently, a gamete genome may
contain variable proportions of its two parental diploid genomes.

The analogy in your 2nd reading of a book is quite useful. 

	You have two copies of your 22 autosomal chromosomes, one you inherited from your biological mother and one from your father (we’ll ignore for the moment the small subset of our genomes that are inherited in a different manner, i.e., the mitochondria, and the Y chromosome, and the X chromosome). Your mother in turn had two copies of each of these chromosomes; one she received from your maternal grandfather and one from your maternal grandmother. Your mother can only pass on a single copy of each of these chromosome into the egg (through the process called meiosis). When she comes to pass on a particular chromosome, sometimes she transmits you a copy of your maternal grandmother’s chromosome, and sometimes she passes you a copy of your maternal grandfather’s chromosome. In those cases, your entire copy of that particular chromosome traces to either your maternal grandmother or your maternal grandfather. However, frequently when she copies out her chromosome she takes big chunks* from her mum’s copy and then switches to her dad’s copy. Imagine that each of these chromosomes are books — now you could have inherited page 1-253 from your maternal grandmother and 254-600 from your maternal grandfather. In that way, the copy of the chromosomal book you receive from your mother will be a mosaic of the copies in your maternal grandfather and grandmother. The mosaic you receive was bound together carefully so that you aren’t missing any pages and so you get the entire story (no annoying bits where you’re missing the page where the murderer isnrevealed). The process of forming the mosaic is called recombination, and the switch points in the story are called recombination events (or crossovers).

https://gcbias.files.wordpress.com/2017/12/parents_grandparents.png?w=768

### Reproduction and Genetic Inheritance
A diploid individual's genome may be replicated thousands, or even 
millions of times, through meiosis (e.g., production of sperm or eggs), 
but few of these gametes are likely to successfully mate to form a 
new diploid zygote. The newly formed diploid will have two copies at every 
gene, one inherited from its mother and one from its father. 

It is interesting, then, to look at each chromosome, to examine which 
gene copy in each region was sorted into this gamete, and which was not, 
during segregation and independent assortment in your mother and father's 
germline cells that formed the gametes that eventually created you.

In other words, at every gene, the sperm gamete could have carried one of
two possible copies that existed in your dad. And the egg gamete could have 
carried one of two possible copies that existed in your mom. Let's refer
to these as coming from your paternal side grandparents, or your maternal 
side grandparents. This was the topic of one of our readings for today:
https://gcbias.org/2013/10/20/how-much-of-your-genome-do-you-inherit-from-a-particular-grandparent/

"what is the probability that by chance your parent entirely failed to pass 
any autosomal DNA from a grandparent to you?" We can estimate this using some
simple probability calculations.

#### Independent assortment alone
Let's first assume no recombination and ask how likely this would be 
from the simple process of independent assortment. Let's focus on the 
probability that we inherit no DNA from our Mom's Mom. 
- We have two copies of each of our 22 chromosome (we are diploid).
- One copy of each chromosome comes from Mom, and one from Dad.
- In the absence of recomb., each copy from Mom could be the one she
inherited from her Dad or from her Mom.
- What is the probability we inherited *no* chromosomes from Mom's Mom 
(i.e., inherited only the other chromosome from Mom 22 times)?

- This is 1/2 * 1/2 * 1/2 * 1/2 ... (22 times total) == 0.5^22 = 2.35×10^(-7).

- In the article, they asked what is the probability "a grandparent"
fails to pass DNA to you, in which case we would multiply this by 2, 
because you could fail to inherit any DNA from either one of your Mom's
grandparents, or one of your Dad's grandparents.

-  2 x 0.5^22 = 4.7×10^(-7).

#### With recombination
The probability above is already quite low, however, it becomes much lower
when you add recombination, because now a greater proportion of your Mom
or Dad's chromosomes contains *some* DNA from both of their grandparents.

The calculations on GCBias include a number of interesting notes: Recombination
is more likely to occur on larger chromosomes. It occurs more often in women
than in men. The calculations show that the probability becomes much smaller
still.

https://gcbias.files.wordpress.com/2013/10/transmission_cartoon.png


### How much of your genome do you inherit from a particular ancestor?

#### Mitochondrial Eve
How much of your genetic material do you inherit from a particular ancestor? 
You inherit your mitochondria through your matrilineal lineage (your mum, 
your mum’s mum, your mum’s mum’s mum and so one). The mitochondria is 
*mostly* non-recombining. It thus provides a single large informative locus
that can be used to trace ancestry. 

There are fewer copies of mito genomes -- lower Ne -- and thus genetic 
drift occurs faster. This means a shorter time until you share a most 
recent common ancestor (same gene copy) with other humans.

- https://ib.bioninja.com.au/_Media/mtdna_med.jpeg
- https://en.wikipedia.org/wiki/Mitochondrial_Eve

#### Autosomes
But let's focus on the 22 autosomes for now, because we are interested in
the process by which recombination breaks up chromosomes into a mosaic of
different ancestors over time.

<!-- interpretation of this -->
https://gcbias.files.wordpress.com/2017/12/parents_grandparents.png?w=768

As we look at ancestors farther and farther back in time, we find that 
we have inherited less and less of their DNA. In this case we find an 
ancestor only 7 generations back that has contributed *NO DNA* to our 
genome! 
<!-- interpretation of this -->
https://gcbias.files.wordpress.com/2017/12/male_line.png

Whereas we computed earlier that this is very unlikely for a grandparent, 
it is not that unlikely for a great-great-great-great grandparent.
	
	"Despite being your genealogical ancestor, he is not your genetic 
	ancestor, none of their story has been passed down to you."


### Genetic versus genealogical ancestors
- https://gcbias.org/2013/11/11/how-does-your-number-of-genetic-ancestors-grow-back-over-time/
- https://gcbias.files.wordpress.com/2013/11/num_genetics_vs_genealogical_ancs.png
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

<!-- BREAK Maybe -->

### Review: modeling evolution
Under our simple definition of evolution as "changes in allele frequencies
in a population over time", we can model evolution as a result of at least
five simple processes. In an idealized population allele frequencies will
not change (will be in HW equilibrium). 

We next relaxed one assumption, making population size finite instead of 
infinite. This introduces a very realistic *random* process into our 
model of evolution: genetic drift results from the chance probability that
some gene copies are or are not replicated from one generation to the next.
The strength of genetic drift is measured as 1/2N (the number of gene copies
in a population). Drift is stronger in smaller populations.
<!-- - [show fluctuation plots] -->

This can be visualized in a WF model, where evolution over many generations
causes changes in allele frequencies. 

In addition, we can see that this process over multiple generations 
generates genealogies among gene copies.


### Genealogical ancestry
<!-- review exercise -->
In the case of Wright-Fisher model with finite population size. 
- yields genealogies of ancestor-descendant relationships.
- coalescent times can be predicted by Ne.
- these times (branch lengths) represent the opportunity over which 
mutations mutations can occur.
- Thus, we have a model where: Population model <-> genealogies <-> sequence variation.


### The coalescent
- Those WF simulations were pretty slow.
- We can do a MUCH faster approximation using probability alone, and model
assumptions.
- Kingman coalescent.

### Applications of the coalescent
- B/C relationships between pop Ne and sequence variation...
- Estimate effective population size from genetic data.
- We can simulate data under complex models:
	- migration between populations of different sizes
	- changing population sizes
	- divergences between populations (more on this later).

### Why so great?
The coalescent has proved so 
popular primarily because it gives a natural framework for analysing samples 
of DNA sequences and also because it allows efficient simulation, following 
samples of genes rather than the whole population. (Barton 2007)

We don't need to simulate whole genomes and populations.


### Population substructure
<!-- Rhode et al. -->
#### Empirical example
- expand from idea of mitochondrial eve

#### Species trees
- 



## Assigned for next class
- Futuyma textbook chapter 16
- Rosenberg "Multispecies coalescent"
- Notebooks:
	- Genealogies and coalescent
	- Species trees and ILS
	- Tree-thinking and newick
	- ...