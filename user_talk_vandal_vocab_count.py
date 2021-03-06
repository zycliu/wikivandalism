from wkv_common import *

def user_talk_vandal_vocab_count(username):
    req = construct_user_talk_page_contents_request(username, 500)
    jsontxt = make_wikipedia_request(req)
    vandalvocab = ['unconstructive', 'revert', 'vandal', 'block', 'warn']
    wordsInText = jsontxt.replace(',', ' ').split(' ')
    vandalwordcount = 0
    for vandalword in vandalvocab:
        for w in wordsInText:
            if vandalword in w:
                vandalwordcount += 1
    return vandalwordcount
