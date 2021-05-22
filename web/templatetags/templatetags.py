from django import template
register = template.Library()
from service.models import UrunModel as urun, KategoriModel


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


@register.inclusion_tag("tools/sliderresim.html")
def urunsliderresim(u:urun):
    # for resim in u.urunresimler_set.all():
    #     if resim.sliderresim :
    #         return {'resim':resim.urunresim.url}

    # resim = u.urunresimler_set.all()[len(u.urunresimler_set.all())-1]

    return {'resim':u.resim.url}


# @register.inclusion_tag("tools/kategoriurunler.html")
# def kategoriurunler():
#     kategoriler  = KategoriModel.objects.all()
#     urunler = []
#     for kategori in kategoriler:
#          urunler  = urun.objects.filter(kategori)