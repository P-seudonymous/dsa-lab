import bisect

bst = list(map(int, input("Input tree: ").split()))


bst_sorted = bst.sort()


def search(key):
    i = bisect.bisect_left(bst, key)
    return i < len(bst) and bst[i] == key


def delete(key):
    i = bisect.bisect_left(bst, key)
    if i < len(bst) and bst[i] == key:
        bst.pop(i)
        print(f"Deleted {key}")
    else:
        print(f"{key} not found")


print("Inorder (sorted):", bst)

key = 50
if search(key):
    delete(key)
else:
    print("Not found")

print("After deletion:", bst)
