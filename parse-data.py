import pandas as pd


def main():
    df = pd.read_csv("./version-v-tested.csv")
    data = pd.read_csv('./data.csv')

    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

    # filter out any failing rows
    passing = df[df['result'].str.contains("pass")]
    release = df['release']
    release2 = data['release']

    sorting = passing.sort_values(by=['release'], ascending=False)
    
    delta = pd.concat([release,release2]).drop_duplicates(keep=False)

    print("main dataframe:")
    print(df.head())

    # print("DF 2:")
    # print(data.head())

    print("release:")
    print(release.head())

    print("release2:")
    print(release2.head())

    print("delta:")
    print(delta.head())

    print("Sort:")
    print(sorting.head())

    release43 = passing[passing['release'].str.contains("4.3")].sort_values(by=['release'], ascending=False)
    print(release43.head())

if __name__ == '__main__':
    main()
