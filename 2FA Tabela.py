import smtplib
import random
import string
import uuid

# Função para gerar um código de verificação aleatório
def generate_verification_code():
    codigo = random.randint(56545, 988928)
    return codigo
    
def main(): 
    try:        
        # Configurações do servidor de e-mail
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        email_sender = "luizc.dinani@gmail.com"
        email_password = "yhpenuengyzdyohv"
    
        # Endereço de e-mail do destinatário
        authorized_emails = ["beatriz.cardoso1220@gmail.com"]
        email_recipient = input("Qual é o seu email?")
    
        while email_recipient not in authorized_emails:
            print("Email não autorizado")
            email_recipient = input("Qual é o seu email?")
    
        # Gera um código de verificação
        verification_code = generate_verification_code()
    
        # Configurações do e-mail
        subject = "Código de Verificação 2FA"
        body = f"Seu código de verificação é: {verification_code}"
        message = f"Codigo 2FA é {verification_code}"
    
    # Envia o e-mail
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email_sender, email_password)
        server.sendmail(email_sender, email_recipient, message.encode())
        print("E-mail enviado com sucesso!")
        # Agora você pode comparar o código inserido pelo usuário com o código gerado
        codigoCerto = False
        while (not codigoCerto):
            user_input = input("Insira o código de verificação: ")
            if user_input == str(verification_code):
                print("Código correto. Acesso permitido.")
                print("Clientes Anonimizados: https://docs.google.com/spreadsheets/d/17YOVJR--2xMkAtDlJnpe_ZoiW-ivZuc8yH1PFVdv59Y/edit?usp=sharing")
                codigoCerto = True
            else:
                print("Código incorreto. Acesso negado.")
    except Exception as e:
        print("Erro ao enviar e-mail:", e)
    finally:
        server.quit()
    
main()