

def output_bacteria() -> None:
    """This function print """
    user_output = input()
    nitrogenous_bases = {
    "A": "T",
    "C": "G",
    "T": "A",
    "G": "C"
}
    print("".join(nitrogenous_bases[gene] for gene in user_output))

if __name__ == "__main__":
    output_bacteria()
        
