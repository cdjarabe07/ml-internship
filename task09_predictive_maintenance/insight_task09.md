# Insight — Task 9 : Maintenance prédictive industrielle (Industry Level)

## Ce qu'on a cherché à savoir
Peut-on prédire qu'une machine industrielle va tomber en panne à partir de ses capteurs, en évitant de déclencher trop de fausses alertes coûteuses ?

## Ce qu'on a trouvé — un vrai compromis, pas une réponse unique

Deux modèles testés donnent deux résultats très différents, qui illustrent bien la tension centrale de cette tâche :

| Modèle | Fausses alertes (FDR) | Pannes détectées (Recall) |
|---|---|---|
| **Random Forest** | 12.2 % (peu de fausses alertes) | 53 % seulement |
| **XGBoost pondéré** | 28.4 % (beaucoup plus de fausses alertes) | 78 % |

**Aucun des deux n'est "le meilleur" dans l'absolu** — le choix dépend du coût réel dans l'usine : si arrêter la ligne de production pour rien coûte très cher, on préfère Random Forest (peu de fausses alertes, mais on rate presque une panne sur deux). Si une panne non détectée est catastrophique (sécurité, casse majeure), XGBoost devient préférable malgré ses fausses alertes plus fréquentes.

## Le facteur le plus révélateur : le couple (Torque)

**Le couple exercé sur la machine est le meilleur indicateur précoce de panne** — devant même l'usure de l'outil, qui est pourtant le facteur "intuitif" auquel on penserait en premier. La température (air ou process) et la vitesse de rotation sont nettement moins prédictives.

## Pourquoi on n'a pas utilisé les colonnes de détail des pannes (TWF, HDF, PWF...)

Point méthodologique important : ces colonnes indiquent **quel type** de panne s'est produit, mais elles ne sont connues qu'*après coup* — les utiliser comme variables d'entrée aurait été de la fuite de données (le modèle "trÍcherait" en utilisant une information qu'il n'aurait jamais en situation réelle, avant la panne).

## Sur le "Time-to-Failure"

Une estimation simple basée sur l'usure de l'outil au moment de la panne donne un R² de seulement 0.213 — **trop faible pour être fiable**. Ce n'est pas surprenant : ce dataset ne contient que des observations ponctuelles indépendantes, pas un historique continu de capteurs sur une même machine dans le temps. Un vrai modèle de durée de vie restante demanderait des données de série temporelle, absentes ici.

## À retenir
1. **Il n'y a pas de "bon" modèle sans connaître le coût métier** — le choix entre Random Forest et XGBoost dépend de ce qui coûte le plus cher : les fausses alertes ou les pannes ratées.
2. **Le couple est le signal le plus utile**, un point concret à remonter à une équipe de maintenance si elle devait prioriser quel capteur surveiller de près.
