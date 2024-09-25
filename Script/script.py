import feedparser as fp
import pandas as pd
import re

# Section of interest are:
# Sports
# Economy
# Science and technology
# Culture

# For each news article extract:
# Title (<title>)
# Content summary (<description>)
# Section
# URL (<link>)
# Date of publication (<pubDate>)


def get_news(url, source, section):
    df = pd.read_csv('raw data corpus.csv')
    d = fp.parse(url)
    new_data = []
    new_entries = 0

    for post in d.entries:
        # Check if the post is already in the dataframe
        if post.title in df['Title'].values:
            print(f"Post: {post.title} already in dataframe")
            continue
        else:
            new_date = change_date_format(post.published)
            new_data.append(
                [source, post.title, post.description, section, post.link, new_date]
            )
            new_entries += 1

    add_news(df, new_data)
    return new_entries

def add_news(df, new_data):
    new_data_df = pd.DataFrame(new_data, columns=['Source', 'Title', 'Content', 'Section', 'URL', 'Date'])
    df_updated = pd.concat([df, new_data_df], ignore_index=True)
    df_updated.to_csv('raw data corpus.csv', index=False)

def clean_data(df):
    empty_df = df[0:0]
    empty_df.to_csv('raw data corpus.csv', index=False)

def change_date_format(old_date):

    new_date = date.search(old_date).group(0).split(" ")
    month = months.get(new_date[1])
    new_date = f"{new_date[0]}/{month}/{new_date[2]}"

    return new_date

if __name__ == '__main__':
    months = {
        "Jan": "01",
        "Feb": "02",
        "Mar": "03",
        "Apr": "04",
        "May": "05",
        "Jun": "06",
        "Jul": "07",
        "Aug": "08",
        "Sep": "09",
        "Oct": "10",
        "Nov": "11",
        "Dec": "12"
    }
    date = re.compile("\d\d? \w\w\w \d\d\d\d")

    new_entries = get_news('https://www.jornada.com.mx/rss/deportes.xml?v=1', 'La Jornada', 'Sports')

    new_entries += get_news('https://www.jornada.com.mx/rss/economia.xml?v=1',  'La Jornada', 'Economy')
    new_entries += get_news('https://expansion.mx/rss/economia', 'Expansion', 'Economy')

    new_entries += get_news('https://www.jornada.com.mx/rss/ciencias.xml?v=1', 'La Jornada', 'Science and technology')
    new_entries += get_news('https://expansion.mx/rss/tecnologia', 'Expansion', 'Science and technology')

    new_entries += get_news('https://www.jornada.com.mx/rss/cultura.xml?v=1', 'La Jornada', 'Culture')

    print(f"New entries: {new_entries}")
    print(f"Total entries: {len(pd.read_csv('raw data corpus.csv'))}")

    # df = pd.read_csv('raw data corpus.csv')
    # df['Date'] = df['Date'].apply(change_date_format)
    # df.to_csv('raw data corpus.csv', index=False)


