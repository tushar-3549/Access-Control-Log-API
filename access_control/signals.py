
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import AccessLog
import subprocess
from datetime import datetime

LOG_FILE = "system_events.log"

@receiver(post_save, sender=AccessLog)
def log_access_create(sender, instance, created, **kwargs):
    if created:
        status = "GRANTED" if instance.access_granted else "DENIED"
        log_line = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] - CREATE: Access log created for card {instance.card_id}. Status: {status}.\n"
        subprocess.run(['bash', '-c', f'echo "{log_line}" >> {LOG_FILE}'])

@receiver(post_delete, sender=AccessLog)
def log_access_delete(sender, instance, **kwargs):
    log_line = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] - DELETE: Access log (ID: {instance.id}) for card {instance.card_id} was deleted.\n"
    subprocess.run(['bash', '-c', f'echo "{log_line}" >> {LOG_FILE}'])
