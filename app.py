from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbjungle

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/memo', methods=['POST'])
def post_article():
    # 1. 클라이언트로부터 데이터를 받기
    comment_title = request.form['title_give']  # 클라이언트로부터 title를 받는 부분
    comment_receive = request.form['comment_give']  # 클라이언트로부터 comment를 받는 부분
    comment_cardnum = makeCard[2][i]
    article = {
        'title':comment_title, 
        'comment': comment_receive
        'cardnum' : comment_cardnum
        }

    # 3. mongoDB에 데이터를 넣기
    db.articles.insert_one(article)
    return jsonify({'result': 'success'})


@app.route('/update', methods=['POST'])
def post_article():
    # 1. 클라이언트로부터 데이터를 받기
    comment_title = request.form['title_give']  
    comment_receive = request.form['comment_give']  

    article = {
        'title':comment_title, 
        'comment': comment_receive
        }

    # 3. mongoDB에 데이터를 넣기
    db.articles.insert_one(article)
    return jsonify({'result': 'success'})

    



@app.route('/memo', methods=['GET'])
def read_memos():
    # 1. mongoDB에서 _id 값을 제외한 모든 데이터 조회해오기 (Read)
    articles = list(db.articles.find({}, {'_id': 0}))
    # 2. all_articles라는 키 값으로 article 정보 보내주기
    return jsonify({'result': 'success', 'all_articles': articles})





@app.route('/delete', methods=['POST'])
def post_article():
    # 1. 클라이언트로부터 데이터를 받기
    comment_title = request.form['title_give']  # 클라이언트로부터 title를 받는 부분
    comment_receive = request.form['comment_give']  # 클라이언트로부터 comment를 받는 부분

    article = {
        'title':comment_title, 
        'comment': comment_receive
        }

    # 3. mongoDB에 데이터를 넣기
    db.articles.insert_one(article)

    return jsonify({'result': 'success'})


if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)
