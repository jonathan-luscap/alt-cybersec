# iteration 2 : dépendances

## 1.1 — Le rôle des dépendances (etl’exemple de log4j)

je pense qu'apache a du être touché.

## 1.3 — Dependencies de “conduit”

le programme à installer pour gérer les dépendances du projet est **composer**. pour mettre à jour un projet comme conduit en laravel 8.65, la dernière version de composer est plus adaptée. les dépendances sont répertorié dans composer.json :

 "require": {
        "php": "^7.3|^8.0",
        "fruitcake/laravel-cors": "^2.0",
        "guzzlehttp/guzzle": "^7.0.1",
        "laravel/framework": "^8.65",
        "laravel/tinker": "^2.5",
        "tymon/jwt-auth": "^1.0"
    },
    "require-dev": {
        "facade/ignition": "^2.5",
        "fakerphp/faker": "^1.9.1",
        "laravel/sail": "^1.0.1",
        "mockery/mockery": "^1.4.4",
        "nunomaduro/collision": "^5.10",
        "phpunit/phpunit": "^9.5.10"
    }

php, laravel et jwt-auth sont des dépendances qui pour moi pourraient présenter des risques liés à la sécurité.

dernières versions :
    - php 8.4.1
    - laravel 11
    - jwt-auth 2

après avoir effectuer un 'compose audit', le projet ne présente que deux dépendances qui ont été abandonnées.