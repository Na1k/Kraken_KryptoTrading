import sqlalchemy
import pandas as pd
import matplotlib.pyplot as plt

engine = sqlalchemy.create_engine('mysql+pymysql://root:root@localhost/kryptotrading?charset=utf8mb4')
df = pd.read_sql('SELECT * from etheur', engine)

plt = df.price.plot(figsize=(20, 16)).get_figure()
plt.savefig('ETHEUR-chart.png')