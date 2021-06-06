eleman = 'teknik','muhasebe','yazılım'

eleman = eleman.split(',')

metin = 'ahmet ceylan ankara istanbul eskişehir'
metin2 = 'ahmet, ceylan, ankara, istanbul, eskişehir'

sonuc = metin.split(maxsplit=3)
sonuc2 = metin2.split(',')
print(sonuc)
print(sonuc2)

import re 

a = 'ali,veli;mert*than||sah'
a = re.split(',|;|\*|\|\|',a)
print(a)

