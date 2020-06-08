import re, pyperclip

phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?
	(\s|-|\.)?
	(\d{3})
	(\s|-|\.)
	(\d{4})
	(\s*(ext|x|ext.)\s*(\d{2,5}))?
	)''', re.VERBOSE)

emailRegex = re.compile(r'''(
	[a-z A-z 0-9 ._%+-]))+
	@
	[a-z A-Z 0-9.-]+
	(\.[a-zA-Z]{2,4})
	)''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
	print(groups)
