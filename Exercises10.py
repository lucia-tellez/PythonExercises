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

#EXERCISE 3: Find the EcoRI cutting motif and give the length of the second half

EcoDNA = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
EcoDNA.find("GAATTC")
SecondHalf = str(EcoDNA[21+1:])
len(SecondHalf)

##EXERCISE 4: Extract the exons from a sequence
GenomicDNA = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

FirstExon = GenomicDNA[:61]

SecondExon = GenomicDNA[90:]
CodingSequence = FirstExon + SecondExon
CodingPercentage = (len(CodingSequence)/len(GenomicDNA))*100
print("The percentage of coding sequence in this DNA fragment is of", CodingPercentage)

#Print the original genomic sequence with introns in lowercase
Intron = GenomicDNA[61:89]
IntronLC = Intron.lower()
SequenceEX4 = FirstExon + IntronLC + SecondExon
