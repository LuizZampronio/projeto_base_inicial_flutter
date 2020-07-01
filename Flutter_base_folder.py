import os
import os.path

currentDir = str(os.getcwd())


#user's input
pasta = str(input(print('Digite o nome da nova pasta: ')))

#check if the folder already exists
if os.path.exists(pasta):
	os.chdir(currentDir + '/' + pasta)
else:
	os.mkdir(pasta)
	os.chdir(currentDir + '/' + pasta)

while True:

	flutterName = str(input(print('Digite o nome do projeto Flutter: ')))

	if os.path.exists(currentDir + '/' + pasta + '/' + flutterName):
		print('Project already exists')
	else:
		os.system('flutter create' + ' ' + flutterName)
		break

#change to the Project directory
os.chdir(currentDir + '/' + pasta + '/' + flutterName)

#open VsCode
os.system('code .')