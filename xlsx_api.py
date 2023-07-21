import pandas as pd

path = "C:/Users/KurzanovAV/Documents/portfolio/"

def xlsx_deals_read():
    df = pd.read_excel(path + "deals.xlsx", usecols="B:F,H:L,O:Q")
    df.columns = [
        "num_trade",
        "dt_deal",
        "dt_settle",
        "secid",
        "sec_type",
        "oper_type",
        "volume",
        "price",
        "acc_int",
        "amount",
        "comis_ts",
        "comis_bank",
        "amount_inout"
    ]

    return df

df = xlsx_deals_read()
df[df["oper_type"] == "Продажа", "volume"] = df[df["oper_type"] == "Продажа", "volume"] * (-1)
df['volume'] = df.apply(lambda x: 30 if x['TIME'][:2]=='02' else x['VALUE'], axis='columns')
print(df)


