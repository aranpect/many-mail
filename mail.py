#自分のメールアドレスを入れる
x="xxxx@.gmailcom"

#自分のgoogleアカウントのパスワード
y="****"

#送りたい相手を指定
z="xxxx@gmail.com"

#送りたいメールの要件
a="こんばんは"

#送りたい内容を指定
b="こんばんは！元気ですか！？"

for i in range():
  import smtplib, ssl
  from email.mime.text import MIMEText

  gmail_account = x
  gmail_password = y
  mail_to = z

  subject = a
  body = b
  msg = MIMEText(body, "html")
  msg["Subject"] = subject
  msg["To"] = mail_to
  msg["From"] = gmail_account

  server = smtplib.SMTP_SSL("smtp.gmail.com", 465,
      context=ssl.create_default_context())
  server.login(gmail_account, gmail_password)
  server.send_message(msg) 
  print("成功")
