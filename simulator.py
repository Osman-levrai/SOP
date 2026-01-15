import heapq
from events import Event


class Simulator:
    def __init__(self):
        """
        Initialise le simulateur à événements discrets.
        """
        self.clock = 0.0        # Horloge globale (temps logique)
        self.events = []        # File de priorité (min-heap) pour les événements
        self.processes = {}     # Registre pour accéder aux processus par leur ID

    def register_process(self, process):
        """
        Enregistre un processus dans le simulateur.
        """
        self.processes[process.pid] = process

    def get_process(self, pid):
        """
        Récupère un objet processus par son ID (utile pour l'envoi de messages).
        """
        return self.processes.get(pid)

    def schedule(self, delay, receiver, action, params=None):
        """
        Programme un événement futur.
        
        :param delay: Le temps d'attente avant l'exécution (simule latence réseau ou calcul).
        :param receiver: L'objet Process qui subira l'action.
        :param action: La méthode à appeler (ex: receiver.receive_message).
        :param params: Les paramètres à passer à la méthode (ex: le Message).
        """
        trigger_time = self.clock + delay
        
        # On crée l'événement (en utilisant la classe Event définie précédemment)
        # Note: Assurez-vous que la classe Event est importée ou définie dans le même fichier
        event = Event(trigger_time, receiver, action, params)
        
        # On l'ajoute au tas. heapq maintient l'ordre croissant des timestamps.
        heapq.heappush(self.events, event)

    def run(self):
        """
        Boucle principale de la simulation.
        Traite les événements un par un jusqu'à ce que la file soit vide.
        """
        print(f"--- Démarrage de la simulation à t={self.clock} ---")
        
        while self.events:
            # 1. Extraire l'événement avec le plus petit timestamp (le plus tôt)
            current_event = heapq.heappop(self.events)
            
            # 2. Avancer l'horloge globale au temps de cet événement
            # C'est ce qui définit le "Discrete Event Model" 
            self.clock = current_event.timestamp
            
            # 3. Exécuter l'action associée
            # On gère le cas où il y a des paramètres ou non
            if current_event.params is not None:
                current_event.action(current_event.params)
            else:
                current_event.action()

        print(f"--- Fin de la simulation à t={self.clock} ---")