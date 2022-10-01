import wikipedia

def get_info(given_name):
    info = wikipedia.page(given_name)
    summary = wikipedia.summary(given_name, sentences = 2)
    print(f'\n{info.title}\n')
    print(summary, '\n')
    print(f'Source: {info.url}')
