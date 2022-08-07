def output_bacteria() -> None:
    """This function print """
    user_output = input()
    nitrogenous_bases = {
    "A": "T",
    "C": "G",
    "T": "A",
    "G": "C"
}
    print(user_output)
    print("".join(nitrogenous_bases[gene] for gene in user_output))


def cut_bacteria() -> None:
    """This function cut and print """
    line, line_1 = input().split()
    print(line.replace("CTGCAG", "C TGCAG"))
    print(line_1.replace("GACGTC", "GACGT C"))



if __name__ == "__main__":
    output_bacteria()
    
