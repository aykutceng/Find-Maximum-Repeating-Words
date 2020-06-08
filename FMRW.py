import string
import re
import nltk
import collections
import operator
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize #kelime bazında listeleyen nltk formatı: "word_tokenize"
from nltk.stem import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
translator = str.maketrans('','', string.punctuation) # noktalama işaretlerini silen objemiz. Kullanımı 18. satırda

text = " Bu durumun en ilginç sonucu, meditasyonun neden zihnin gevşeyip rahatlaması konusunda işlevsel olduğunu açıklama potansiyeline sahip olmasıdır. Meditasyon yapanlar, 'om' sözcüğünü çok iyi bilirler. Gözleri kapatıp, gevşeyip, bu sözcüğü uzun uzun tekrarlarlar. İşte 'om' sözcüğüne odaklanıp bunu tekrar ettiklerinde, semantik doygunluğa erişirler ve 'om' sözcüğü anlamını yitirerek birey 'şu an'a odaklanabilir. Bu durum, düşüncelerin temizlenmesini ve olumsuz düşüncelerden arınmayı sağlar. Bazı meditasyon tekniklerinde, olumsuz sözcükler (küfür ve hakaretler gibi) 45 saniye gibi sürelerce tekrar edilirler. Bu sayede sözcüklerin nötrleşmesi ve anlamlarını yitirmesi hedeflenir. Bu, yaygın olarak kabul gören bir psikolojik tedavi yöntemi olmasa da, bazı insanların rahatsız oldukları sıfatların ('şişko' ya da 'açgözlü' gibi) psikolojik olarak yıkıcı etkisinden arınmak için bu tür yöntemlere başvurulabilir. Olgunun ilginç sonuçlarından birisiyse, eğitim alanında gözükmektedir. Birçok okul, çeşitli temel bilgileri tekrar tekrar söyleterek ezberletmeyi hedefler ('2 kere 2, 4 eder' gibi). İnsanlar çok sayıda tekrarın ezberlemek için iyi bir yol olduğuna inanırlar. Halbuki 1962 senesinde Jakobovits ve Lambert tarafından üniversite öğrencileri arasında yapılan bir araştırma, çok sayıda yapılan tekrarın semantik doygunluğa erişilmesine neden olduğunu ve bu nedenle kelimelerin (ve öğrenilmeye çalışılan şeyin) anlamını yitirdiğini göstermiştir. Bu konu hakkında sayfalarca yazı yazılabilir ve birçok da akademik makale yayınlanmıştır. Burada kısa bir özet vermeye çalıştık; ancak merak edenler kaynaklarımızdan daha fazla bilgi alabilirler."
dic = dict() #boş sözlük yapısı

text = text.lower() #Hepsini küçük hale getirdim.
text = re.sub(r'\d+', '', text) # sanırım burada sayıları sildim emin değilim unuttum fonksiyonu
text = text.strip() #Birden fazla yan yana boşluk varsa sildim. Örn: "a  a" => "a a" oldu
text = text.translate(translator) #noktalama işaretlerini sildim.
tokens = word_tokenize(text) #kelime kelime haline geldi tüm text

for i in range(0,len(tokens)):
    if tokens[i] in list(dic):
        value = dic[tokens[i]] + 1
        dic[tokens[i]] = value
    else:
        dic[tokens[i]] = 1
print(dic)
sorted_dict = sorted(dic.items(),  key=lambda kv:(kv[1], kv[0]), reverse=True)
sorted_dict = collections.OrderedDict(sorted_dict)
print(sorted_dict)   
print(list(sorted_dict)[0]+": "+str(list(sorted_dict.values())[0])+" kez metin içerisinde geçmiştir.")
