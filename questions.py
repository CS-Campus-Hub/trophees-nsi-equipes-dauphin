import random

questions = [
    {
        "text": "De combien de degrés de température suffit-il pour que les coraux blanchissent ?",
        "options": ["1–2 °C", "10–15 °C", "20–25 °C"],
        "answer": "1–2 °C"
    },
    {
        "text": "Quelle part de la chaleur excédentaire due au réchauffement climatique l’océan a-t-il absorbée ?",
        "options": ["Plus de 90%", "10%", "50%"],
        "answer": "Plus de 90%"
    },
    {
        "text": "De combien l’acidité de l’océan a-t-elle augmenté depuis la Révolution industrielle ?",
        "options": ["30%", "5%", "10%"],
        "answer": "30%"
    },
    {
        "text": "Quelle proportion de la Grande Barrière de corail a subi un blanchissement ces dernières décennies ?",
        "options": ["Plus de 90%", "25%", "50%"],
        "answer": "Plus de 90%"
    },
    {
        "text": "Quelle part de l’oxygène terrestre est produite par l’océan ?",
        "options": ["50%", "25%", "90%"],
        "answer": "50%"
    },
    {
        "text": "Quelle part du dioxyde de carbone excédentaire issu des activités humaines est absorbée par l’océan ?",
        "options": ["30%", "60%", "90%"],
        "answer": "30%"
    },
    {
        "text": "Quelle élévation du niveau de la mer est attendue d’ici 2100 si le réchauffement continue ?",
        "options": ["1 mètre", "10 centimètres", "5 mètres"],
        "answer": "1 mètre"
    },
    {
        "text": "À quelle vitesse les océans se réchauffent-ils aujourd’hui par rapport aux 50 dernières années ?",
        "options": ["2x plus vite", "Même rythme", "10x plus vite"],
        "answer": "2x plus vite"
    },
    {
        "text": "Combien d’espèces marines dépendent des récifs coralliens, menacés par le réchauffement ?",
        "options": ["25%", "50%", "75%"],
        "answer": "25%"
    },
    {
        "text": "Quelle quantité de glace l’Arctique a-t-il perdu en été par rapport aux années 1980 ?",
        "options": ["75%", "25%", "50%"],
        "answer": "75%"
    }
]

for q in questions:
    random.shuffle(q["options"])