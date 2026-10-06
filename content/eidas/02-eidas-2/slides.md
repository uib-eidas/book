# D'eIDAS a eIDAS 2.0

---

## eIDAS: el punt de partida

- **Reglament (UE) 910/2014**, relatiu a la identificació electrònica i els serveis de confiança
- Aplicable des de l'**1 de juliol de 2016**
  - Deroga la Directiva 1999/93/CE de signatura electrònica
- Com a reglament, és **directament aplicable** a tots els estats membres
- Té dos pilars:
  1. **Identificació electrònica**
  2. **Serveis de confiança**

---v

## Pilar 1: identificació electrònica

- Cada estat membre té el seu propi sistema d'identificació electrònica, com el DNI electrònic a Espanya
- L'estat pot **notificar-lo**: comunicar-lo formalment a la Comissió perquè els altres estats l'avaluïn i el reconeguin
  - És voluntari: cada estat decideix si ho fa
- **Reconeixement mutu**: un cop notificat, els serveis públics dels altres estats l'han d'acceptar

---v

## Nivells de garantia

- El **nivell de garantia** diu quanta confiança es pot tenir que l'usuari és qui diu ser
- Depèn de dues coses:
  - Com es va **comprovar la identitat** en donar-lo d'alta
  - Com de difícil és **suplantar-lo** després
- Tres nivells:
  - **Baix**: només redueix el risc de suplantació
  - **Substancial**: el redueix força; per exemple, dos factors i identitat contrastada
  - **Alt**: l'ha d'evitar; identitat verificada presencialment o equivalent, i claus en maquinari segur
- La cartera europea ha de ser de nivell **alt**

---v

## Pilar 2: serveis de confiança

- Serveis regulats:
  - **Signatura electrònica** (persones físiques) i **segell electrònic** (persones jurídiques)
  - **Segell de temps** electrònic
  - **Entrega electrònica certificada**
  - **Certificats d'autenticació de llocs web**
- Distingeix entre serveis **qualificats** i no qualificats
  - Els prestadors qualificats estan supervisats i figuren a les **llistes de confiança**
- La **signatura electrònica qualificada** té el mateix efecte jurídic que la signatura manuscrita, i es reconeix a tots els estats membres

---

## Per què calia revisar-lo?

- **Fragmentació**: solucions nacionals divergents i estats sense cap mitjà d'identificació electrònica
- **Sector privat**: els beneficis d'eIDAS no hi arribaven
- **Només identitat**: no preveia compartir atributs verificats, com títols acadèmics o qualificacions professionals
- **Control de l'usuari**: calia que cada persona pogués decidir quines dades comparteix i amb qui

> Objectiu per al 2030: una identitat digital de confiança, voluntària i controlada per l'usuari, reconeguda a tota la Unió.

---

## eIDAS 2.0

- **Reglament (UE) 2024/1183**, d'11 d'abril de 2024
- No substitueix eIDAS: **modifica** el Reglament 910/2014
- En vigor des del **20 de maig de 2024**
- Estableix el **marc europeu d'identitat digital**
- Tres grans novetats:
  1. La **cartera europea d'identitat digital**
  2. Les **declaracions electròniques d'atributs** (EAA)
  3. **Nous serveis de confiança**

---

## La cartera europea d'identitat digital

- _European Digital Identity Wallet_ (EUDI Wallet)
- És un **mitjà d'identificació electrònica** que permet a l'usuari:
  - Guardar i gestionar les seves **dades d'identificació** i **declaracions d'atributs**
  - Presentar-les a les parts usuàries i a altres carteres
  - **Signar** amb signatura electrònica qualificada
- Cada estat membre n'ha d'oferir **almenys una**, amb nivell de garantia **alt**: identitat verificada a fons i claus en maquinari segur

---v

## Qui proporciona la cartera?

- Tres vies possibles:
  - Directament l'**estat membre**
  - Un tercer, per **mandat** de l'estat
  - Un tercer **independent**, però reconegut per l'estat
- El codi font dels components d'aplicació ha de tenir **llicència de codi obert**

---v

## Què ha de permetre fer

- Obtenir, guardar, combinar i presentar dades d'identificació i atributs, **en línia i fora de línia**
- **Divulgació selectiva**: compartir només les dades necessàries
- Generar **pseudònims**
- Intercanviar dades de forma segura **entre dues carteres**
- Consultar un **registre de transaccions**, demanar la supressió de dades i denunciar peticions sospitoses
- **Signar** amb signatura electrònica qualificada
- Exercir el dret a la **portabilitat** de les dades

---v

## Garanties per a l'usuari

- **Voluntària**: no es pot perjudicar qui no la faci servir
- **Gratuïta** per a les persones físiques
  - També la signatura qualificada, per a usos no professionals
- **Control total** de l'usuari sobre les seves dades
- **Sense seguiment**: ni el proveïdor de la cartera ni els emissors poden rastrejar l'ús que se'n fa
- **Accessible** per a persones amb discapacitat

---

## Declaracions electròniques d'atributs (EAA)

- **Atribut**: característica, qualitat, dret o permís d'una persona o d'un objecte
- **Declaració electrònica d'atributs** (_Electronic Attestation of Attributes_, EAA): declaració en format electrònic que permet autenticar atributs
- Tres tipus, segons qui les emet:
  - **EAA, no qualificada**: qualsevol prestador de serveis de confiança
  - **QEAA** (_Qualified EAA_): un prestador **qualificat** de serveis de confiança
  - **Pub-EAA** (_Public body EAA_): un organisme públic responsable d'una **font autèntica**, o algú en nom seu

---v

## Efecte jurídic

- Cap declaració d'atributs es pot rebutjar només pel fet de ser electrònica
- Les **QEAA** i les **Pub-EAA** tenen el mateix efecte jurídic que les declaracions en paper
- Les **Pub-EAA** d'un estat membre es reconeixen a tots els altres

---v

## Atributs mínims verificables

Els estats han de permetre verificar, contra fonts autèntiques del sector públic, almenys:

- Adreça, edat, gènere, estat civil i composició familiar
- Nacionalitat o ciutadania
- Títols acadèmics i qualificacions professionals
- Poders de representació
- Permisos i llicències públics
- Dades financeres i societàries (persones jurídiques)

---

## Parts usuàries

- **Part usuària** (_relying party_): qui confia en la cartera per prestar un servei
- Obligacions:
  - **Registrar-se** a l'estat membre on està establerta
  - Declarar **quines dades demanarà**, i no demanar-ne cap altra
  - **Identificar-se** davant l'usuari
  - Acceptar **pseudònims** quan la llei no exigeix identificar l'usuari
- El registre de parts usuàries és **públic**

---v

## Qui ha d'acceptar la cartera?

- **Sector públic**: tots els serveis en línia que exigeixen identificació electrònica
- **Sector privat** obligat a fer autenticació forta: transport, energia, banca, salut, educació, telecomunicacions...
  - Excepte microempreses i petites empreses
- **Plataformes en línia molt grans**, quan exigeixen autenticació

Sempre a **petició voluntària de l'usuari**.

---

## Nous serveis de confiança

- **Emissió de declaracions electròniques d'atributs**
- **Arxiu electrònic**
- **Llibres majors electrònics** (_electronic ledgers_)
- **Gestió de dispositius remots** de creació de signatura i de segell

---v

## Certificats d'autenticació web (QWAC)

- Els **navegadors** han de reconèixer els certificats qualificats d'autenticació de llocs web
  - I mostrar de manera clara les dades d'identitat que contenen
- Només poden prendre **mesures cautelars** contra un certificat en cas de bretxa de seguretat o pèrdua d'integritat, i ho han de notificar
- És un dels punts més polèmics del reglament

---

## Què canvia

|                           | eIDAS (2014)                           | eIDAS 2.0 (2024)                                |
| ------------------------- | -------------------------------------- | ----------------------------------------------- |
| **Mitjà d'identificació** | Sistemes nacionals                     | Sistemes nacionals i cartera                    |
| **Obligació dels estats** | Notificar és opcional                  | Oferir almenys una cartera                      |
| **Abast**                 | Sector públic                          | Públic i part del privat                        |
| **Dades**                 | Identitat                              | Identitat i atributs                            |
| **Control de l'usuari**   | No previst                             | Divulgació selectiva                            |
| **Serveis de confiança**  | Signatura, segell, temps, entrega, web | S'hi afegeixen atributs, arxiu i llibres majors |

---

## Cronologia

![Cronologia d'eIDAS a eIDAS 2.0, de 2014 a finals de 2027](./img/cronologia.svg)

Els **actes d'execució** són els reglaments amb què la Comissió concreta els detalls tècnics de la cartera. Els dos terminis es compten des que van entrar en vigor: 24 mesos per a les carteres i 36 per a l'acceptació pel sector privat.

---

## Relació amb la SSI

- eIDAS 2.0 adopta el **triangle de confiança** de la SSI:
  - **Emissor**: proveïdors de dades d'identificació i de declaracions d'atributs
  - **Titular**: usuari de la cartera
  - **Verificador**: part usuària
- I els seus principis: control de l'usuari, divulgació selectiva i pseudònims
- La confiança, però, s'ancora en un **marc legal**: prestadors supervisats, registres i llistes de confiança

---

## Referències

- [Reglament (UE) 2024/1183](https://eur-lex.europa.eu/eli/reg/2024/1183/oj), pel qual es modifica el Reglament (UE) 910/2014
- [Reglament (UE) 910/2014](https://eur-lex.europa.eu/eli/reg/2014/910/oj) (eIDAS)
- [Reglament d'execució (UE) 2024/2979](https://eur-lex.europa.eu/eli/reg_impl/2024/2979/oj), sobre la integritat i les funcionalitats bàsiques de la cartera
