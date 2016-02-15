import random

def selectCodon(x):
    if x == 'I':
        possibleCodons = ['ATT', 'ATC', 'ATA']
        return(random.choice(possibleCodons))
    if x == 'L':
        possibleCodons = ['CTT', 'CTC', 'CTA', 'CTG', 'TTA', 'TTG']
        return(random.choice(possibleCodons))
    if x == 'V':
        possibleCodons = ['GTT', 'GTC', 'GTA', 'GTG']
        return(random.choice(possibleCodons))
    if x == 'F':
        possibleCodons = ['TTT', 'TTC']
        return(random.choice(possibleCodons))
    if x == 'M':
        possibleCodons = ['ATG']
        return(random.choice(possibleCodons))
    if x == 'C':
        possibleCodons = ['TGT', 'TGC']
        return(random.choice(possibleCodons))
    if x == 'A':
        possibleCodons = ['GCT', 'GCC', 'GCA', 'GCG']
        return(random.choice(possibleCodons))
    if x == 'G':
        possibleCodons = ['GGT', 'GGC', 'GGA', 'GGG']
        return(random.choice(possibleCodons))
    if x == 'P':
        possibleCodons = ['CCT', 'CCC', 'CCA', 'CCG']
        return(random.choice(possibleCodons))
    if x == 'T':
        possibleCodons = ['ACT', 'ACC', 'ACA', 'ACG']
        return(random.choice(possibleCodons))
    if x == 'S':
        possibleCodons = ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC']
        return(random.choice(possibleCodons))
    if x == 'Y':
        possibleCodons = ['TAT', 'TAC']
        return(random.choice(possibleCodons))
    if x == 'W':
        possibleCodons = ['TGG']
        return(random.choice(possibleCodons))
    if x == 'Q':
        possibleCodons = ['CAA', 'CAG']
        return(random.choice(possibleCodons))
    if x == 'N':
        possibleCodons = ['AAT', 'AAC']
        return(random.choice(possibleCodons))
    if x == 'H':
        possibleCodons = ['CAT', 'CAC']
        return(random.choice(possibleCodons))
    if x == 'E':
        possibleCodons = ['GAA', 'GAG']
        return(random.choice(possibleCodons))
    if x == 'D':
        possibleCodons = ['GAT', 'GAC']
        return(random.choice(possibleCodons))
    if x == 'K':
        possibleCodons = ['AAA', 'AAG']
        return(random.choice(possibleCodons))
    if x == 'R':
        possibleCodons = ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG']
        return(random.choice(possibleCodons))
    
def breakAminoAcid():
    AminoAcid = input('''Type your string of amino acids and hit enter.
All capital letters and no spaces.''')
    for y in range (len(AminoAcid)):
        print(selectCodon(AminoAcid[y]))

print(breakAminoAcid())
