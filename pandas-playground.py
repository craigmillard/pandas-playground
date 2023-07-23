import pandas

def main():

    #get csv as data frame
    original = pandas.read_csv(f"data-sources/original.csv", header=0)
    changed = pandas.read_csv(f"data-sources/changed.csv")
    compared = original.compare(changed)
    compared.columns = compared.columns.get_level_values(0)
    original = compared.loc[:,~compared.columns.duplicated()]
    new = compared.loc[:,~compared.columns.duplicated(keep='last')]
    print(compared.columns.get_level_values(0).unique())

if __name__ == "__main__":
    main()