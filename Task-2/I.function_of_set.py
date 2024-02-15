set1={""}
set2={""}
concat={''}
def concat_sets(set1,set2):
    for x in set1:
        if x in set2:
            concat.add(x)
    concat.pop()#to delete the first element 
    print(concat)

concat_sets({1,8,9,"apple","cat"}  ,  {9,"cat","ok"})
