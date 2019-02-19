from app.models import Blogpost , Users
from app import db

def setUp(self):
        self.user_loise = User(username = 'loise',password = 'potato', email = 'geerockface4@gmail.com')
        self.new_blog = Blog(id=12345,title='Full stack development',content='dont do that', date = 1-12-2019, ,user = self.user_loise)


def tearDown(self):
        Blog.query.delete()
        User.query.delete()


def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.id,12345)
        self.assertEquals(self.new_blog.title,'Full stack development')
        self.assertEquals(self.new_blog.content,"Is it safe to go the full-stack way or better the Android path")
        self.assertEquals(self.new_blog.date, 1-12-2019)
        self.assertEquals(self.new_blog.user,self.user_Gerald)

def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Review.query.all())>0)

def test_get_blog_by_id(self):

        self.new_blog.save_review()
        got_blogs = Blog.get_blogs(12345)
        self.assertTrue(len(got_blogs) == 1)