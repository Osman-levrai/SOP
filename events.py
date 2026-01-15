class Event:
    def __init__(self, timestamp, process, action, params=None):
        """
        Définit un événement discret dans la simulation.
        
        :param timestamp: Le temps logique auquel l'événement doit se produire.
        :param process: L'objet Processus concerné par cet événement.
        :param action: La méthode du processus à exécuter (ex: process.receive_message).
        :param params: Les arguments à passer à la méthode 'action'.
        """
        self.timestamp = timestamp
        self.process = process
        self.action = action
        self.params = params

    def __lt__(self, other):
        """
        Comparaison pour le tri dans la file de priorité (heapq).
        Un événement est 'plus petit' (prioritaire) s'il a un timestamp plus petit.
        """
        return self.timestamp < other.timestamp

    def __repr__(self):
        return f"[Time {self.timestamp}] Event for {self.process.pid}"