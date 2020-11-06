#!/usr/bin/env python3

# this is a python script template
# this next line will download the file using curl

gff="Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.37.gff3.gz"
fasta="Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.dna.chromosome.Chromosome.fa.gz"

import os,gzip,itertools,csv,re

# this is code which will parse FASTA files
# define what a header looks like in FASTA format
def isheader(line):
    return line[0] == '>'

def aspairs(f):
    seq_id = ''
    sequence = ''
    for header,group in itertools.groupby(f, isheader):
        if header:
            line = next(group)
            seq_id = line[1:].split()[0]
        else:
            sequence = ''.join(line.strip() for line in group)
            yield seq_id, sequence



if not os.path.exists(gff):
    os.system("curl -O ftp://ftp.ensemblgenomes.org/pub/bacteria/release-45/gff3/bacteria_0_collection/escherichia_coli_str_k_12_substr_mg1655/Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.37.gff3.gz")

if not os.path.exists(fasta):
    os.system("curl -O ftp://ftp.ensemblgenomes.org/pub/bacteria/release-45/fasta/bacteria_0_collection/escherichia_coli_str_k_12_substr_mg1655/dna/Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.dna.chromosome.Chromosome.fa.gz")
    
with gzip.open(gff,"rt") as fh:
    # now add code to process this
    gff = csv.reader(fh,delimiter="\t")
    for row in gff:
        if row[0].startswith("#"):
            continue
        print(row[3],row[6])
	  

# part 2 and 3 of q2
gene_count = 0
total_gene_length=0
CDS_count=0
total_CDS_length
if row[2] == "gene": 
    gene_count += 1
    total_gene_length += (int(row[4] - int(row[3])

# part 5 of q2, finding rows whose second columns is CDS:

if row[2] == "CDS":
    CDS_count += 1
    total_CDS_length += (int(row[4] - int(row[3]))

print(gene_count)
print(total_gene_length)
print(total_CDS_length)


		    
		  
# for part 4 of the question starting over from template related to this part of the question
		    
import os,gzip,itertools,csv,re
def isheader(line):
    return line[0] == '>'
def aspairs(f):
    seq_id = ''
    sequence = ''
    for header,group in itertools.groupby(f, isheader):
        if header:
            line= = next(group)
	    seq_id = line[1:].split()[0]
        else:
            sequence = ''.join(line.strip() for line in group)
            yield seq_id, sequence
if not os.path.exists(fasta):
    os.system("curl -O ftp://ftp.ensemblgenomes.org/pub/bacteria/release-45/fasta/bacteria_0_collection/escherichia_coli_str_k_12_substr_mg1655/dna/Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.dna.chromosome.Chromosome.fa.gz")
with gzip.open(fasta, "rt") as f:
    pairs= aspairs(f)
    sequencess= dict(pairs)
    for seq_id in sequencess:
        bps= len(sequences[seq_id])
percentage=(total_gene_length/bps)*100

