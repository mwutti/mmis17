import os
import pickle
import download_flickr
import classify

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

#init flickr and keras helper
flickrHelper = download_flickr.Flickr()
kerasHelper = classify.Classify()

#start process
for i, word in enumerate(randomwordList):
    if word == latestWord:
        print('Processing word ' + word + ' ' + str(i + 1) + ' out of ' + str(len(randomwordList)))
        photo_urls_src = []
        photo_urls_org = []

        helperResponse = flickrHelper.loadImageData(word)

        for photo in helperResponse['photos']['photo']:
            if 'url_q' in photo.keys() and 'url_o' in photo.keys():
                photo_urls_src.append(photo['url_q'])
                photo_urls_org.append(photo['url_o'])

        if len(photo_urls_src) > 0:

            #all urls for the keyword are in photo_urls
            classified_images = kerasHelper.classifyImagesByUrls(photo_urls_src, photo_urls_org)

            print('writing results to file')
            #write results to textfile
            with open(os.path.join(working_directory, 'classify_results1.txt'), 'a') as resultfile:
                resultfile.write('\n'.join('%s %s %f %s %f %s %f %s' % x for x in classified_images))

        latestWord = randomwordList[i + 1]
        pickle.dump(latestWord, open("latest.p", "wb"))

