import zipfile, os, shutil

folderToSave = "C:\\Users\\admin\\Desktop"

def backupToZip(folder):
	cwd = os.getcwd()
	folder = os.path.abspath(folder)
	num = 1
	while True:
		zipFileName = os.path.basename(folder) + '_' + str(num) + '.zip'
		if not os.path.exists(zipFileName):
			break
		num = num + 1

	print("File to create: %s" % (zipFileName))
	backupZip = zipfile.ZipFile(zipFileName, 'w')
	#обход всего дерева папки
	for foldername, subfolders, filenames in os.walk(folder):
		print('Adding files from %s folder' % (foldername))
		backupZip.write(foldername)
		for filename in filenames:
			newBase = os.path.basename(folder) + '_'
			if filename.endswith('.zip') and filename.startswith(newBase):
				continue
			backupZip.write(os.path.join(foldername, filename), compress_type=ZIP_DEFLATED)
	backupZip.close()
	print('Finished')
	shutil.move(os.path.join(cwd, zipFileName), folderToSave)

folder = input("Write down a full path to the folder you want to zip >> ")

backupToZip(folder)  