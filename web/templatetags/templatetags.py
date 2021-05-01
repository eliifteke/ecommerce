from django import template
register = template.Library()
from service.models import UrunModel as urun


@register.inclusion_tag("tools/slider.html")
def slideryonetim():
    u = urun.objects.all()
    return {'urunler' : u}

@register.inclusion_tag("tools/social.html")
def social():
    return {'data':'data'}

@register.inclusion_tag("tools/loginsystem.html")
def loginsystem():
    return {'data': 'data'}

@register.inclusion_tag("tools/navbar.html")
def navbar():
    return {'data':'data'}


@register.inclusion_tag("tools/footer.html")
def footer():
    return {'data':'data'}

@register.inclusion_tag("tools/urundetay.html")
def urundetaymodal(u : urun):
    return {'urun':u}