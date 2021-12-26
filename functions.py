import json


def read_json(filename):
    with open(filename, encoding='utf-8') as f:
        return json.load(f)


def len_list(filename):
    with open(filename, encoding='utf-8') as f:
        return len(json.load(f))


def len_comments(filename, postid):
    len_comments_1 = 0
    with open(filename, encoding='utf-8') as f:
        list_1 = json.load(f)
        for i in list_1:
            if i["post_id"] == postid:
                len_comments_1 += 1
        return len_comments_1


def get_posts(data, word):
    result = []
    word_2 = f"{word}"
    for record in data:
        if word_2.casefold() in record["content"].casefold():
            result.append(record)
    return result


def len_comments_2(filename, filename_2, username):
    len_comments_1 = 0
    with open(filename, encoding='utf-8') as f:
        list_1 = json.load(f)
        for i in filename_2:
            for l in list_1:
                if i['poster_name'] == username:
                # for l in list_1:
                    if l['post_id'] == i['pk']:
                        len_comments_1 += 1
        return len_comments_1





