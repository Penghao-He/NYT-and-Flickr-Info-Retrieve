import requests
import json
import sys
NYT_API_KEY = "9e746a919f6d4b05b7d62417458ee6f6"
CACHE_FNAME = "SI506finalproject_cache.json"
KEYWORD = sys.argv[1]                               #The keyword searched by NYT, can be modified
try:
    cache_file = open(CACHE_FNAME, 'r')
    CACHE_DICTION = json.load(cache_file)
    cache_file.close()
except:
    CACHE_DICTION = {}

def params_unique_combination_nyt(baseurl, params_d):
    alphabetized_keys = sorted(params_d.keys())
    res = []
    for k in alphabetized_keys:
        res.append("{}={}".format(k, params_d[k]))
    return baseurl + "?" + "&".join(res)

def get_nyt_data(tags_string, n=50):
    baseurl = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
    params_diction = {}
    params_diction["api-key"] = NYT_API_KEY
    params_diction["q"] = "+".join(tags_string.split())
    params_diction["sort"] = 'newest'
    unique_ident = params_unique_combination_nyt(baseurl, params_diction)
    if unique_ident in CACHE_DICTION:
        print("Getting cached data...")
        return CACHE_DICTION[unique_ident]
    else:
        print("Making a request for new data...")
        nyt_resp = requests.get(baseurl, params= params_diction)
        nyt_text = nyt_resp.text
        CACHE_DICTION[unique_ident] = json.loads(nyt_text)['response']['docs']
        dumped_json_cache = json.dumps(CACHE_DICTION)
        print('Saving in '+CACHE_FNAME)
        fw = open(CACHE_FNAME, "w")
        fw.write(dumped_json_cache)
        fw.close()  # Close the open file
        return CACHE_DICTION[unique_ident]

class Article:
    def __init__(self, dic):
        if 'keywords' in dic:
            self.keywords = [ii['value'] for ii in dic['keywords']]
        else:
            self.keywords = []
        if 'snippet' in dic:
            self.snippet = dic['snippet']
        else:
            self.snippet = ""
        if 'headline' in dic:
            self.headline = dic['headline']['main']
        else:
            self.headline = ""
        if 'pub_date' in dic:
            self.pub_date = dic['pub_date'][:10]
        else:
            self.pub_date = ""
        if "byline" in dic:
            self.author = dic['byline']['original']
        else:
            self.author = ""

    def __str__(self):
        return "\"{}\" {} On {}, {}".format(self.headline, self.author, self.pub_date, len(self.keywords))

    def find_long(self):
        num = 0
        long = ""
        for ii in self.snippet.split():
            if len(ii) > num:
                num = len(ii)
                long = ii
        return long

nyt_result = get_nyt_data(KEYWORD)
nyt_instances = []
for ii in nyt_result:
    nyt_instances.append(Article(ii))
nyt_instances_sorted = sorted(nyt_instances, key = lambda x: (len(x.keywords), x.headline), reverse = True)[:5]
long_word = [ii.find_long() for ii in nyt_instances_sorted]
for i in range(len(long_word)):
    long_word[i] = "".join([ii.lower() for ii in long_word[i] if ii.isalpha() == True])
print(long_word)

FLICKR_KEY = "25c767937ad2728d3276e36103d68a23"

def params_unique_combination_flickr(baseurl, params_d, private_keys=["api_key"]):
    alphabetized_keys = sorted(params_d.keys())
    res = []
    for k in alphabetized_keys:
        if k not in private_keys:
            res.append("{}-{}".format(k, params_d[k]))
    return baseurl + "_".join(res)

def get_flickr_data(tags_string, n=50):
    baseurl = "https://api.flickr.com/services/rest/"
    params_diction = {}
    params_diction["api_key"] = FLICKR_KEY
    params_diction["tags"] = tags_string
    params_diction["method"] = "flickr.photos.search"
    params_diction["per_page"] = n
    params_diction["format"] = "json"
    unique_ident = params_unique_combination_flickr(baseurl, params_diction)
    if unique_ident in CACHE_DICTION:
        print("Getting cached data...")
        return CACHE_DICTION[unique_ident]
    else:
        print("Making a request for new data...")
        # Make the request and cache the new data
        flickr_resp = requests.get(baseurl, params= params_diction)
        flickr_text = flickr_resp.text
        flickr_text_fixed = flickr_text[14:-1]
        CACHE_DICTION[unique_ident] = json.loads(flickr_text_fixed)
        dumped_json_cache = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME, "w")
        fw.write(dumped_json_cache)
        fw.close()  # Close the open file
        return CACHE_DICTION[unique_ident]

def get_flickr_info(id):
    baseurl = "https://api.flickr.com/services/rest/"
    params_diction = {}
    params_diction["api_key"] = FLICKR_KEY
    params_diction["method"] = "flickr.photos.getInfo"
    params_diction['photo_id'] = id
    params_diction['format'] = 'json'
    unique_ident = params_unique_combination_flickr(baseurl, params_diction)
    if unique_ident in CACHE_DICTION:
        print("Getting cached data...")
        return CACHE_DICTION[unique_ident]
    else:
        print("Making a request for new data...")
        # Make the request and cache the new data
        flickr_resp = requests.get(baseurl, params= params_diction)
        flickr_text = flickr_resp.text
        flickr_text_fixed = flickr_text[14:-1]
        CACHE_DICTION[unique_ident] = json.loads(flickr_text_fixed)
        dumped_json_cache = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME, "w")
        fw.write(dumped_json_cache)
        fw.close()  # Close the open file
        return CACHE_DICTION[unique_ident]

flickr_data = []
for ii in long_word:
    flickr_data.append(get_flickr_data(ii)['photos']['photo'])

def csv_text(str):
    s = ""
    for ii in range(len(str)):
        if str[ii]=="\"" or str[ii]=="\'":
            s += "\""+str[ii]
        else:
            s += str[ii]
    s = "\"" + s + "\""
    return s

class Photo:

    def __init__(self, dic):
        if '_content' in dic['title']:
            self.title = csv_text(dic['title']['_content'])
        else:
            self.title = ""
        if 'username' in dic['owner']:
            self.username = csv_text(dic['owner']['username'])
        else:
            self.username = ""
        if 'taken' in dic['dates']:
            self.date = dic['dates']['taken']
        else:
            self.date = ""
        if 'tag' in dic['tags']:
            self.tags = [csv_text(ii['_content']) for ii in dic['tags']['tag']]
        else:
            self.tags = []

    def __str__(self):
        return "\"{}\" by {}, taken on {}".format(self.title, self.username, self.date)

    def total_tags(self):
        return len(self.tags)

flickr_info_all = []

for ii in flickr_data:
    for jj in range(min(20,len(ii))):
        flickr_info_all.append(get_flickr_info(ii[jj]['id']))
flickr_info = []
for ii in flickr_info_all:
    if "photo" in ii:
        flickr_info.append(ii['photo'])

flickr_instances = []
for ii in flickr_info:
    flickr_instances.append(Photo(ii))

flickr_instances_sorted = sorted(flickr_instances, key = lambda x: x.total_tags(), reverse = True)

with open('Photo.csv', 'w') as p:
    p.write("Title,Username,All the tags,Number of tags\n")
    for ii in flickr_instances_sorted:
        p.write("{},{},{},{}\n".format(ii.title, ii.username, " ".join(ii.tags), ii.total_tags()))