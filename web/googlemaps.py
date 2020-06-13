import sys, webbrowser

if len(sys.argv) > 1:
	for i in range(1, len(sys.argv)):
		sys.argv[i] = sys.argv[i] + ',+'
	address = ''.join(sys.argv[1:])
	print(f"Cmd argunemts: {sys.argv[1:]}")
	print(f"address: {address}")
else:
	print("You have to write an address")

webbrowser.open('https://www.google.es/maps/place/' + address)