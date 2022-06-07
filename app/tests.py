from django.test import TestCase
from django.contrib.auth.models import User
from .models import *

# Create your tests here.
class TestUser(TestCase):
    def setUp(self) -> None:
        self.example_user = User(username="emma",email="emma@example.com",password="kenya@59")
        self.example_user.save()

    def test_user_instance(self):
        self.assertTrue(isinstance(self.example_user, User))

class TestProfile(TestCase):
    def setUp(self) -> None:
        self.example_user = User(username="emma",email="emma@example.com",password="kenya@59")
        self.example_user.save()

        self.example_profile = Profile(user = self.example_user,prof_pic = "../assets/avatar.png",bio = "Lorem Ipsum",website = "emma.website.com",name = "emma")

    def test_profile_instance(self):
        self.assertTrue(isinstance(self.example_profile, Profile))

class TestPost(TestCase):
    def setUp(self) -> None:
        self.example_user = User(username="emma",email="emma@example.com",password="kenya@59")
        self.example_user.save()

        self.example_profile = Profile(user = self.example_user,prof_pic = "../assets/avatar.png",bio = "Lorem Ipsum",website = "emma.website.com",name = "emma")
        self.example_profile.save()

        self.example_post = Post(image_upload="../assets/avatar.png",image_name="mypost",image_caption="Lorem ipsum",image_owner=self.example_profile)

    def tearDown(self) -> None:
        Profile.objects.all().delete()
        Post.objects.all().delete()

    def test_post_instance(self):
        self.assertTrue(isinstance(self.example_post, Post))

    def test_del_instance(self):
        self.example_post.save()
        self.example_post.delete()
        self.assertTrue(len(Post.objects.all()) == 0)

class TestComment(TestCase):
    def setUp(self) -> None:
        self.example_user = User(username="emma",email="emma@example.com",password="kenya@59")
        self.example_user.save()

        self.example_profile = Profile(user = self.example_user,prof_pic = "../assets/avatar.png",bio = "Lorem Ipsum",website = "emma.website.com",name = "emma")
        self.example_profile.save()

        self.example_post = Post(image_upload="../assets/avatar.png",image_name="mypost",image_caption="Lorem ipsum",image_owner=self.example_profile)
        self.example_post.save()

        self.example_comment = Comment(user=self.example_user, user_profile=self.example_profile,user_comment="Lorem Ipsum", post_associated=self.example_post)

    def tearDown(self) -> None:
        Profile.objects.all().delete()
        Post.objects.all().delete()
        User.objects.all().delete()

    def test_comment_instance(self):
        self.assertTrue(isinstance(self.example_comment, Comment))

    def test_del_comment(self):
        self.example_comment.save()
        self.example_comment.delete()
        self.assertTrue(len(Comment.objects.all())==0)

class TestPostVote(TestCase):
    def setUp(self) -> None:
        self.example_user = User(username="emma",email="emma@example.com",password="kenya@59")
        self.example_user.save()
        
        self.example_profile = Profile(user = self.example_user,prof_pic = "../assets/avatar.png",bio = "Lorem Ipsum",website = "emma.website.com",name = "emma")
        self.example_profile.save()

        self.example_post = Post(image_upload="../assets/avatar.png",image_name="mypost",image_caption="Lorem ipsum",image_owner=self.example_profile)
        self.example_post.save()

        self.example_post_vote = PostVote(profile_vote=self.example_profile,post_voted=self.example_post)

    def test_instance_post_vote(self):
        self.assertTrue(isinstance(self.example_post_vote, PostVote))
        




