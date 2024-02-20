# Scraper pour twitter

## Note
Récupère les informations de twitter d'un utilisateur, d'une expression ou d'un hashtag pour une analyse ultérieure

## Installation

- Téléchargez python3 pour windows (Version stable le 16/02/2024: 3.11.8) selon votre architecture (généralement 64bit) à https://www.python.org/downloads/windows et suivez la procédure d'installation.

- Téléchargez le projet (bouton vert "Code" -> download zip -> extraire le fichier sur le bureau).

- Cliquez sur le point d'entrée du programme (ici: main.py).



## Usage

from ntscraper import Nitter

scraper = Nitter(log_level=1, skip_instance_check=False)

francetravail_tweets = scraper.get_tweets(*"FranceTravail"*, mode='user', number=10, instance=random_instance)

display_and_save_tweets_info(francetravail_tweets, "/home/user/francetravail_tweets")

```
Paramètres:
- term: terme de la recherche
- mode: term (default), user, hashtag
- number: nombre de tweets à scraper (default -1 unlimited).
```


## Example avec le compte officiel de FranceTravail
```
User: France Travail (ex-Pôle emploi) (@FranceTravail)
Date: Feb 19, 2024 · 7:50 AM UTC
Text: Lancement des Journées des métiers de l’#agriculture et du vivant ! 🌱  🗓️ 19 au 23 février 2024  + de 500 événements organisés avec l’@oselagri_anefa sur l’ensemble du #territoire ➡️ https://www.francetravail.org/accueil/communiques/2024/france-travail-et-lanefa-se-mobilisent-pour-lemploi-dans-lagriculture.html?type=article #LagriRecrute #AvecFranceTravail

Pictures:
 - https://pbs.twimg.com/media/GGry61WXoAAf_9h.jpg
Stats: Comments: 0, Retweets: 18, Quotes: 1, Likes: 19

--------------------------------------------------
User: France Travail Normandie (ex-Pôle emploi) (@FTravail_NDIE)
Date: Feb 20, 2024 · 10:31 AM UTC
Text: Aujourd'hui, @ThibautGuilluy directeur général @FranceTravail est en visite à la Mission locale du Havre !  Au programme :  Découverte d’actions locales innovantes, réflexion sur l'anticipation des besoins en compétences, et renforcement de la coopération pour l’#emploi.

Pictures:
 - https://pbs.twimg.com/media/GGxeJGlXEAAuFV1.jpg
 - https://pbs.twimg.com/media/GGxeJHlWEAAtmT7.jpg
 - https://pbs.twimg.com/media/GGxeJHOW4AA9Gk9.jpg
This is a retweet.
Stats: Comments: 0, Retweets: 4, Quotes: 0, Likes: 7

--------------------------------------------------
User: Apec_Etudes 🔎 (@Apec_Etudes)
Date: Feb 20, 2024 · 8:18 AM UTC
Text: Retrouvez notre publication sur les métiers #cadres porteurs en 2024 : https://corporate.apec.fr/home/nos-etudes/toutes-nos-etudes/les-metiers-cadres-porteurs-en-2024.html 🧵

Pictures:
 - https://pbs.twimg.com/media/GGxCfisWYAEPvJ9.jpg
This is a retweet.
Stats: Comments: 1, Retweets: 3, Quotes: 0, Likes: 1

--------------------------------------------------
User: France Travail (ex-Pôle emploi) (@FranceTravail)
Date: Feb 20, 2024 · 8:39 AM UTC
Text: L'#agriculture maintient une dynamique d’embauche importante sur l'ensemble du #territoire ! 🚀  + de 245 000 projets de #recrutement chaque année, selon notre enquête #BMO sur les besoins en main-d’œuvre des entreprises 🔎  cc @oselagri_anefa #LagriRecrute #AvecFranceTravail

Stats: Comments: 1, Retweets: 6, Quotes: 0, Likes: 7

--------------------------------------------------
User: France Travail (ex-Pôle emploi) (@FranceTravail)
Date: Feb 19, 2024 · 2:04 PM UTC
Text: Plusieurs leviers existent pour répondre aux besoins de #recrutement de la filière agricole. Parmi eux : la promotion des métiers auprès de toutes et tous 📣  De nombreux acteurs se mobilisent pour l'#emploi des ♀️ dans l'#agriculture ➡️ https://francetravail.org/accueil/actualites/2024/lagriculture-un-secteur-entre-defis-et-mutations.html?type=article #AvecFranceTravail

Pictures:
 - https://pbs.twimg.com/media/GGtIKzBXAAADcfb.jpg
Stats: Comments: 0, Retweets: 10, Quotes: 0, Likes: 15

--------------------------------------------------
User: France Travail (ex-Pôle emploi) (@FranceTravail)
Date: Feb 19, 2024 · 12:31 PM UTC
Text: En France, + de 25 000 personnes en situation de #handicap travaillent dans l’#agriculture 🌱  💡 C’est un secteur dynamique qui ouvre ses portes aux travailleurs handicapés, comme le présente @ID_LinfoDurable ➡️ https://www.linfodurable.fr/handicap-travailler-en-agriculture-avec-ses-differences-43783 #LagriRecrute #AvecFranceTravail #inclusion

Pictures:
 - https://pbs.twimg.com/media/GGszPnlWUAAYFlZ.jpg
Stats: Comments: 1, Retweets: 5, Quotes: 0, Likes: 12

--------------------------------------------------
User: France Travail (ex-Pôle emploi) (@FranceTravail)
Date: Feb 16, 2024 · 12:24 PM UTC
Text: Comment France Travail accompagne les entreprises ? 🤝  🎙️ Avec la préparation opérationnelle à l'emploi individuelle, France Travail propose une aide au financement de #formation avant l'embauche pour faciliter les #recrutements de l'entreprise Otis ➡️ https://francetravail.org/accueil/actualites/2024/nos-techniciens-sont-nos-premiers-ambassadeurs-aupres-de-nos-clients.html?type=article

Pictures:
 - https://pbs.twimg.com/media/GGdS5W_XMAAK8wQ.jpg
Stats: Comments: 2, Retweets: 11, Quotes: 2, Likes: 21

--------------------------------------------------
User: France Travail Nouvelle-Aquitaine (ex-Pôle emploi) (@FTravail_NA)
Date: Feb 16, 2024 · 8:40 AM UTC
Text: .@ThibautGuilluy est en visite à l'agence de #Bergerac. A la rencontre des conseillers, mais aussi des entreprises. La semaine dernière, l'opération "Je Teste un Métier" en #Dordogne et en #Corrèze a permis de lancer 550 #immersions, dont 30% pour les jeunes. #AvecFranceTravail

Pictures:
 - https://pbs.twimg.com/media/GGchBfCXwAAvyXy.jpg
This is a retweet.
Stats: Comments: 2, Retweets: 5, Quotes: 0, Likes: 20

--------------------------------------------------
User: Thibaut Guilluy (@ThibautGuilluy)
Date: Feb 15, 2024 · 1:53 PM UTC
Text: 🥇🥈🥉 Je suis supporter des #JOP de @Paris2024 et je suis fier de vous présenter les 18 athlètes de haut niveau soutenus par @FranceTravail ! Merci de porter haut les valeurs qui nous sont communes. Dernière ligne droite 💥 Nous sommes tous derrière vous ! #AvecFranceTravail

This is a retweet.
Stats: Comments: 4, Retweets: 42, Quotes: 2, Likes: 95

--------------------------------------------------
User: Fonds social européen + (@FSE_nat)
Date: Feb 15, 2024 · 2:33 PM UTC
Text: 🤓 Envie d'en apprendre davantage sur les programmes nationaux #FSE+ et #FTJ 🇪🇺 ? Découvrez notre synthèse en 4 pages sur notre site ➡️ https://fse.gouv.fr/sites/default/files/2024-02/Les%20Programmes%20nationaux%20FSE%2B%20%2522Emploi%2C%20Inclusion%2C%20Jeunesse%20et%20Comp%C3%A9tences%2522%20et%20FTJ%20%2522Emploi%20-%20Comp%C3%A9tences%2522%202021-2027.pdf #Emploi #Inclusion #Jeunesse #Compétences #Transition

Pictures:
 - https://pbs.twimg.com/media/GGYoaeFaAAAijoc.jpg
This is a retweet.
Stats: Comments: 0, Retweets: 7, Quotes: 0, Likes: 6

--------------------------------------------------
```
