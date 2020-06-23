from blog.models import BlogIndexPage, BlogPage
from home.models import HomePage


def test_homepage_has_body():
    assert HomePage._meta.get_field('body').__class__.__name__ == 'RichTextField'


def test_blog_index_intro_is_richtext():
    assert BlogIndexPage._meta.get_field('intro').__class__.__name__ == 'RichTextField'


def test_blog_page_intro_is_plaintext():
    assert BlogPage._meta.get_field('intro').__class__.__name__ == 'CharField'
