import pandas as pd
from scipy.stats import pointbiserialr

def main():
    res = {}
    file = pd.read_csv("../Train_knight.csv")
    file["knight"] = file["knight"].map({"Jedi": 1, "Sith": 0})
    for col in file.columns:
        cor, pv = pointbiserialr(file["knight"], file[col])
        res[col] = {"correlation": cor, "p_value": pv}
    res = dict(sorted(res.items(), key=lambda item: abs(item[1]["correlation"]), reverse=True))
    for key, value in res.items():
        print(f"{key}: {value['correlation']:.4f},    {value['p_value']:.4e}")

if __name__ == "__main__":
    main()