from html.parser import HTMLParser
import re

class uri_profile_information(HTMLParser):
		
	def __init__(self):
		HTMLParser.__init__(self)
		self.info_found = False
		self.profile_data = ''
 
	def handle_starttag(self, tag, attrs):      
		if tag == 'ul':
			for attr, value in attrs:
				if attr == 'class' and value == 'pb-information':           
					self.info_found = True 
 
	def handle_endtag(self, tag):
		if self.info_found and tag == 'ul':
			self.info_found = False
 
	def handle_data(self, data):
		if self.info_found:
			self.profile_data += data
            
	def format_profile_data(self):
		data = re.sub('[ ]', '', self.profile_data)
		data = [i for i in data.split('\\n') if i != '']
		formated_data = {}
		for i in range(0, len(data), 2):
			try:
				formated_data[data[i]] = data[i+1]
			except:
				pass
		return formated_data            
             
	def get_profile_data(self):
		return self.format_profile_data()
