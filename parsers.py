from html.parser import HTMLParser
import re

class dados_perfil_uri(HTMLParser):
		
	def __init__(self):
		HTMLParser.__init__(self)
		self.usuario_encontrado = False
		self.dados_encontrados = False
		self.usuario = ''
		self.dados_perfil = ''
 
	def handle_starttag(self, tag, atributos):      
		if tag == 'ul' or tag == 'div':
			for atributo, valor in atributos:
				if atributo == 'class':
					if valor == 'pb-usuario':
						self.usuario_encontrado = True
					elif valor == 'pb-information':           
						self.dados_encontrados = True 
 
	def handle_endtag(self, tag):
		if self.usuario_encontrado and tag == 'div':
			self.usuario_encontrado = False
			self.usuario = re.sub('[ \n]', '', self.usuario)
		elif self.dados_encontrados and tag == 'ul':
			self.dados_encontrados = False
 
	def handle_data(self, dados):
		if self.usuario_encontrado:
			self.usuario += dados
		elif self.dados_encontrados:
			self.dados_perfil += dados
            
	def formatar_dados_perfil(self):
		dados = re.sub('[ ]', '', self.dados_perfil)
		dados = [i for i in dados.split('\\n') if i != '']
		dados_formatados = {}
		dados_formatados[self.usuario] = {}
		for i in range(0, len(dados), 2):
			try:
				dados_formatados[self.usuario][dados[i]] = dados[i+1]
			except:
				pass
		return dados_formatados            
             
	def obter_dados_perfil(self):
		return self.formatar_dados_perfil()
