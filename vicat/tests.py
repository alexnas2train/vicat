from django.test import TestCase

# Create your tests here.
def test_add_package_view(self):
    url = reverse('my-url')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'package/package_form.html')
    for c in Category.objects.all():
        self.assertContains(response, c.title)
    count = Package.objects.count()
    response = self.client.post(url, {
        'category': Category.objects.all()[0].pk,
        'repo_url': 'http://github.com/django/django',
        'slug': 'test-slug',
        'title': 'TEST TITLE',
    }, follow=True)
    self.assertEqual(Package.objects.count(), count + 1)
    self.assertContains(response, "Django")




