from django.test import TestCase
from django.urls import reverse

from .models import AboutUs, Category, ContactMessage, Post


class BlogViewsTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Technology")
        self.post = Post.objects.create(
            title="The Art of Coding",
            content="Writing code is mostly reading and thinking.",
            image_url="https://example.com/code.jpg",
            category=self.category,
        )
        AboutUs.objects.create(content="About this blog.")

    def test_index_lists_posts(self):
        response = self.client.get(reverse("blog:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "The Art of Coding")

    def test_search_filters_posts(self):
        response = self.client.get(reverse("blog:index"), {"q": "reading"})
        self.assertContains(response, "The Art of Coding")

        response = self.client.get(reverse("blog:index"), {"q": "cooking"})
        self.assertNotContains(response, "The Art of Coding")

    def test_detail_page_uses_slug(self):
        response = self.client.get(
            reverse("blog:detail", kwargs={"slug": self.post.slug})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "The Art of Coding")

    def test_missing_post_returns_404(self):
        response = self.client.get(
            reverse("blog:detail", kwargs={"slug": "does-not-exist"})
        )
        self.assertEqual(response.status_code, 404)

    def test_contact_form_saves_message(self):
        response = self.client.post(
            reverse("blog:contact"),
            {
                "name": "Anu",
                "email": "anu@example.com",
                "message": "Hello from the test suite.",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactMessage.objects.count(), 1)
        self.assertContains(response, "Your message has been received")

    def test_contact_form_rejects_invalid_email(self):
        response = self.client.post(
            reverse("blog:contact"),
            {"name": "Anu", "email": "not-an-email", "message": "Hello"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactMessage.objects.count(), 0)
        self.assertContains(response, "Enter a valid email address")

    def test_about_page_uses_database_content(self):
        response = self.client.get(reverse("blog:about"))
        self.assertContains(response, "About this blog.")
