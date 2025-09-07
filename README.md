## Görüntü İşleme

### Görüntü işleme nedir?
 Görüntü işleme, en basit haliyle, önceden kaydedilen görüntülerin ya da videoların bilgisayarlar tarafından anlaşılabilir bir hale getirilerek analiz edilmesi ve yorumlanması sürecidir. Bu süreçte amaç, insan gözünün kaçırabileceği ayrıntıları yakalamak, verileri sayısal formata dönüştürmek ve bu verilerden anlamlı sonuçlar çıkarmaktır.

### Görüntü işleme nerede kullanılır? 
 Örneğin bir fotoğrafın kalitesini arttırmak, yüklenen bir fotoğrafta yüz, obje tespiti, duygu tespiti, tıpta röntgen, MR veya ultrason gibi görüntülerin analiz edilerek hastalıkların teşhisine yardımcı olur. Endüstride, üretim hattındaki ürünlerin kalite kontrolü için otomatik denetim sistemlerinde kullanılır. Otonom araçlarda, yol, yaya ve diğer araçları algılayarak güvenli sürüş sağlar. Güvenlik sistemlerinde, yüz tanıma veya parmak izi okuma gibi biyometrik teknolojilerin temelini oluşturur.verebiliriz.

 
### Bu projede neler yer almaktadır?
 
 ## netlestirme.py
 Yüklediğimiz kalitesi düşük olan bir fotoğrafı 1920x1080pye getirmemizi sağlayan bir program. RealEsrgan teknolojisinden faydalanarak çalışıyor ancak çalışması biraz uzun süren bir programdır yani çalıştırdıktan sonra yaklaşık 5-10 dakika beklemeniz gerekmektedir. 

 ## sekil.py

 Yüklediğiniz fotoğraf üzerindeki üçgen, kare, dikdörtgen, daire ve çokgenleri tespit edip ekrana yazdırmamızı sağlar. Kodun mantığı köşe saymaktan geçiyor ne kadar köşesi varsa ona göre şekli yazıyor eğer ki dörtgense aspect ratiosuna yani boyu ve enine göre farkı anlıyor.

 ## kedi.html

 Yüklediğiniz fotoğraftaki kedileri tespit etmeye yarayan bir yazılımdır. Bu yazılım TensorFlow'dan destek alarak çalışmaktadır.

 ## qrtest.py

 kameraya gösterdiğimiz qr kodları tespit edip çıktısını ya da yönlendireceği siteyi terminale yazan bir programdır.

 ## Gereksinimler

- python 3.8.10 
homebrew ile kurmak isterseniz "brew install python@3.10"
eğer ki çalışmazsa pip install yazıp import yazan kütüphaneleri indirmelisniz

- requirements.txt dosyasındaki kütüphaneler
"pip install -r requirements.txt" komutu ile indirebilirsiniz.

ya da bunlarla uğraşmak istemiyorsanız kurulum.sh dosyasını çalıştırabilirsiniz.

