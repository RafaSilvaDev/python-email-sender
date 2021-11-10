#email quando uma turma começar a preencher
#email depois de um certo período, para retornar quantos porcentos de alunos já preencheram a pesquisa

# https://youtu.be/umvzsQLZYD4

# email de app: securesally@gmail.com
# senha de app: umpjwfvjhdlxpcnd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

host = 'smtp.gmail.com'
port = '587'
login = 'rafabdasilvadev@gmail.com'
senha = 'umpjwfvjhdlxpcnd'
reciever = 'seuemail@gmail.com'

server = smtplib.SMTP(host, port)
server.starttls()
server.login(login, senha)

# cpnstruindo email tipo MIME
corpo = """\
    <div style="display: flex; align-items: center; justify-content: center; background-color: brown;">
        <h1 style="color: #fff; padding: 10px;">🚨⚠ ATENÇÃO ATENÇÃO ⚠🚨</h1>
    </div>
    <br />
    <h2>SEU TELEFONE CELULAR ACABA DE SER CLONADO!! 📱🚫</h2>
    <h4>Execute as etapas a seguir para manter seu dispositivo seguro:</h4>
    <br />
    <hr>
    < style="padding: 15px;">
        <p>1 - Abra seu WhatsApp</p>
        <p>2 - Procure pelo PV de Rafael Barbosa da Silva</p>
        <p>3 - Digite "SOCORRO! eu desejo desbloquear meu dispositivo agora!"</p>
        <p>4 - Envie a mensagem</p>
        <p>5 - Aguarde uma resposta</p>
    </div>
    <hr>
    <p>Após realizar esses procedimentos, pode ter a certeza de que está seguro(a)! 🤝🤝</p>
"""

msg = MIMEMultipart()
msg['From'] = login
msg['To'] = login
msg['Subject'] = 'ESTE EMAIL É MUITO IMPORTANTE'
msg.attach(MIMEText(corpo, 'html'))

server.sendmail(login, reciever, msg.as_string())

print('email enviado!')