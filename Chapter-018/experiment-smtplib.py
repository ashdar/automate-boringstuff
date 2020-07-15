import smtplib
print("Open a connection.")
smtpObj = smtplib.SMTP_SSL('smtp.verizon.net', 465)
print("ehlo.")
smtpObj.ehlo()

# print("Start TLS.")
# smtpObj.starttls()
# smtplib.SMTPNotSupportedError: STARTTLS extension not supported by server.
# doesn't .SMTP_SSL() take care of TLS?

print("Quit.")
smtpObj.quit()
print("Done.")