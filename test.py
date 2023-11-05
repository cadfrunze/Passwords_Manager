from datetime import datetime

data_editare = datetime.now().strftime("Data: %d/%m/%Y | Ora: %H:%M:%S")

with open('./work_log.txt','a') as fisier:
    fisier.writelines('\n' + data_editare)
