# Create Glowing Bacteria

## A complementary strand

### Description
To give the bacteria new properties, we have to start by modifying the plasmid.

Typically, a bacterial plasmid looks like a huge four-letter text (A, T, C, G). It has a header denoted by the symbol ">", in which you can find a description of the organism and key information about the sequence. Everything else is the sequence itself.

>MK753227.1 Escherichia coli str. K-12, partial sequence
GACGTCTGTGCAAGTACTACTGTTCTGCAGTCACTTGAATTCGATACCCAGCTGTGTGCACTACCTCCTT
GGTTGTCTATGCTATGCTGATCTACAACTGGCATGCGGTCAGTGCGTCCTGCTGATGTGCTCAGTATCTC
TATCACTGATAGGGATGTCAATCTCTATCACTGATAGGGAAACGTTTCGCAGAAGCTTCCGCAAGGTACC
...
Now you are looking at a sequence of a bacterial plasmid. Alas, it's just a single strand (single DNA chain). Before modification, we need to create a second complementary strand. To get it, replace each element of the original sequence with its opposite according to the complementarity principle:

Adenine (A) <-> Thymine (T);
Cytosine (C) <-> Guanine (G).

For instance, if the sequence is TTAGCGCA your answer should be AATCGCGT.
![screen_grid](misc/images/cron1.png)


### Objectives
At this stage, you will create the complementary plasmid strand. Use only the first line of the plasmid sequence above. It looks as follows:

GACGTCTGTGCAAGTACTACTGTTCTGCAGTCACTTGAATTCGATACCCAGCTGTGTGCACTACCTCCTT
Input the sequence of the original strand;
Print the complementary strand as an answer.
Hint

### Example
The greater-than symbol followed by a space (> ) represents the console input.

> TTAGCGCA
AATCGCGT # the output starts here