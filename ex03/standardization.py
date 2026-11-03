import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

def main():
    colors = {"Jedi": "blue", "Sith": "red"}
    data = pd.read_csv("../Train_knight.csv")
    cols = data.select_dtypes("number").columns
    scaler = StandardScaler()
    data[cols] = scaler.fit_transform(data[cols])
    plt.scatter(data["Empowered"], data["Prescience"], c = data["knight"].map(colors), alpha=0.5)
    plt.savefig("plot1.png")

if __name__ == "__main__":
    main()