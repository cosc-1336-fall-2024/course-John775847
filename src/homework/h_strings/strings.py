

def get_hamming_distance(dna1, dna2):
    output = 0

    if (len(dna1) == len(dna2)):
        for i in range(len(dna1)):
            if (dna1[i] != dna2[i]):
                output += 1
                i+=1
            else:
                i+=1
    else:
        return "error, missmatch strings"

    return output

def get_dna_complement(dna):
    flip = ""
    swip = ""

    for i in range(len(dna)):
        flip += dna[len(dna) - (i+1)]

    for i in range(len(dna)):
        if (flip[i] == "A"):
            swip += "T"
            i+=1
        elif (flip[i] == "T"):
            swip += "A"
            i+=1
        elif (flip[i] == "C"):
            swip += "G"
            i+=1
        elif (flip[i] == "G"):
            swip += "C"
            i+=1
        else:
            swip += flip[i]

    return swip

def idk():
    return "idk"
