from flask import Flask, render_template, jsonify, request
app = Flask(__name__)


from pymongo import MongoClient
client = MongoClient('mongodb')
db = client.MovieTracker

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/list', methods=['GET'])
def movie_list():
   result = list(db.movieList.find({}, {'_id':0}))
   return jsonify({'result':'success', 'msg':'GET 연결 완료!', 'movie_list':result})

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5001,debug=True)