s="this is so cool (234) test (123)"
for i in s.split(")"):
    if "(" in i:
       print (i.split("(")[-1])
