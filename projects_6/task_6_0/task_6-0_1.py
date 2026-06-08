import pandas as pd
df = pd.read_csv("C:/Users/user/Desktop/wild_boars.csv")
print(df['tusk_length_cm'])
min_tusk = df['tusk_length_cm'].min()
max_tusk = df['tusk_length_cm'].max()
print(f"самый короткий клык: {min_tusk:.2f} см")
print(f"самый длинный клык: {max_tusk:.2f} см")
