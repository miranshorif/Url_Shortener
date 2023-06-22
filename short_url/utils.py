from django.conf import settings
from random import choice
from string import ascii_letters,digits


SIZE = 7
AVABLEABLE_CHARS = ascii_letters + digits
def create_random_chars(chars=AVABLEABLE_CHARS):
    return "".join(
        [choice(chars) for _ in range(SIZE)]
    )
    
def create_shortened_url(model_instance):
    randome_chars = create_random_chars()
    model_class = model_instance.__class__
    if model_class.objects.filter(short_url=randome_chars).exists():
        return create_shortened_url(model_instance)
    return randome_chars
