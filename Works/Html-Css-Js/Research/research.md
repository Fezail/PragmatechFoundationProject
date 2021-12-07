Sual 1: CSS-də px və % xaricində hansı ölçü vahidləri var nümunələr verin.

CSS içinde uzunluk ve genişlik tanımlamaları için bir çok ölçü birimi vardır. Bunların bazıları baskı dünyasından gelmiş bazıları günlük hayattan, bazıları da bilişim teknolojilerinde kullanılan ölçü birimleridir.

GÖRECELİ (RELATIVE) ÖLÇÜ BİRİMLERİ

em : Bağıl ölçü birimi olarak da adlandırılır. Bu ölçü biriminde varsayılan font ailesinde (font-family) yer alan M harfinin genişliğinin ölçü için referans olarak alınmasıdır. Aslen bir tipografi ölçü birimidir.  Eğer 1em değerini 16px olarak alırsanız, herhangi bir boyutlandırma işleminde 2em değeri verdiğinizde bu boyutun 32px değerine karşılık geldiğini görürsünüz. em ölçü birimi bir HTML elementinin kendi hiyerarşisinde kendini kapsayıcı elementinin font boyutuna göre değişiklik gösterir. Ayrıca siz font-size değeri sabit iken font-family değiştirirseniz görüntüde değişiklikler olur.  Bir html tagının font-size değeri 16px ise bu 1 em’ye eşit demektir. font-size değeri 12px olarak atanmış ise bu defa da 1em 12px olacaktır. Bu şekilde bir CSS yapısı oluşturduğunuzda sadece tagının font-size değerini değiştirdiğinizde sayfanızdaki bütün fontların boyutlarının da aynı oranda değiştiğini göreceksiniz. Ayrıca bu ölçü birimini sadece font-size değerini belirlerken değil diğer bütün elementlerin ölçülerinin belirlenmesinde de kullanabilirsiniz.

ex : em elementi ile benzerlik gösterir. Tek farkı font ailesinde (font-family) küçük x harfinin yüksekliği ölçü için referans alınmasıdır. Bu da genellikle font ailesindeki bir harfin yüksekliğinin yarısına denk gelir.

rem : root em kısaltılışıdır. Daha uyumlu ve dengeli tasarım yapmanıza yardımcı olan bir ölçü birimidir. rem ölçü birimi bir html sayfasının element diziliminin en kök (root) elementinin font-size değeri demektir.  Bu da bir web sayfasında < html > elementine karşılık gelir.

px : Ekran çözünürlüğüne göre değişen ve ekranda bulunan noktaların (bu her bir noktaya piksel denir) bir tanesinin yüksekliğidir. Standart bilgisayar ekranlarında 1 inç başına 96 nokta düşer. Buna DPI (Dot per Inch) denir. Bir bilgisayar veya televizyon ekranlarına çok çok yakından bakarsanız çok küçük kutucuklardan oluşmuş bir ızgara görürsünüz. İşte buradaki görünen her bir kutucuk aslında 1 pikseldir. Buda demektir ki piksel ölçü birimi her monitöre göre farklılık gösterir. Piksel cinsinden font boyutunu ayarlamak en doğru yöntemdir. Ancak bu yöntem eski tarayıcılar ve kapraz geliştiriler (cross platform) için farklılıklar gösterebilmektedir. Ancak bu farklılık çok önemsenecek bir türden farklılık değildir. Piksel ölçü birimi görüntüleme cihazları için kullanılan bir ölçü birimidir. Düşük dpi cihazlar için 1px, ekranın bir noktasına karşlılık gelir. Yazıcılar ve yüksek çözünürlüklü ekranlar için 1px, birden fazla piksel anlamına gelebilir.

% : Uygulanan nesneye göre değişen bir birimdir. Bir html elementinin varsayılan değerine göre kendini ayarlar. Bu ölçü birimi her zaman başka bir ölçü birimine göre kendisini orantılı olarak değiştiren bir birimdir. Kullanımı orantı değeri ve yüzde işaretinden meydana gelir. 50% gibi. Mesela sayfamızda 800px genişliğinde bir element olsun. Bu elementin içerisinde eşit boylarda 4 kutu oluşturulacağını varsayalım. Bunun için kutuların genişliklerini 25% değeri vermek yeterli olacaktır. Sonuç olarak her bir kutunun değeri 200px olarak ayarlanır. Eğer sayfamızdaki 800px genişliğindeki element 600px genişliğine düşürmek istersek bu sefer kutuların genişlikleri otomatik olarak 150px olur. Bu mantık özellikle duyarlı tasarımlar (responsive) için çok kullanışlı bir yoldur.

ch :  Tıpkı em ölçü birimi gibi ch ölçü birimi de varsayılan font ailesinde (font-family) yer alan “0″ (sıfır) sayısının genişliğinin ölçü için referans olarak alınmasıyla oluşur. Her karakterin sabit genişlikte olduğu monospace yazı tiplerine uygun bir tanımdır.





Sual 2: div,section,main,article,aside taglarinin hansı hallarda istifadə oluna biləcəyini qeyd edin.

div : Etiketi bir HTML belgesindeki bir bölümü ve ya bölümü tanımlar. Class ve ya id özelliği kullanılarak kolayca biçimlendirilir.

section : Etiketi bir belgedeki bir bölümü tanımlar.

main : Etiketi bir belgenin ana içeriğini belirtir.

article : Etiketi bağımsız, kendi-kendine yeten içeriği belirtir.

aside : Etiketi, yerleştirildiği içerik dışında bazı içerikleri tanımlar.




Sual 3: display:inline-block,display:inline,display:table,display:grid,display:flex xüsusiyyətlərini araşdıraraq məqsədlərini 2-3 cümlə ilə ifadə edin.

display:inline-block : Satır içi blok olarak ayarlanan bir öğe, metnin doğal akışıyla ("taban çizgisinde") satır içi olarak ayarlanacağı için satır içi öğeye çok benzer. Aradaki fark, saygı duyulacak bir genişlik ve yükseklik ayarlayabilmenizdir.

display:inline : Öğe, kendilerinden önce veya sonra satır sonları oluşturmayan bir veya daha fazla satır içi öğe kutusu oluşturur. Normal akışta boşluk varsa bir sonraki eleman aynı satırda olacaktır.

display:table : Bunun gerçekleşmesi gerekiyorsa, tablo dışı öğeleri tablo öğeleri gibi davranmaya zorlayan bir dizi görüntüleme değeri vardır. Nadirdir, ancak bazen tabloların benzersiz konumlandırma güçlerini kullanırken kodunuzla "daha semantik" olmanıza izin verir.

display:grid : CSS Izgara Düzen Modülü, satırlar ve sütunlar içeren ızgara tabanlı bir düzen sistemi sunarak, kayan noktalar ve konumlandırma kullanmak zorunda kalmadan web sayfalarını tasarlamayı kolaylaştırır.

display:flex : Flexbox modelini kullanmaya başlamak için önce bir esnek kap tanımlamanız gerekir.