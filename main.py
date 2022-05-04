from flask import Flask, request, render_template
from functions import read_json, len_list, len_comments, get_posts, len_comments_2

app = Flask(__name__)


@app.route('/')
def main():
    list_1 = read_json("data/data.json")
    number = len_list("data/data.json")
    list_2 = read_json("data/comments.json")
    numbers = 0
    # numbers = len_comments("data/comments.json", postid)
    # with open("data/data.json", "r", encoding='utf-8') as file:
    #     list_1 = json.load(file)
    #     number = len(list_1)
        # for i in list_1:
            # poster_name = i["poster_name"]
            # poster_avatar = i["poster_avatar"]
            # pic = i["pic"]
            # content = i["content"]
            # views_count = i["views_count"]
            # likes_count = i["likes_count"]da
            # pk = i["pk"]
    return render_template('test.html', list_1=list_1, number=number, list_2=list_2)   #poster_name=poster_name, poster_avatar=poster_avatar, pic=pic, content=content, views_count=views_count, likes_count=likes_count, pk=pk)


@app.route('/posts/<int:postid>')
def post(postid):
    list_1 = read_json("data/data.json")
    list_2 = read_json("data/comments.json")
    number = len_comments("data/comments.json", postid)
    return render_template('post.html', postid=postid, list_1=list_1, list_2=list_2, number=number)


@app.route('/search')
def search():
    search_1 = request.args.get('s')
    list_3 = read_json("data/data.json")
    posts = get_posts(list_3, search_1)
    return render_template('test_2.html', posts=posts, numbers=len(posts), search_1=search_1)
    #return f'{search_1}'


# @app.route('/search/search')
# def search_1():
#     search_1 = request.args.get("s")
#     return f"{search_1}"


@app.route('/users/<username>')
def user(username):
    list_1 = read_json("data/data.json")
    number = len_comments_2("data/comments.json", list_1, username)
    return render_template('user-feed.html', list_1=list_1, username=username, number=number)




if __name__ == "__main__":
    app.run(debug=True)