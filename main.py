from repositories.contacts_repository import get_contacts
from services.zapi_service import send_message


contacts = get_contacts(limit=1)
print(contacts)
for contact in contacts:
    name = contact["name"]
    number = contact["number"]

    if send_message(number, name):
        print(f"Mensagem enviada para {name} ({number})")
    else:
        print(f"Falha ao enviar mensagem para {name} ({number})")
