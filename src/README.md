# Python Calculator

Projet personnel réalisé en Python afin de pratiquer et approfondir les concepts de programmation orientée objet.

L'objectif est de construire progressivement une calculatrice en plusieurs versions, tout en appliquant de bonnes pratiques de conception et en découvrant différents concepts de Python.

## Objectifs

Ce projet permet de travailler notamment sur :

- Programmation orientée objet
- Héritage
- Polymorphisme
- Pattern Factory
- Exceptions personnalisées
- Tests unitaires avec `pytest`
- Interface graphique
- Threads et concurrence
- Synchronisation avec `Lock` un truc avec le 'Threads'
- Gestion d'un historique des calculs

## Versions

### V1 — Calculatrice console

- Addition
- Soustraction
- Multiplication
- Division
- Gestion des erreurs
- Exceptions personnalisées
- Saisie d'une expression :

```text
5 + 7
10 / 2
25 * 4
```

- Possibilité d'effectuer plusieurs calculs (un par un)
- `Ctrl + C` pour quitter

### V2 — Interface graphique

Création d'une interface graphique permettant d'utiliser la calculatrice sans passer directement par le terminal.

### V3 — Fonctionnalités avancées

- Historique des calculs
- Exécution avec des threads
- Synchronisation des accès aux données
- Tests du code concurrent
- Gestion des interactions clavier

## Architecture

Le projet est organisé autour de plusieurs responsabilités :

```text
calculator/
│
├── main.py
│
├── src/
│   ├── operations/
│   │   ├── operation.py
│   │   ├── addition.py
│   │   ├── soustraction.py
│   │   ├── multiplication.py
│   │   └── division.py
│   │
│   ├── exceptions/
│   │   ├── calculator_exception.py
│   │   ├── division_by_zero.py
│   │   └── invalid_operation.py
│   │
│   ├── services/
│   │   ├── calculator.py
│   │   ├── history.py
│   │   └── operation_factory.py
│   │
│   ├── threads/
│   │   └── calculation_task.py
│   │
│   └── ui/
│       └── calculator_window.py
│
└── tests/
    ├── test_operations.py
    ├── test_calculator.py
    └── test_history.py
```

Le fonctionnement principal repose sur une séparation claire des responsabilités :

```text
Utilisateur
    |
main.py
    |
OperationFactory
    |
Operation
    |
Calculator
    |
Résultat
```

`OperationFactory` est responsable de créer l'opération appropriée, tandis que `Calculator` est responsable de son exécution.

## Concepts de POO

Les différentes opérations héritent d'une classe commune :

```text
             Operation
                 │
       ┌─────────┼─────────┐         
   Addition   Multiplication  Division
```

Cette architecture permet notamment d'utiliser le polymorphisme : `Calculator` peut recevoir différentes opérations sans avoir besoin de connaître leur classe concrète.

## Lancer le projet

Depuis la racine du projet :

```bash
python3 main.py
```

Puis entrer une opération :

```text
Calcul : 5 + 7
Résultat : 12.0
```

Pour quitter :

```text
Ctrl + C
```

## Tests

Les tests sont réalisés avec `pytest`.

```bash
pytest
```

## Pourquoi ce projet ?

Ce projet est avant tout un projet d'apprentissage.

L'objectif n'est pas de créer une calculatrice complexe, mais de construire progressivement une application simple permettant de comprendre et de pratiquer des concepts importants du développement logiciel.

## Améliorations prévues

- [x] Finaliser la V1 console
- [ ] Améliorer le parsing des expressions
- [ ] Ajouter davantage de tests
- [ ] Créer l'interface graphique
- [ ] Ajouter l'historique
- [ ] Implémenter les threads
- [ ] Ajouter la synchronisation
- [ ] Tester les comportements concurrents
- [ ] Améliorer l'expérience utilisateur

---

Projet réalisé en Python.