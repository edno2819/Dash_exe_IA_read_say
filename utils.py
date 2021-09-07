import csv

def consult_csv():
    configs={}
    gnore = [' ', '[', '#']
    with open('configs.txt', newline='', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='\n')
        for row in spamreader:
            if row!=[]:
                if row[0][0] not in gnore:
                    dic = row[0].split('=')
                    value = dic[1].strip().split(',')

                    configs[dic[0].strip()] = '' if len(dic)<2 else value
    return configs