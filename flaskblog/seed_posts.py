import json
from flaskblog import app, db
from flaskblog.models import Post

with app.app_context():
    with open('flaskblog/snippets/posts.json') as f:
        posts = json.load(f)

    for p in posts:
        post = Post(
            title=p['title'],
            content=p['content'],
            user_id=p['user_id']
        )
        db.session.add(post)

    db.session.commit()
    print("Posts inserted successfully!")