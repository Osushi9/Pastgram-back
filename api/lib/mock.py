class MockUser:
    def __init__(self, user_id, name, profile_name, icon_path):
        self.id = user_id
        self.name = name
        self.profile_name = profile_name
        self.icon_path = icon_path
    
    def copy(self):
        return MockUser(self.id, self.name, self.profile_name, self.icon_path)

user1 = MockUser(1, "tanaka", "田中", "icon-path-1")
user2 = MockUser(2, "sato", "佐藤", "icon-path-2")
user3 = MockUser(3, "nakamura", "中村", "icon-path-3")
users = [user1, user2, user3]

class MockPost:
    def __init__(self, post_id, user_id, image_path, taken_at, likes):
        self.id = post_id
        self.user_id = user_id
        self.image_path = image_path
        self.taken_at = taken_at
        self.likes = likes
    
    def copy(self):
        return MockPost(self.id, self.user_id, self.image_path, self.taken_at, self.likes)


post1 = MockPost(1, 1, "image-path-1", "2023/01/01", 10)
post2 = MockPost(2, 1, "image-path-2", "2023/02/01", 20)
post3 = MockPost(3, 2, "image-path-3", "2023/03/01", 30)
posts = [post1, post2, post3]
post = post2

class MockComment:
    def __init__(self, comment_id, post_id, user_id, content, time):
        self.id = comment_id
        self.content = content
        self.time = time
        self.user_id = user_id
        self.post_id = post_id
    
    def copy(self):
        return MockComment(self.id, self.post_id, self.user_id, self.content, self.time)

comment1 = MockComment(1, 1, 1, "sample comment 1", "2023/08/10")
comment2 = MockComment(2, 1, 2, "sample comment 2", "2023/08/20")

tag = "高校時代の思い出"
limit = "2023/08/31"