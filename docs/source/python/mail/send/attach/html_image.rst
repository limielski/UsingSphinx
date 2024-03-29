
.. _HTMLzobrazkiem:

html z obrazkiem
----------------

.. code-block:: python
   :linenos:

   import smtplib
   from email.mime.image import MIMEImage
   from email.mime.multipart import MIMEMultipart
   from email.mime.text import MIMEText

   from conf import sender, password, receiver, smtp_server, smtpTLS_port


   def send_email_with_image(sender_email, sender_password, receiver_email, subject_email, body_mail, image_file):
       # Tworzenie wiadomości e-mail
       message = MIMEMultipart('related')
       message['From'] = sender_email
       message['To'] = receiver_email
       message['Subject'] = subject_email

       # Tworzenie treści HTML z obrazkiem
       html_content = f'''
       <html>
         <body>
           <p>{body_mail}</p>
           <img src="cid:image1" style="width:100px;">
         </body>
       </html>
       '''

       html = MIMEText(html_content, 'html')
       message.attach(html)

       # Otwarcie obrazka i odczytanie jego zawartości
       with open(image_file, 'rb') as image_file:
           image_data = image_file.read()

       # Dodanie obrazka jako załącznika z identyfikatorem CID

       image = MIMEImage(image_data)
       message.attach(image)

       image.add_header('Content-ID', '<image1>')

       # Logowanie i wysyłanie wiadomości. smtpTLS_port = 587
       with smtplib.SMTP(smtp_server, smtpTLS_port) as server:
           server.starttls()
           server.login(sender_email, sender_password)
           server.sendmail(sender_email, receiver_email, message.as_string())


   if __name__ == "__main__":
       subject = 'Prosty HTML z obrazkiem'
       body = 'Witaj! Oto prosty e-mail HTML z obrazkiem.'
       image_path = 'picture.jpg'  # Ścieżka do obrazka

       send_email_with_image(sender, password, receiver, subject, body, image_path)
