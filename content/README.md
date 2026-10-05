# eIDAS 2.0

![Logo UIB](./img/logo-uib.png)

> **Universitat de les Illes Balears**
>
> **Autor**: Miquel A. Cabot ([miquel.cabot@uib.cat](mailto:miquel.cabot@uib.cat))

Documentació sobre el funcionament d'**eIDAS 2.0**: el Reglament (UE) 2024/1183, la cartera europea d'identitat digital (EUDI Wallet), els seus actors, credencials i protocols. Està escrita en format [mdBook](https://rust-lang.github.io/mdBook/), amb presentacions generades mitjançant [reveal-js](https://revealjs.com/).

## Llegeix el Llibre

Us recomanam la [versió en línia](#disponible-en-línia) per a un ús general. Tot i així, podeu clonar, instal·lar i compilar aquest llibre [sense connexió](#compilar-sense-connexió).

### Disponible en línia

La darrera versió està disponible a: [https://uib-eidas.github.io/book/](https://uib-eidas.github.io/book/)

### Compilar sense connexió

Heu d'[instal·lar Rust](https://www.rust-lang.org/tools/install) abans de continuar.

Per a fer-vos la vida més senzilla amb `make` 😉, disposeu d'un conjunt de tasques que utilitzen [`cargo make`](https://sagiegurari.github.io/cargo-make/#overview).

Un cop tingueu [`cargo make`](https://sagiegurari.github.io/cargo-make/#installation) instal·lat, podeu llistar totes les tasques incloses per facilitar la instal·lació, compilació, servei, formatació i més amb:

```sh
# Executeu-ho des del directori arrel d'aquest repositori
makers --list-all-steps
```

Les tasques haurien de ser autoexplicatives.

### Servir en local amb Yarn

El `package.json` inclou dos scripts per veure el contingut en local. Necessiteu [Yarn](https://yarnpkg.com/) i haver instal·lat les dependències un cop amb `yarn install`.

**Presentacions** (`serve-slides`): arrenca [reveal-md](https://github.com/webpro/reveal-md) a `http://localhost:1948`, amb un llistat de tots els fitxers `slides.md`. Es recarrega automàticament quan en modificau un.

```sh
yarn serve-slides
```

**Llibre** (`serve-book`): amb Python 3, serveix el contingut de la carpeta `html-book` a `http://localhost:1949`. No compila ni detecta canvis, així que primer heu de generar el llibre i tornar-ho a fer després de cada modificació.

```sh
mdbook build
yarn serve-book
```

Els enllaços «Obrir la presentació» del llibre només funcionen si les presentacions s'han incrustat dins `html-book`. La tasca `makers serve` ho fa tot: compila presentacions i llibre, les incrusta i arrenca aquest mateix servidor.

## Llicència

Tots els materials d'aquest repositori estan llicenciats sota la Llicència Mozilla Public License Versió 2.0. Consulteu la [Llicència](./LICENSE.md) per a més detalls.
