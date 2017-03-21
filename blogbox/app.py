from flask import Flask, send_file, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import literal
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__, template_folder=".")
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://blogbox:blogbox@db/blogbox"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public = db.Column(db.Boolean)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.String(500), nullable=False)
    tagstring = db.Column(db.String(100))

    def __init__(self, public, title, body, tagstring):
        self.public=public
        self.title=title
        self.body=body
        self.tagstring=tagstring

    def __repr__(self):
        return "({}) {} - {}".format(self.public, self.id, self.title)

db.drop_all()
db.create_all()

post1 = Post(False, "The Answers", "I was searching around for stuff today! I found this super cool string. Whatcha think? easyctf{i_cant_GET_n0_s@tisfAct10N}", "cool, easyctf, apistorm, hekked")
post2 = Post(True, "Dustbin Dreams", "Should the previous woman compose? The postscript cracks. The dustbin stretches. His outstanding mixture rephrases whatever wind. Past the painted religion hardens his fooling bench. My rolling reluctance inserts the purchase. When will our market die? An imperial household banks a desire within the grab havoc. The corporate orbit believes. The configured march toes the line underneath the tip. His lazy promise storms. The capital razors the view.", "these, words, don't, make, sense")
post3 = Post(True, "Electronic Misery", "Should the vote create a modified sabotage? A satire pants? The reluctance creams the shaken deed. Outside an electronics hunts a window. How does a stone fume past the cuddly cry? The rain returns past a detailed apple. The organized passage deeds another image. A load toys with the incorporate philosophy. Within the contained hook gossips an adult dive. An evil wets my expressway. The rhyme loses. A sack arrests the trap. The mental ballet changes before the restrictive quest.", "what, is, wrong, with, this, dumb, ctf")
post4 = Post(True, "Tennis Slam", "The fabric scratches! An arbitrary chair fumes with the scarce alphabet. A coupled manager invokes the elevator near the mistaken minister. The bigot inhabits a sabotage with the modified amateur. Outside the privileged disclaimer cries the mediaeval page. Will the people button the accusing refrain? The annual reject collapses against the nonsense defeat. A conduct toes the line behind the imperfect tennis. Underneath the reactionary succeeds the derived hook.", "lol, what, do, these, words, mean")
post5 = Post(True, "Delicate Comedy", "Throughout a soul declines the poor follower. The undefined climate pops the monthly automobile. The flame hunts after a radio. The outgoing love pastes the harden. A contest cheats inside a sarcasm. Your backbone believes. A node exercises underneath the occasional age. The military racks the fundamental god. How can every flag trip? How can every stupid husband return? The variant trades a cardboard handbook.", "kek, good, luck, solving, me")
post6 = Post(True, "A Glutton's Lament", "A communal flower waffles next to the struggle. A project surveys the neck. When can the human gender score the supported timer? The microprocessor waves throughout any approach. The unwelcome pan flies against the repulsive excess. The humble offender volunteers into a publicized romance. Whatever snack crashes. The virgin cough believes across a moved ax.", "these, tags, are, useless, rip")
db.session.add(post1)
db.session.add(post2)
db.session.add(post3)
db.session.add(post4)
db.session.add(post5)
db.session.add(post6)
db.session.commit()

@app.route("/", methods=["GET", 'POST'])
def index():
    if request.method == 'POST':
        q = request.form['query']
        return redirect('/search?query={}'.format(q))
    return render_template("index.html")

@app.route("/search")
def search():
    q = request.args.get("query")
    pub = request.args.get("public") not in ['False', 'false', '0']
    q = q if len(q) > 2 else chr(0)
    res = Post.query.all()
    res = filter(lambda g: g.public == pub and q.lower() in g.body.lower(), res)
    return render_template('search.html', results=res, search_phrase=q)

app.run(host="0.0.0.0", port=80)
# app.run(debug=True)
