def dict(object,lst):
    #print(lst)
    k=object
    p=0
    for i in range(len(lst)):
        #t=k
        #print(k)
        if type(k) == str:
            print("No value is found")
            return
        if i not in object:
            print("Not in dictionary")
            continue
        k=k[lst[i]]
        p=1
    if p == 1:
        print(k)

object = {"x":{"y":{"z":"a"}}}
key = "a/b/c"
lst=key.split('/')
dict(object,lst)
