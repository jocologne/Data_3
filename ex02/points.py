import pandas as pd
import matplotlib.pyplot as plt

def main():
    colors = {"Jedi": "blue", "Sith": "red"}
    data = pd.read_csv("../Train_knight.csv")
    plt.scatter(data["Empowered"], data["Prescience"], c = data["knight"].map(colors), alpha=0.5)
    plt.savefig("plot1.png")
    plt.clf()
    plt.scatter(data["Mass"], data["Friendship"], c = data["knight"].map(colors), alpha=0.5)
    plt.savefig("plot2.png")

if __name__ == "__main__":
    main()