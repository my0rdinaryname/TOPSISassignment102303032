import pandas as pd
import sys
from topsis_102303032 import topsis

print("Program started successfully")

def main():
    arguments = sys.argv[1:]
    if len(arguments) != 3:
        print("Error: Expected 3 arguments -> filename, weights, impacts")
        sys.exit(1)

    filename = sys.argv[1]
    assert filename, "Filename must be provided"
    if not filename.endswith(".csv"):
        print("Error: Input file must be a CSV")
        sys.exit(1)

        
    dataframe = pd.read_csv(filename,header=0)
    name = dataframe.iloc[:,0]
    data = dataframe.iloc[:,1:]
    weights = sys.argv[2].split(',')
    impacts = sys.argv[3]
    if len(impacts) != len(weights):
        print("Error: Number of impacts must match number of weights")
        sys.exit(1)

    
    output = topsis(data,weights,impacts)
    data["Topsis Score"] = output["Score"].values
    data["Rank"] = output["Rank"].values
    data.to_csv("output-result.csv", index=False)
    print("Output file saved as output-result.csv")

    ranks = output.iloc[:,-1]
    max_index = ranks.idxmin()
    
    print("\n|| The best alternative is {} ||\n".format(name[max_index-1]))
    print("The breakdown of scores and ranks is:\n=====================================================================================\n")
    print(output)
    
if __name__ == "__main__":
    main()
