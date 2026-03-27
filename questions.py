import random

questions = [
    {
        "text": "De combien de degrés de température suffit-il pour que les coraux blanchissent ?",
        "options": ["1–2 °C", "10–15 °C", "20–25 °C", "30 °C ou plus"],
        "answer": "1–2 °C"
    },
    {
        "text": "Quelle part de la chaleur excédentaire due au réchauffement climatique l’océan a-t-il absorbée ?",
        "options": ["Plus de 90%", "Environ 10%", "Autour de 50%", "Moins de 5%"],
        "answer": "Plus de 90%"
    },
    {
        "text": "De combien l’acidité de l’océan a-t-elle augmenté depuis la Révolution industrielle ?",
        "options": ["Environ 30%", "5%", "10%", "70%"],
        "answer": "Environ 30%"
    },
    {
        "text": "Quelle proportion de la Grande Barrière de corail a subi un blanchissement ces dernières décennies ?",
        "options": ["Plus de 90%", "10%", "25%", "50%"],
        "answer": "Plus de 90%"
    },
    {
        "text": "Quelle part de l’oxygène terrestre est produite par l’océan ?",
        "options": ["Environ 50%", "10%", "25%", "90%"],
        "answer": "Environ 50%"
    },
    {
        "text": "Quelle part du dioxyde de carbone excédentaire issu des activités humaines est absorbée par l’océan ?",
        "options": ["Environ 30%", "5%", "60%", "90%"],
        "answer": "Environ 30%"
    },
    {
        "text": "Quelle élévation du niveau de la mer est attendue d’ici 2100 si le réchauffement continue ?",
        "options": ["Jusqu’à 1 mètre", "10 centimètres", "5 mètres", "Aucun changement"],
        "answer": "Jusqu’à 1 mètre"
    },
    {
        "text": "À quelle vitesse les océans se réchauffent-ils aujourd’hui par rapport aux 50 dernières années ?",
        "options": ["Environ deux fois plus vite", "Plus lentement qu’avant", "Au même rythme", "Dix fois plus vite"],
        "answer": "Environ deux fois plus vite"
    },
    {
        "text": "Combien d’espèces marines dépendent des récifs coralliens, menacés par le réchauffement ?",
        "options": ["Environ 25% de toutes les espèces marines", "5%", "50%", "75%"],
        "answer": "Environ 25% de toutes les espèces marines"
    },
    {
        "text": "Quelle quantité de glace l’Arctique a-t-il perdu en été par rapport aux années 1980 ?",
        "options": ["Environ 75%", "10%", "25%", "50%"],
        "answer": "Environ 75%"
    }
]

# Mélanger les options de chaque question
for q in questions:
    random.shuffle(q["options"])
