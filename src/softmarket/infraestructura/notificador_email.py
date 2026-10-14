"""Adaptador de notificación por correo electrónico."""
import smtplib
from email.message import EmailMessage

from softmarket.dominio.cliente import Cliente

REMITENTE = "noreply@softmarket.dev"
ASUNTO = "Bienvenido a SoftMarket"


class NotificadorEmail:
    """Implementa el puerto ServicioNotificacion usando SMTP."""

    def __init__(self, servidor_smtp: str, puerto: int = 587) -> None:
        self._servidor = servidor_smtp
        self._puerto = puerto

    def notificar(self, cliente: Cliente) -> None:
        """Envía el correo de bienvenida al cliente."""
        mensaje = EmailMessage()
        mensaje["From"] = REMITENTE
        mensaje["To"] = cliente.email
        mensaje["Subject"] = ASUNTO
        mensaje.set_content(
            "Hola " + cliente.nombre + ", su cuenta fue creada correctamente."
        )
        with smtplib.SMTP(self._servidor, self._puerto) as smtp:
            smtp.send_message(mensaje)
