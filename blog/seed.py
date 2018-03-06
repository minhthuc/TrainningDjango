from post.models import Post, Author
from faker import Faker

faker = Faker()
posts = Post.objects.all()
for post in posts:
    post.pub_time = faker.date_time()
    post.save()
for _ in 10:
    Author.objects.create(name = faker.name(), dob = faker.date())