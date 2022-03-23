lines_seen = set() # holds lines already seen
outfile = open("words.txt", "w")
for line in open("input.txt", "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()

#credit: https://stackoverflow.com/questions/1215208/how-might-i-remove-duplicate-lines-from-a-file