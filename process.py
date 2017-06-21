import os
import pickle
import download_flickr

working_directory = os.path.dirname(os.path.realpath(__file__))


def getRandomWordList():
    random_word_path = os.path.join(working_directory, "random_words.txt")
    with open(random_word_path) as file:
        return file.read().splitlines()

#get the lrandom word list
randomwordList = getRandomWordList()

# init the first words
if not os.path.isfile(os.path.join(working_directory, "latest.p")):
    pickle.dump("beach", open("latest.p", "wb"))

latestWord = pickle.load(open("latest.p", "rb"))

#init flickr helper
helper = download_flickr.Flickr()

#start process
for i, word in enumerate(randomwordList):
    if word == latestWord:
        photo_urls = []
        helperResponse = helper.loadImageData(word)

        for photo in helperResponse['photos']['photo']:
            photo_urls.append(photo['url_z'])

        #all urls for the keyword are in photo_urls

        latestWord = randomwordList[i + 1]
        pickle.dump(latestWord, open("latest.p", "wb"))


# flickr = FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, format='parsed-json')
# extras='url_sq,url_t,url_s,url_q,url_m,url_n,url_z,url_c,url_l,url_o'
# cats = flickr.photos.search(text='kitten', per_page=5, extras=extras)
# photos = cats['photos']
