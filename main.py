alphanumeric = "abcdefghijklmnopqrstuvwxyz"

reverseCouple = [["a","z"], ["b","y"], ["c","x"], 
                 ["d","w"], ["e","v"], ["f","u"], 
                 ["g","t"], ["h","s"], ["i","r"], 
                 ["j","q"], ["k","p"], ["l","o"], 
                 ["m","n"], ["n","m"], ["o","l"], 
                 ["p","k"], ["q","j"], ["r","i"], 
                 ["s","h"], ["t","g"], ["u","f"], 
                 ["v","e"], ["w","d"], ["x","c"], 
                 ["y","b"], ["z","a"]]

geneDict = {
    0 : "A",
    1 : "C",
    2 : "G",
    3 : "T"
}

nucleotidePairs = {
    "A" : "T",
    "C" : "G",
    "G" : "C",
    "T" : "A"
}

def encode(message):
    encoded = ""
    cypher = ""
    print(message)

    #Substituting each character for their couple in the reverse couple
    #end var = cypher
    for letter in message:
        for couple in reverseCouple:
            if letter == couple[0]:
                cypher += couple[1]

    print(cypher)

    #each letter is switched to binary form and split into pairs, these pairs are translated to
    #integers and a corresponding nucleotide is assigned, then the pair is found creating the cypher
    #end var = dnaSeq
    dnaSeq = ""
    for char in cypher:
        char_bin = format(ord(char), '08b')
        #format 01110011
        for x in range(0, len(char_bin), 2):
            dnaSeq += nucleotidePairs[geneDict[int(char_bin[x:x+2], 2)]]
    
    #print(dnaSeq)
    encoded = dnaSeq
    return encoded

def decode(encryptedMessage):
    print(encryptedMessage)

print(encode("The visitor entered at a time not listed on any clock. Under the heel of his boot, the dust shifted just slightly, as though remembering something. Nothing on the walls made sense — not the crooked map, not the mirror that reflected nothing but heat. Keyholes outnumbered doors, but none were shaped alike. Every footprint he didn’t leave led somewhere. Yesterday was printed beneath the rug. Or maybe the word was “Yet.” Usually the light flickered twice, then once, then three times. Silence answered first. He smiled. He was always fond of games."))