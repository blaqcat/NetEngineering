#Creating an SMTP Server

from smtpd import SMTPServer

def main():
    localaddr = ('localhost', 8080)
    remoteaddr = ('mail.example.com', 8080)

    server = SMTPServer(localaddr, remoteaddr, data_size_limit=33554432,
                    map=None, enable_SMTPUTF8=False, decode_data=False)

if __name__ == '__main__':
    main()
