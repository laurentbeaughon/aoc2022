from utils import read_pair_lists_characters


def is_right_order(list1, list2, index=0):
    min_length = min(len(list1), len(list2))
    copy_list1 = list1.copy()
    copy_list2 = list2.copy()
    while index < min_length:
        val_one, val_two = copy_list1[index], copy_list2[index]
        if val_one == val_two:
            index += 1
            if index == min_length:
                return len(copy_list1) < len(copy_list2)
        else:
            type1, type2 = type(val_one), type(val_two)
            if type1 != type2:
                if "]" in [val_one, val_two]:
                    return val_one == "]"  # list 1 must be the first to close
                if type1 == int:
                    copy_list1.insert(index, "[")
                    copy_list1.insert(index + 2, "]")
                elif type2 == int:
                    copy_list2.insert(index, "[")
                    copy_list2.insert(index + 2, "]")
            else:
                if type1 == int:
                    return val_one < val_two
                else:  # list 1 must be the first to close
                    return val_one == "]" and val_two == "["


def part_1(lists, verbose):
    output = 0
    for i in range(len(lists)):
        if is_right_order(lists[i][0], lists[i][1]):
            if verbose:
                print(f"pair {i + 1} is in the right order")
            output += i + 1
    return output


def part_2(lists, verbose):
    all_lists = sum(lists, []) + [["[", "[", 2, "]", "]"], ["[", "[", 6, "]", "]"]]
    sorted_lists = [all_lists[0]]
    for list in all_lists[1:]:
        for i, sorted_list in enumerate(sorted_lists):
            if is_right_order(list, sorted_list):
                sorted_lists.insert(i, list)
                break
        else:
            sorted_lists.append(list)
    return (sorted_lists.index(["[", "[", 2, "]", "]"]) + 1) * (
        sorted_lists.index(["[", "[", 6, "]", "]"]) + 1
    )


def main(args):
    lists = read_pair_lists_characters(args.data_file)
    print(part_1(lists, args.verbose))
    print(part_2(lists, args.verbose))
