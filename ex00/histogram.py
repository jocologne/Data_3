import pandas as pd
import matplotlib.pyplot as plt

def plot_test():
    test = pd.read_csv("../Test_knight.csv")
    print("Available columns:")
    for i, col in enumerate(test.columns):
        print(f"{i}: {col}")
    choice = int(input("Select column to plot: "))
    col = test.columns[choice]
    
    if col in test.columns:
        plt.hist(test[col], bins=50)
        plt.title(f"{col}")
        plt.savefig("plot.png")
    else:
        print("Invalid column name")

def plot_train():
    train = pd.read_csv("../Train_knight.csv")
    jedi = train[train["knight"] == "Jedi"]
    sith = train[train["knight"] != "Jedi"]
    for i, col in enumerate(train.columns):
        print(f"{i}: {col}")
    choice = int(input("Select column to plot: "))
    col = train.columns[choice]
    if col in train.columns:
        plt.hist(jedi[col], bins=50, alpha=0.5, label="jedi", color="blue")
        plt.hist(sith[col], bins=50, alpha=0.5, label="sith", color="red")
        plt.title(f"{col}")
        plt.savefig("comp.png")
    else:
        print("Invalid column name")

def main():
    plot_test()
    plt.clf()
    plot_train()

if __name__ == "__main__":
    main()