# Gestion_Taches
une petite application de gestion de tâches avec un backend en Pyhton/Django (API) et une interface frontend en Svelte.
Fonctionnalités  :
- Ajouter, modifier, supprimer une tâche
- Marquer une tâche comme faite / à faire
- Filtrer les tâches (toutes / faites / à faire)
# Technologies utilisées
- **Backend** : Django (Python)
- **Frontend** : Svelte , javascript
- **Base de données** : SQLite
- **Version Python** :  3.12.6
- **Version Node.js** : 20.16.0

git clone https://github.com/eya-dhouib/Gestion_Taches.git

cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


cd frontend
npm install
npm run dev


