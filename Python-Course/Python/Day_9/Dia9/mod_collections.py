#from collections import Counter
#from collections import defaultdict
#from collections import namedtuple
from collections import *

numeros =[8,6,9,5,4,5,5,5,5,8,7,4,5,4,4]
print(Counter(numeros))
print(Counter('mississipi'))
frase = 'al pan pan y al vino vino'
print(Counter(frase.split()))

serie = Counter([1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,4,4,4,4])
print(serie.most_common())
print(serie.most_common(3))
print(list(serie))
print('*'*25)
mi_dic = defaultdict(lambda: 'nada')
mi_dic ['uno'] = 'verde'
print(mi_dic['dos'])

print(mi_dic)
print('*'*25)
Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
ariel = Persona('Ariel', 1.76, 79)
print(ariel[2])