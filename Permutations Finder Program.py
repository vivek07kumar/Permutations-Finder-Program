def permute(prefix,suffix) :
    suffix_size = len(suffix)
    if suffix_size == 0 :
        print(prefix)
    else :
        for i in range(0,suffix_size) :
            new_pre = prefix + [suffix[i]]
            new_suff = suffix[:i] + suffix[i+1:]
            permute(new_pre,new_suff)
def main() :
    a = list(eval(input('>> Please enter Numbers/Strings seperated by comma : ')))
    permute([],a)
main()
