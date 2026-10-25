# pauk.paris

Le site de Pauk (Paul Brunstein-Compard), humoriste : stand-up, impro musicale, cours.

Site statique : de simples fichiers HTML, une feuille de style et un petit script. Aucun logiciel à installer, aucun abonnement.

## Les fichiers

| Fichier | Page |
|---|---|
| `index.html` | Accueil |
| `sur-scene.html` | Dates, seul-en-scène L'Art de rater, spectacles passés |
| `videos.html` | Court métrage L'Art de rater, extraits, TV |
| `enseignement.html` | Cours particuliers de stand-up, parcours, stages et ateliers |
| `presse.html` | Bios à copier, photos HD, revue de presse |
| `contact.html` | Adresse unique, sujets, réseaux |
| `mentions-legales.html` | Mentions légales (obligatoires en France) |
| `assets/style.css` | Couleurs, polices, mise en page (ordinateur et téléphone) |
| `assets/site.js` | Menu mobile, masquage automatique des dates passées, bouton « Copier » |
| `assets/pull.svg`, `assets/pull-lisere.svg` | Motif tricoté d'après le pull fétiche de Pauk |
| `assets/img/` | Photos (pour l'instant : l'affiche de L'Art de rater) |
| `outils/pull.py` | Programme qui dessine le motif du pull |

## Le motif du pull

Le motif jacquard vient du pull que Paul porte sur l'affiche de *L'Art de rater* : losanges rouges concentriques, croix ocre, rangs de picots et dents de scie, dessinés maille par maille. Il apparaît en grande bande sous le titre de l'accueil, et en liseré sous l'en-tête de chaque page et au-dessus du pied de page.

Pour changer une couleur ou le dessin, modifier `outils/pull.py` puis, depuis le dossier `outils` :

```
python pull.py ../assets/pull.svg
python pull.py ../assets/pull-lisere.svg lisere
```

## Les photos

Dans `assets/img/` : une version web (1600 px) de chaque photo, et dans `assets/img/hd/` une version haute définition (2400 px) que la page Presse propose aux journalistes. Les métadonnées (lieu GPS, appareil) ont été retirées.

Pour ajouter une photo, la redimensionner aux mêmes tailles, la déposer dans ces deux dossiers et copier une ligne `<figure>` de `presse.html`.

## Ce qui reste à compléter

Tout ce qui est à compléter apparaît sur le site **hachuré en rose**. Pour les retrouver dans le code, chercher `todo`. Une fois l'élément rempli, retirer `todo` de la classe.

- [ ] Accord des autres comédiens visibles sur la photo FMR Académie (`fmr-academie-avignon-2026.jpg`, pages Sur scène et Presse).
- [ ] Affiche de L'Art de rater en haute définition (celle du site ne fait que 500 px de large).
- [ ] Créer l'adresse **contact@pauk.paris** chez le bureau d'enregistrement.
- [ ] Lien de la chaîne YouTube.
- [ ] Court métrage L'Art de rater : durée, année, équipe, lien de visionnage ou bande-annonce.
- [ ] Passage sur Comédie+ : émission, date, extrait.
- [ ] Un extrait de stand-up.
- [ ] Liens directs de billetterie pour Méchant.e, FMR Académie et Bon Camarade (ils renvoient pour l'instant vers la fiche Offi de Paul).
- [ ] Fréquence des passages au Poulet Comedy Club.
- [ ] Cours particuliers : durée, rythme et tarifs des séances.
- [ ] Formats des stages et ateliers (page Enseignement) : à valider par Paul.
- [ ] Hébergeur et éventuel SIRET dans les mentions légales.

### À faire relire par Paul

Ces textes viennent de sources publiques (Offi, BilletRéduc, franceinfo, archives HAL), de l'affiche et de la description fournie :

- les deux biographies (page Presse) ;
- le contenu des cours particuliers (page Enseignement) ;
- la mention de son mémoire universitaire sur le Madame Sarfati Comedy Club (page Enseignement) ;
- les stages aux Ateliers Comédie (page Enseignement) ;
- l'idée que *L'Art de rater* est le même spectacle que *Pauk, le one-man show presque musical* joué au Lieu (page Sur scène).

## Ajouter une date

Dans `sur-scene.html` (et `index.html` pour les 3 ou 4 prochaines), copier un bloc `<li>` de la setlist :

```html
<li data-end="2027-03-15">
  <span class="when">15 mars 2027</span>
  <span class="what">Nom du spectacle<small>Salle, ville</small></span>
  <span class="side"><span class="tag">Stand-up</span><a class="go" href="LIEN-BILLETTERIE" target="_blank" rel="noopener">Réserver →</a></span>
</li>
```

`data-end` est la date de dernière représentation, au format année-mois-jour. Le lendemain, la ligne disparaît toute seule du site.

## Nom de domaine

Domaine principal : **pauk.paris**. Domaine secondaire conseillé : **paulbrunsteincompard.fr**, redirigé vers pauk.paris, pour ceux qui cherchent son nom civil. Les deux étaient libres le 25 octobre 2026.

- Réserver les deux au nom de Paul, chez un bureau d'enregistrement qui gère le `.paris` (par exemple OVH), et activer le renouvellement automatique.
- Comparer le prix de la première année et celui du renouvellement : les noms courts sont parfois vendus plus cher.
- Créer l'adresse `contact@pauk.paris` chez le même bureau d'enregistrement.

## Mettre en ligne (gratuit)

Le code est sur GitHub. Le plus simple est de relier le dépôt à Netlify ou Cloudflare Pages : chaque modification enregistrée sur GitHub met le site à jour toute seule.

1. Créer un compte sur [Netlify](https://app.netlify.com) ou [Cloudflare Pages](https://pages.cloudflare.com), en se connectant avec GitHub.
2. Choisir « Importer un projet depuis GitHub », puis le dépôt `pauk.paris`. Aucune commande de construction, dossier de publication : la racine du dépôt.
3. Relier le nom de domaine (rubrique « Domain management » ou « Custom domains ») : `pauk.paris` en principal, `paulbrunsteincompard.fr` en redirection. Le certificat HTTPS est fourni automatiquement.
4. Pour une mise à jour : modifier les fichiers directement sur GitHub (bouton crayon) ou avec Claude, puis enregistrer.
