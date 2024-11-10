from linked_list import LinkedList

# Question
# Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. If x is contained within the list the values of x only need
# to be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.
# EXAMPLE
# Input:3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
# Output:3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8


def partition_one_ll(ll: LinkedList, p: int) -> LinkedList:
    return True


def partition_two_ll(ll: LinkedList, p: int) -> LinkedList:
    return True


def test_lr_partition():
    partitioners = [partition_one_ll, partition_two_ll]
    for partition_func in partitioners:
        # book example
        ll = LinkedList([3, 5, 8, 5, 10, 2, 1])
        assert not is_partitioned(ll, x=5)
        ll = partition_func(ll, 5)
        assert is_partitioned(ll, x=5), f"{partition_func} did not partition {ll}"

        # random example
        ll = LinkedList.generate(10, 0, 99)
        x = ll.head.value
        ll = partition_func(ll, x)
        assert is_partitioned(ll, x=x), f"{partition_func} did not partition"


def is_partitioned(ll, x):
    seen_gt_partition = False
    for node in ll:
        if node.value >= x:
            seen_gt_partition = True
            continue
        if seen_gt_partition and node.value < x:
            return False
    return True


if __name__ == "__main__":
    test_lr_partition()
