from sys import argv, exit

# provided
#
# Read integers from the given filename.
#
# Return value: list of integers
def read_array(filename):
    try:
        with open(filename) as f:
            return [int(n) for n in f.read().split()]
    except:
        exit("Couldn’t read numbers from file \""+filename+"\"")


# implement
#
# Return the number of inversions in the given list, by doing a merge
# sort and counting the inversions.
#
# Return value: number of inversions
def count_inversions(in_list):
    if len(in_list) <= 1:
        return 0
    middle = len(in_list)//2
    l_list = [in_list.pop(0) for i in range(middle)]
    r_list = [in_list.pop(0) for j in range(len(in_list))]
    r_a = count_inversions(l_list)
    r_b = count_inversions(r_list)
    r_m = merge_i(l_list,r_list,in_list)
    return r_a + r_b + r_m


# implement
#
# Merge the left & right lists into in_list.  in_list already contains
# values--replace those with the merged values.
#
# Return value: inversion count
def merge_i(l_list, r_list, in_list):
    count = 0
    while l_list and r_list:
        if r_list[0] < l_list[0]:
            in_list.append(r_list.pop(0))
            count += len(l_list)
        else:
            in_list.append(l_list.pop(0))
    if l_list:
        while l_list:
            in_list.append(l_list.pop(0))
    if r_list:
        while r_list:
            in_list.append(r_list.pop(0))
    return count


# provided
if __name__ == '__main__':
    if len(argv) != 2:
        exit("usage: python3 "+argv[0]+" datafile")
    in_list = read_array(argv[1])
    print(count_inversions(in_list))
