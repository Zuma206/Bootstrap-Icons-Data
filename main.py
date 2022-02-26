from requests import get
from bs4 import BeautifulSoup
from json import dump

dump(
	{
		e.text.replace('\n', '').replace('-', ' ').capitalize()
		:
		'<i class="bi bi-'+e.text.replace("\n", "")+'"></i>'
		for e in BeautifulSoup(
			get(
				'https://icons.getbootstrap.com'
			).text,
			'html.parser'
		).find_all(attrs={
			'class':'d-block text-dark text-decoration-none'
		})
	},
	open('data.json', 'w'),
	indent=1
)