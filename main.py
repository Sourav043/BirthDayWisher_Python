import pandas as pd
import datetime
import smtplib
# import os
# os.chdir(r"C:\Users\sourav sarkar\Desktop\pythonn\birthday_wisher")
# os.mkdir("testing")

# Enter your authentication details
GMAIL_ID = ****** #Enter Your Email Id
GMAIL_PSWD = ****** # Enter Your Password


def sendEmail(to,sub,msg) :
    print(f"Email {to} , {sub} , {msg}")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(GMAIL_ID, GMAIL_PSWD)
    s.sendmail(GMAIL_ID, to, f"Subject: {sub}\n\n{msg}")
    s.quit()

if __name__ == "__main__":
    x=input("number")
    df = pd.read_excel("data_file.xlsx")
    #print(df)

    today = datetime.datetime.now().strftime("%d-%m")
    yearNow = datetime.datetime.now().strftime("%Y")
    #print(today)
    writeInd= []

    for index,item in df.iterrows():
        bday = item['Birthday'].strftime("%d-%m")
        if(today == bday) and yearNow not in str(item['Year']):
            sendEmail(item['Email'],"Sourav",item['Dialouge'])
            writeInd.append(index)

    if (writeInd!=0) :            
        for i in writeInd :
            yr = df.loc[i,'Year']
            df.loc[i,'Year']=str(yr) + ', '+str(yearNow)
            print(yr)
        df.to_excel('data_file.xlsx',index=False)    
