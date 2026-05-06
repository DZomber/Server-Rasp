import bs4
import requests

#resultado = requests.get('https://escueladirecta-blog.blogspot.com/2024/07/por-que-se-utiliza-python-en-ciencia-de.html')
resultado = requests.get('https://es.wikihow.com/calentar-tus-manos')
#print(resultado.text)

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
#print(sopa.select('title')[0].get_text()) # -> quitar las etiquetas
#print(sopa.select('p')) -> parrafo
#columna_lateral = sopa.select('.post-body p')
#for p in columna_lateral:
#    print(p.getText())

imagenes = sopa.select('img')[50]['src']
imagen_curso = requests.get(imagenes)
f = open('mi_imagen.jpg', 'wb')
f.write(imagen_curso.content)
f.close()
