from random import SystemRandom
from django.utils.text import slugify
import string


def random_latters(k=5):
    return ''.join(SystemRandom().choice(string.ascii_letters + string.digits, k=k))

def slugify_new(text):
    return slugify(text) + '-' + random_latters()