import pickle
import gzip

from metainfo import readmetadata


WHITELIST_FILE = './whitelist.csv'

requirements = {
    'language': 'en',
    'formats': 'text/plain',
}

def ebook_suitable(ebook):
    try:
        return all(v in ebook[k] for k, v in requirements.items())
    except:
        return False

def generate_whitelist(whitelist_location):
    md = readmetadata()
    whitelist = [ebook['formats']['text/plain'] for i, ebook in md.items() if ebook_suitable(ebook)]
    with open(whitelist_location, 'w') as f:
        f.write('\n'.join(str(i) for i in whitelist))


if __name__ == '__main__':
    generate_whitelist(WHITELIST_FILE)