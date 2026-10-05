# Credencials

---

## De credencials a declaracions

- A la SSI en dèiem **credencials verificables**
- A eIDAS 2.0, les dades s'intercanvien en forma de **declaracions electròniques d'atributs**
- El reglament hi afegeix una categoria a part: les **dades d'identificació de la persona** (PID)
- Tècnicament, PID i declaracions es construeixen igual

---

## Anatomia d'una declaració

![Les tres parts d'una declaració: atributs, metadades i prova](./img/anatomia.svg)

---v

## Les tres parts

- **Atributs**: la informació sobre el subjecte
  - La part usuària en demana només els que necessita
- **Metadades**: la informació sobre la declaració mateixa
  - Tipus, proveïdor i període de validesa
  - Clau pública que la vincula al dispositiu
  - Referència per comprovar si ha estat revocada
- **Prova**: garanteix la integritat i l'autenticitat
  - Ha de permetre la **divulgació selectiva**
  - Inclou el certificat del proveïdor i la referència a l'àncora de confiança

---

## Quatre categories legals

- **PID**: dades d'identificació de la persona
- **QEAA**: declaració qualificada, emesa per un prestador qualificat
- **Pub-EAA**: emesa per un organisme públic responsable d'una font autèntica
- **EAA**: declaració no qualificada

La diferència és **purament legal**, no tècnica:

- Un títol universitari pot ser una QEAA o una EAA, segons qui l'emeti
- Un permís de conduir pot ser Pub-EAA, QEAA o EAA, segons l'estat membre

---

## El PID

- Permet establir la **identitat** d'una persona
- Atributs **obligatoris**:
  - Cognoms i nom
  - Data i lloc de naixement
  - Nacionalitat
  - Fotografia, llevat que l'usuari hi renunciï
- Atributs **opcionals**: adreça, sexe, número administratiu personal, correu electrònic, telèfon...
- Metadades: autoritat i país que l'emeten

---v

## Particularitats del PID

- És l'única dada que ha de tenir **nivell de garantia alt**
  - Les seves claus han d'estar al WSCD
- Determina l'estat de la cartera: sense cap PID vàlid, la unitat és operativa però no **vàlida**
- Una cartera pot contenir **diversos PID**
  - Per exemple, si l'usuari té més d'una nacionalitat
  - Tots han de ser de la mateixa persona

---

## Formats

| | mdoc | SD-JWT VC | W3C VCDM 2.0 |
| --- | --- | --- | --- |
| **Estàndard** | ISO/IEC 18013-5 | IETF | W3C |
| **Codificació** | CBOR (binari) | JSON | JSON-LD |
| **Prova** | Hashes amb sal | Hashes amb sal | S'ha de definir a part |
| **Ús principal** | Presencial | Remot | General |
| **Suport a la cartera** | Obligatori | Obligatori | Opcional |

---v

## mdoc

- Neix com a estàndard del **permís de conduir mòbil** (mDL)
  - Només l'esquema d'atributs és específic del permís; la resta és genèric
- Codificació binària **CBOR**, amb espais de noms per evitar col·lisions
- La vinculació al dispositiu és **obligatòria**
- Serveix per a presentacions **presencials** i remotes

---v

## SD-JWT VC

- Un **JSON Web Token** amb divulgació selectiva
- Cada tipus de declaració s'identifica amb un **tipus de credencial** (`vct`)
  - Un tipus en pot estendre un altre: tipus nacionals a partir d'un tipus europeu comú
- La vinculació al dispositiu és opcional a l'estàndard
- Només per a presentacions **remotes**
- Té moltes opcions: cal seguir el perfil **HAIP** per garantir la interoperabilitat

---v

## W3C VCDM

- Un **model de dades** general, basat en JSON-LD
- Deixa oberts els mecanismes de seguretat, la signatura i el transport
  - Cal un perfil addicional per ser interoperable
- A la cartera és **opcional**, i només per a declaracions **no qualificades**
- Molt utilitzat al sector **educatiu**

---

## Divulgació selectiva

![Divulgació selectiva amb hashes amb sal: l'emissor signa els hashes, la cartera revela només alguns atributs i la part usuària els verifica](./img/divulgacio-selectiva.svg)

---v

## Com funciona

1. L'emissor calcula el **hash** de cada atribut, combinat amb una **sal** aleatòria
2. Signa la llista de hashes, no els valors
3. La cartera envia la llista signada i, només per als atributs triats, el **valor i la sal**
4. La part usuària recalcula els hashes i comprova que són a la llista signada

Els dos formats obligatoris fan servir el mateix mecanisme.

---

## Vinculació al dispositiu

- Evita que una declaració es pugui **copiar** a una altra cartera
- La declaració conté una **clau pública**; la privada no surt mai del WSCD o del magatzem de claus
- En cada presentació, la cartera **signa un repte** aleatori de la part usuària
  - Per això també se'n diu **prova de possessió**
- **Obligatòria** per al PID i per a totes les declaracions mdoc
- **Recomanada** per a les declaracions SD-JWT VC

---

## Revocació

- Si una declaració és vàlida més de **24 hores**, ha d'incloure informació de revocació
- Dos mecanismes:
  - **Llista d'estat**: una cadena de bits; cada declaració hi té una posició
  - **Llista de revocació**: els identificadors de les declaracions revocades
- La part usuària descarrega la llista i hi consulta la declaració rebuda
  - És recomanable, però no obligatori
  - Sense connexió, ha de decidir segons el risc

---

## Declaració lògica i declaració tècnica

- **Lògica**: el que veu l'usuari, per exemple «el meu PID»
- **Tècnica**: l'objecte signat que realment es presenta
- Una declaració lògica correspon a **moltes de tècniques**
  - L'emissor en pot lliurar un **lot**
  - Tenen una validesa tècnica curta i es **reemeten** periòdicament
- Presentar-ne una de diferent cada vegada dificulta que les parts usuàries **relacionin** les presentacions d'un mateix usuari

---

## Esquemes, llibres de regles i catàlegs

- **Llibre de regles** (_Rulebook_): la documentació per a persones
  - Quins atributs té cada tipus de declaració, què signifiquen i com es codifiquen
- **Esquema de declaració**: la mateixa especificació, llegible per programes
- **Catàleg d'esquemes**: on es publiquen, perquè tothom els trobi
  - És públic, i registrar-s'hi no és obligatori
  - Aparèixer-hi no obliga ningú a acceptar la declaració

---v

## Qui defineix els llibres de regles?

- La **Comissió Europea**: el del PID i el del permís de conduir mòbil
- **Administracions i organitzacions sectorials**: llibres de regles europeus o de sector, per exemple per a titulacions
- **Proveïdors de declaracions**: extensions amb atributs nacionals o propis
- Hi ha també un **catàleg d'atributs**, perquè els prestadors qualificats sàpiguen a quina font autèntica verificar cada atribut

---

## Referències

- Comissió Europea, [_Architecture and Reference Framework_](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/), versió 3.0 (2026), capítols 5 i 6, sota llicència CC BY 4.0
- Comissió Europea, [_PID Rulebook_](https://github.com/eu-digital-identity-wallet/eudi-doc-attestation-rulebooks-catalog/blob/main/rulebooks/pid/pid-rulebook.md)
- [Reglament d'execució (UE) 2024/2977](https://eur-lex.europa.eu/eli/reg_impl/2024/2977/oj), sobre el PID i les declaracions electròniques d'atributs
- [RFC 9901: Selective Disclosure for JSON Web Tokens](https://www.rfc-editor.org/rfc/rfc9901.html)
