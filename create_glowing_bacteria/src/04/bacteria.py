def complementary(original):
    principle = {"A": "T", "T": "A", "C": "G", "G": "C"}
    result = ""
    for c in original:
        result += principle[c]
    return result


def restriction(gfp, l_site, r_site, cut):
    return gfp[gfp.index(l_site) + cut:gfp.rindex(r_site) + cut]


def main():
    gfp = input()
    l_site, r_site = input().split()
    print(restriction(gfp, l_site, r_site, 1))
    print(complementary(restriction(gfp, l_site, r_site, 5)))

if __name__ == "__main__":
    main()

