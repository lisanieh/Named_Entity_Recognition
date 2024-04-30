import requests
import json

def request(sent, token):
    res = requests.post("http://140.116.245.157:2001", data={"data":sent, "token":token})
    if res.status_code == 200:
        return json.loads(res.text)
    else:
        return None 


if __name__ == "__main__":
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJleHAiOjE3MjUxMDE0NTAsImF1ZCI6IndtbWtzLmNzaWUuZWR1LnR3IiwidmVyIjowLjEsInNjb3BlcyI6IjAiLCJzZXJ2aWNlX2lkIjoiMSIsInVzZXJfaWQiOiI0OTEiLCJpc3MiOiJKV1QiLCJpZCI6NzAyLCJpYXQiOjE3MDk1NDk0NTAsIm5iZiI6MTcwOTU0OTQ1MCwic3ViIjoiIn0.SAIGjMEEOKOycRXibQxuGZsAW9aLpqCPPPMHy6zyipBQRF4qQATuYNKzMxOe62IyNKzdY6GIl4druL72_xc4l2YBH6qe4UT8QMeHW3aPCDx454XBUrLso6IxP6dwl58qLU3btsCtHoglCEEwEaCmH9xemFRljEyTDt6wrL5p8aM" # Go 'WMMKS API' website to get your token
    sent = input("請輸入文章：")
    r = request(sent, token)
    # print("word : ",r['ws'])
    # print("tag : ",r['pos'])
    # print("NER : ",r['ner'])
    
    #settings
    person = []
    location = []
    money = []
    time = []
    quantity = []
    money_list = ['元',"塊","圓","美金","歐元","日幣","美元","台幣"]
    
    # store pos tags
    pos_tag = []
    for i in r['pos'][0]:
        pos_tag.append(i)
        
    # categorize
    index = 0
    for tag in pos_tag:
        if(tag == 'Nb'):
            person.append(r['ws'][0][index])
        elif(tag == 'Nc'):
            location.append(r['ws'][0][index])
        elif(tag == 'Nd'):
            text = ""
            time.append(r['ws'][0][index])
        elif(tag == 'Neu'):
            text = r['ws'][0][index]
            if(index+1 < len(pos_tag)):
                if(r['ws'][0][index+1] in money_list):
                    text = text + r['ws'][0][index+1]
                    money.append(text)
                elif(r['pos'][0][index+1] == 'Nf'):
                    text = text + r['ws'][0][index+1]
                    quantity.append(text)
                else:
                    quantity.append(r['ws'][0][index])
        index += 1
    
    # output
    print('人：',person)
    print('地點：',location)
    print('金錢：',money)
    print('時間：',time)
    print('數值：',quantity)
