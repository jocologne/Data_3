import pandas as pd
import matplotlib.pyplot as plt

def main():

    df = pd.read_csv("../Test_knight.csv")

    print("Available columns:")
    for i, col in enumerate(df.columns):
        print(f"{i}: {col}")
    choice = int(input("Select column to plot:"))
    col = df.columns[choice]

    if col in df.columns:
        plt.hist(df[col].dropna(), bins=50)
        plt.title(f"{col}")
        plt.savefig("plot.png")
    else:
        print("Invalid column name")

if __name__ == "__main__":
    main()