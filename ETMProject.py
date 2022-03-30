import argparse
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors
from statistics import median
from rich_dataframe import prettify
import seaborn as sns

# PARSER 

parser = argparse.ArgumentParser(description="a simple python script to visualize better, csv data")
parser.add_argument("criteria",type=str,help="argument to plot",choices=["earnings","project","algorithm","social","influence","chart"])
parser.add_argument("-v","--verbose",help="print some useful information",action="store_true")
parser.add_argument("-t","--table",help="visualize data with a nice table",action="store_true")
args = parser.parse_args()

df = pd.read_csv('Sondaggio cryptovalute.csv')
rows = df.shape[0]
cols = df.shape[1]
df = df.rename(columns={'Attualmente:':'Status','Quando acquisti delle cryptovalute, quanto è importante per te il possibile guadagno a breve-medio termine?':'Earnings',"Quando acquisti delle cryptovalute, quanto è importante per te la mission e vision del progetto che c'è dietro?":'Project',"Quando acquisti delle cryptovalute, quanto è importante l'algoritmo di consenso (ad esempio Proof of Work o Proof of Stake) che c'è dietro?":"Algorithm",'Valuta quanto sei d\'accordo con la seguente affermazione: "Prima di investire soldi in cryptovalute, preferisco informarmi con podcast,siti e social come Reddit,Telegram ecc."':'Social','Valuta quanto sei d\'accordo con la seguente affermazione: "Ho investito dei soldi in cryptovalute perché sono stato incuriosito da altri famosi influencer (ad esempio Elon Musk), che lo hanno fatto."':'Influence',"Siamo alla fine del sondaggio, come ultimo task vorrei chiederti di ordinare in ordine di importanza alcuni aspetti legati alle cryptovalute. N.B. 1 rappresenta quello più importante per te, mentre 5 quello meno importante. [1]":"chart1","Siamo alla fine del sondaggio, come ultimo task vorrei chiederti di ordinare in ordine di importanza alcuni aspetti legati alle cryptovalute. N.B. 1 rappresenta quello più importante per te, mentre 5 quello meno importante. [2]":"chart2","Siamo alla fine del sondaggio, come ultimo task vorrei chiederti di ordinare in ordine di importanza alcuni aspetti legati alle cryptovalute. N.B. 1 rappresenta quello più importante per te, mentre 5 quello meno importante. [3]":"chart3","Siamo alla fine del sondaggio, come ultimo task vorrei chiederti di ordinare in ordine di importanza alcuni aspetti legati alle cryptovalute. N.B. 1 rappresenta quello più importante per te, mentre 5 quello meno importante. [4]":"chart4","Siamo alla fine del sondaggio, come ultimo task vorrei chiederti di ordinare in ordine di importanza alcuni aspetti legati alle cryptovalute. N.B. 1 rappresenta quello più importante per te, mentre 5 quello meno importante. [5]":"chart5"})

# FILTERING DATASET

df_students = df.loc[df['Status'] == 'Studio']
df_workers = df.loc[df['Status'] == 'Lavoro']
df_both = df.loc[df['Status'] == 'Entrambe']
df_neither = df.loc[df['Status'] == 'Nessuna delle due']

# SHOWING THE DATA

if args.table:
    table = prettify(df,row_limit=100,col_limit=20)
    print(table)

def show_earnings():
    mean = df["Earnings"].mean()
    median = df["Earnings"].median()
    if args.verbose:    
        print(df.describe())
        print(df.groupby(['Earnings']).size())
        print(df_students.groupby(['Earnings']).size())
        print(df_workers.groupby(['Earnings']).size())
        print(df_both.groupby(['Earnings']).size())
    sns.displot(df, x="Earnings",bins=10,palette="rocket",hue="Status", multiple="dodge")
    sns.displot(df,x="Earnings")
    plt.axvline(x=mean,color='red')
    plt.axvline(x=median,color='blue')
    plt.show()

def show_project():
    mean = df["Project"].mean()
    median = df["Project"].median()
    if args.verbose:
        print(df.describe())
        print(df.groupby(['Project']).size())
        print(df_students.groupby(['Project']).size())
        print(df_workers.groupby(['Project']).size())
        print(df_both.groupby(['Project']).size())
    sns.displot(df, x="Project",bins=10,palette="rocket",hue="Status", multiple="dodge")
    sns.displot(df,x="Project")
    plt.axvline(x=mean,color='red')
    plt.axvline(x=median,color='blue')
    plt.show()

def show_algorithm():
    mean = df["Algorithm"].mean()
    median = df["Algorithm"].median()
    if args.verbose:
        print(df.describe())
        print(df.groupby(['Algorithm']).size())
        print(df_students.groupby(['Algorithm']).size())
        print(df_workers.groupby(['Algorithm']).size())
        print(df_both.groupby(['Algorithm']).size())
    sns.displot(df, x="Algorithm",bins=10,palette="rocket",hue="Status", multiple="dodge")
    sns.displot(df,x="Algorithm")
    plt.axvline(x=mean,color='red')
    plt.axvline(x=median,color='blue')
    plt.show()

def show_social():
    mean = df["Social"].mean()
    median = df["Social"].median()
    if args.verbose:
        print(df.describe())
        print(df.groupby(['Social']).size())
        print(df_students.groupby(['Social']).size())
        print(df_workers.groupby(['Social']).size())
        print(df_both.groupby(['Social']).size())
    sns.displot(df, x="Social",bins=10,palette="rocket",hue="Status", multiple="dodge")
    sns.displot(df,x="Social")
    plt.axvline(x=mean,color='red')
    plt.axvline(x=median,color='blue')
    plt.show()

def show_influence():
    mean = df["Influence"].mean()
    median = df["Influence"].median()
    if args.verbose:
        print(df.describe())
        print(df.groupby(['Influence']).size())
        print(df_students.groupby(['Influence']).size())
        print(df_workers.groupby(['Influence']).size())
        print(df_both.groupby(['Influence']).size())
    sns.displot(df, x="Influence",bins=10,palette="rocket",hue="Status", multiple="dodge")
    sns.displot(df,x="Influence")
    plt.axvline(x=mean,color='red')
    plt.axvline(x=median,color='blue')
    plt.show()


 
match args.criteria:
    case 'earnings':
        show_earnings()
    case 'project':
        show_project()
    case 'algorithm':
        show_algorithm()
    case 'social':
        show_social()
    case 'influence':
        show_influence()
    case 'chart':
        for i in range(1,6):
            print("--- " + str(i) + "th PLACE ---")
            print("-------------------")
            print("\n")
            print("--- GENERAL ---")
            print("-------------------")
            print(df.groupby(['chart' + str(i)]).size())
            print("\n")
            print("--- STUDENTS ---")
            print("-------------------")
            print(df_students.groupby(['chart' + str(i)]).size())
            print("\n")
            print("--- WORKERS ---")
            print("-------------------")
            print(df_workers.groupby(['chart' + str(i)]).size())
            print("\n")
            print("--- BOTH ---")
            print("-------------------")
            print(df_both.groupby(['chart' + str(i)]).size())
            print("\n")
            
        