import argparse
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors
from statistics import median
from rich_dataframe import prettify
import seaborn as sns

# PARSER

parser = argparse.ArgumentParser(
    description="a simple python script to visualize better, csv data")
parser.add_argument("criteria", type=str, help="argument to plot", choices=[
                    "earnings", "project", "algorithm", "social", "influence", "chart", "save-all"])
parser.add_argument("-v", "--verbose",
                    help="print some useful information", action="store_true")
parser.add_argument(
    "-t", "--table", help="visualize data with a nice table", action="store_true")
parser.add_argument(
    "-s", "--save", help="save plot in 'plots' folder", action="store_true")
args = parser.parse_args()

df = pd.read_csv('Sondaggio cryptovalute.csv')
rows = df.shape[0]
cols = df.shape[1]
df = df.rename(columns={'Attualmente:': 'Status', 'Quando acquisti delle cryptovalute, quanto è importante per te il possibile guadagno a breve-medio termine?': 'Earnings', "Quando acquisti delle cryptovalute, quanto è importante per te la mission e vision del progetto che c'è dietro?": 'Project', "Quando acquisti delle cryptovalute, quanto è importante l'algoritmo di consenso (ad esempio Proof of Work o Proof of Stake) che c'è dietro?": "Algorithm", 'Valuta quanto sei d\'accordo con la seguente affermazione: "Prima di investire soldi in cryptovalute, preferisco informarmi con podcast,siti e social come Reddit,Telegram ecc."': 'Social', 'Valuta quanto sei d\'accordo con la seguente affermazione: "Ho investito dei soldi in cryptovalute perché sono stato incuriosito da altri famosi influencer (ad esempio Elon Musk), che lo hanno fatto."': 'Influence',
               "Siamo alla fine del sondaggio, come ultimo task vorrei chiederti di ordinare in ordine di importanza alcuni aspetti legati alle cryptovalute. N.B. 1 rappresenta quello più importante per te, mentre 5 quello meno importante. [1]": "chart1", "Siamo alla fine del sondaggio, come ultimo task vorrei chiederti di ordinare in ordine di importanza alcuni aspetti legati alle cryptovalute. N.B. 1 rappresenta quello più importante per te, mentre 5 quello meno importante. [2]": "chart2", "Siamo alla fine del sondaggio, come ultimo task vorrei chiederti di ordinare in ordine di importanza alcuni aspetti legati alle cryptovalute. N.B. 1 rappresenta quello più importante per te, mentre 5 quello meno importante. [3]": "chart3", "Siamo alla fine del sondaggio, come ultimo task vorrei chiederti di ordinare in ordine di importanza alcuni aspetti legati alle cryptovalute. N.B. 1 rappresenta quello più importante per te, mentre 5 quello meno importante. [4]": "chart4", "Siamo alla fine del sondaggio, come ultimo task vorrei chiederti di ordinare in ordine di importanza alcuni aspetti legati alle cryptovalute. N.B. 1 rappresenta quello più importante per te, mentre 5 quello meno importante. [5]": "chart5"})

# FILTERING DATASET

df_students = df.loc[df['Status'] == 'Studio']
df_workers = df.loc[df['Status'] == 'Lavoro']
df_both = df.loc[df['Status'] == 'Entrambe']
df_neither = df.loc[df['Status'] == 'Nessuna delle due']
df_chart = df[["chart1", "chart2", "chart3", "chart4", "chart5"]]


# SHOWING THE DATA

if args.table:
    table = prettify(df, row_limit=100, col_limit=20)
    print(table)


def describe_dataset():
    print(df.describe())
    print(df_students.describe())
    print(df_workers.describe())
    print(df_both.describe())


def get_dataset_size(criteria):
    print(df.groupby([criteria]).size())
    print(df_students.groupby([criteria]).size())
    print(df_workers.groupby([criteria]).size())
    print(df_both.groupby([criteria]).size())


def save_plot(criteria, category):
    plt.savefig('plots/' + criteria + category + '.png')


def save_all(criteria):
    if args.verbose:
        describe_dataset()
    for i in criteria:
        mean = df[i].mean()
        median = df[i].median()
        #print("mean: " + str(mean) + ", median: " + str(median))
        if args.verbose:
            get_dataset_size(i)
        sns.displot(df, x=i, bins=10, palette="rocket",
                    hue="Status", multiple="dodge")
        save_plot(i.lower(), "_specific")
        sns.displot(df, x=i)
        plt.axvline(x=mean, color='red')
        plt.axvline(x=median, color='blue')
        save_plot(i.lower(), "_general")


def plot_data(criteria):
    mean = df[criteria].mean()
    median = df[criteria].median()
    if args.verbose:
        describe_dataset()
        get_dataset_size(criteria)
    sns.displot(df, x=criteria, bins=10, palette="rocket",
                hue="Status", multiple="dodge")
    if args.save:
        save_plot(criteria.lower(), "_specific")
    sns.displot(df, x=criteria)
    plt.axvline(x=mean, color='red')
    plt.axvline(x=median, color='blue')
    if args.save:
        save_plot(criteria.lower(), "_general")
    plt.show()


match args.criteria:
    case 'earnings':
        plot_data("Earnings")
    case 'project':
        plot_data("Project")
    case 'algorithm':
        plot_data("Algorithm")
    case 'social':
        plot_data("Social")
    case 'influence':
        plot_data("Influence")
    case 'chart':
        total = 0
        for i in range(1, 6):
            print("--- " + str(i) + "th PLACE ---" + "\n" + "------------------- \n"
                  + "--- GENERAL --- \n" + "-------------------")
            print(df.groupby(['chart' + str(i)]).size())
            try:
                a = df.groupby(['chart' + str(i)]).size() * (6 - i)
                a["Redditività"]
            except KeyError:
                a["Redditività"] = 0
            total += a
            print("--- " + str(i) + "th PLACE ---" + "\n" + "------------------- \n"
                  + "--- WEIGHTED --- \n" + "-------------------")
            print(total.sort_values(ascending=False))
            print("\n")
    case 'save-all':
        l = ["Earnings", "Project", "Algorithm", "Social", "Influence"]
        save_all(l)
