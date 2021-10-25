def merge(ori_lst, left, mid, right):
    L, R = [], []
    for i in range(left, mid):
        L.append(ori_lst[i])
    for i in range(mid, right):
        R.append(ori_lst[i])
    base = left
    while len(L) > 0 and len(R) > 0:
        if L[0] < R[0]:
            ori_lst[base] = L[0]
            L.remove(L[0])
        else:
            ori_lst[base] = R[0]
            R.remove(R[0])
        base += 1
    while len(L) > 0:
        ori_lst[base] = L[0]
        L.remove(L[0])
        base += 1
    while len(R) > 0:
        ori_lst[base] = R[0]
        R.remove(R[0])
        base += 1


def merge_sort(arr, left, right):
    if left + 1 >= right:
        return None
    mid = left + (right - left) // 2
    merge_sort(arr, left, mid)  # LEFT
    merge_sort(arr, mid, right)  # RIGHT
    merge(arr, left, mid, right)  # MERGE


def sort(arr):
    merge_sort(arr, 0, len(arr))
    return arr


def main():
    lst = []
    num = int(input().strip())
    for i in range(num):
        lst.append(int(input().strip()))

    print("UNSORTED -> ", lst)
    sort(lst)
    print("SORTED -> ", lst)


if __name__ == "__main__":
    main()
