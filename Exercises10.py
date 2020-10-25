#!/usr/bin/env python3

##EXERCISE 1: Calculate AT content of a DNA sequence

shortDNA = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

A = shortDNA.count("A")
T = shortDNA.count("T")
ATcontent = (A + T) / len(shortDNA)
print("The AT content of the DNA sequence is", ATcontent)

##EXERCISE 2: Write the reverse complement of a DNA sequence

reverseseq = shortDNA.replace("A", "t").replace("T","A").replace("G", "c").replace("C", "G")

reverseseq.upper()

