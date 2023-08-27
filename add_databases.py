from api import app, db
from api.models.comments import Comments
from api.models.posts import Posts
from api.models.tags import Tags
from api.models.users import Users

user1 = Users("user1", "okome", "password")
user2 = Users("user2", "okome2", "password2")
user3 = Users("user3", "okome3", "password3")

post1 = Posts(1, "post1", "2020-01-01")
post2 = Posts(2, "post2", "2020-01-02")
post3 = Posts(3, "post3", "2020-01-03")

comment1 = Comments(1, 1, "comment1")
comment2 = Comments(1, 3, "comment2")
comment3 = Comments(3, 2, "comment3")

tag1 = Tags("tag1", "2020-01-01")
tag2 = Tags("tag2", "2020-01-04")
tag3 = Tags("tag3", "2020-01-07")

with app.app_context():
    db.drop_all()
    db.create_all()

    # テーブルの名前とリセットしたい値を指定
    table_name = "your_table_name"
    desired_value = 1  # リセットしたい値

    user1.registerUser()
    user2.registerUser()
    user3.registerUser()
    post1.registerPost()
    post2.registerPost()
    post3.registerPost()
    comment1.registerComment()
    comment2.registerComment()
    comment3.registerComment()
    tag1.registerTag()
    tag2.registerTag()
    tag3.registerTag()
    print(Users.query.all())
    print(Posts.query.all())
    print(Comments.query.all())
    print(Tags.query.all())
