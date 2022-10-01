from gnewsclient import gnewsclient

def get_news():
    client = gnewsclient.NewsClient(language='English', location='United States', topic='Nation', max_results=3)
    news_list = client.get_news()
    print('\nNews Feed:\n')
    for i, item in enumerate(news_list):
        print('Title:', item['title'])
        print(f'Link: {item["link"]}')
        if i != 2:
            print()