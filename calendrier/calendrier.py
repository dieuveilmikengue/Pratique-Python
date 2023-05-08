import calendar #Importer le module calendrier
from datetime import datetime #importer le moduleb datetime depuis datetime pour les dates

annee = datetime.now().year #On affecte l'année actuelle dans la variable annee
mois = datetime.now().month #On affecte le mois l'actuel dans la variable mois

print(calendar.month(annee, mois)) #On affiche le calendrier du mois actuel de cette année

print(calendar.calendar(annee)) #On affiche le calendrier de cette année