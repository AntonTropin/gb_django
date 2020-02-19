from django.shortcuts import render
from productsapp.models import Category, Type, Product

# Create your views here.

def main(requiest):
    return render(
        requiest,
        'mainapp/index.html',
        {
            'args' : [
                {'src': '/static/mainapp/media/ipad-pro-12in-cell-select-gold.jpg', 'name': 'Apple iPad Pro 12.9"(2017)', 'description': '512GB Wi-Fi + Cellular Gold', 'old_price': '91.990₽', 'new_price': '86.990₽'},
                {'src': '/static/mainapp/media/ipad-wifi-select-gold-201803.212x212.png', 'name': 'Apple iPad (2018)', 'description': '128GB Wi-Fi + Cellular Gold', 'old_price': '42.490₽', 'new_price': '39.490₽'},
                {'src': '/static/mainapp/media/iphone7-rosegold-select-2016_av1.212x212.png', 'name': 'Apple iPhone 7', 'description': '32GB Rose Gold', 'old_price': '34.990₽', 'new_price': '31.990₽'},
                {'src': '/static/mainapp/media/mnng2ru.212x212.jpeg', 'name': 'Apple Watch Series 2', 'description': '38mm, silver, алюминевые', 'old_price': '91.990₽', 'new_price': '86.990₽'},
                {'src': '/static/mainapp/media/MacBookAirSale.jpg', 'name': 'MacBook Air 13'' (2017)', 'description': '1.8Ghz, 8Gb, 128Gb (РСТ)', 'old_price': '71.990₽', 'new_price': '61.990₽'},
                {'src': '/static/mainapp/media/tv4.png', 'name': 'Apple TV 4'' (2017)', 'description': '32Gb', 'old_price': '13.990₽', 'new_price': '10.990₽'},
                {'src': '/static/mainapp/media/beats_one.jpeg', 'name': 'Беспроводные наушники', 'description': 'Beats x', 'old_price': '8.990₽', 'new_price': '7.490₽'},
                {'src': '/static/mainapp/media/beats_two.jpeg', 'name': 'Наушники Beats', 'description': 'Solo3 Wireless', 'old_price': '71.990₽', 'new_price': '61.990₽'}
            ]
        }
        )

def support(requiest):
    return render(requiest, 'mainapp/support.html')
