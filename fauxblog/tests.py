from django.test import TestCase
from django.contrib.auth.models import User
from .models import ImagePost, Category, Location

# Create your tests here.
class ImagePostTestClass(TestCase):

    # Creating a new editor and saving it
    def setUp(self):
        self.new_location = Location(location = 'testing')
        self.new_location.save()
        self.new_category = Category(category = 'testing')
        self.new_category.save()
        self.new_user = User(first_name = 'James', last_name = 'Bond', username = 'jamie', email = 'jamesbond@gmail.com')
        self.new_user.save()
        self.new_image= ImagePost(image_name = 'Test Image', image_description = 'This is a random test Post', image_location = self.new_location, image_category = self.new_category, date_publshed = '11/11/2019', posted_by = self.new_user)
        self.new_image.save()

    def tearDown(self):
        ImagePost.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()

    def test_save_image(self):
        self.new_image.save_image()
        pictures = ImagePost.objects.all()
        self.assertTrue(len(pictures) > 0)

    def test_delete_image(self):
        picture = self.new_image
        picture.save()
        picture.delete_image()
        self.assertTrue(len(ImagePost.objects.all()) == 0)

    def test_get_image_by_id(self):
        test_id = 1
        picture = ImagePost.objects.filter(id = self.new_image.id ).first()
        self.assertTrue(picture is not None)

    def test_search_by_category(self):
        test_category = 1
        picture = ImagePost.search_by_category(self.new_category)
        self.assertTrue(len(picture) > 0)
    
    def test_filter_by_location(self):
        test_location = 1
        picture = ImagePost.filter_by_location(self.new_location)
        self.assertTrue(len(picture) > 0)

class CategoryTestCase(TestCase):

    # Set up method
    def setUp(self):
        self.new_category = Category(category = 'testing')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_category, Category))

    # Testing Save method
    def test_save_method(self):
        self.new_category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

    def test_delete_method(self):
        category = self.new_category
        category.save_category()
        category.delete_category()        
        self.assertTrue(len(Category.objects.all()) == 0)

class LocationTestCase(TestCase):

    # Set up method
    def setUp(self):
        self.new_location = Location(location = 'testing')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_location, Location))

    # Testing Save method
    def test_save_method(self):
        self.new_location.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)

    def test_delete_method(self):
        location = self.new_location
        location.save_location()
        location.delete_location()        
        self.assertTrue(len(Location.objects.all()) == 0)
