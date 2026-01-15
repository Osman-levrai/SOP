class MessageType:
    APP = "APPLICATION"  # Message normal de l'application [cite: 24]
    MARKER = "MARKER"    # Message de contrôle pour le snapshot [cite: 25]

class Message:
    def __init__(self, sender_pid, content, msg_type=MessageType.APP):
        """
        Représente un message envoyé d'un processus à un autre.
        
        :param sender_pid: L'ID du processus expéditeur (ex: "P1").
                           Nécessaire pour savoir quel canal enregistrer[cite: 30].
        :param content: Le contenu du message (ex: "M1", "M2") ou None pour un Marker.
        :param msg_type: Le type de message (APP ou MARKER).
        """
        self.sender_pid = sender_pid
        self.content = content
        self.msg_type = msg_type

    def __repr__(self):
        # Format d'affichage utile pour le débogage et le rapport final
        if self.msg_type == MessageType.MARKER:
            return f"<Marker from {self.sender_pid}>"
        return f"<Msg '{self.content}' from {self.sender_pid}>"