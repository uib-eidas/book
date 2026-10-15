# Resum: el mapa d'eIDAS 2.0

---

## Tots els termes en un mapa

```mermaid
%%{init: {"theme": "base", "themeVariables": {"primaryColor": "#e8f1fa", "primaryTextColor": "#1a1a1a", "primaryBorderColor": "#0065bd", "lineColor": "#0065bd", "secondaryColor": "#fff4e0", "tertiaryColor": "#f6f9fc", "fontFamily": "Helvetica, Arial, sans-serif", "fontSize": "16px"}, "flowchart": {"htmlLabels": true, "nodeSpacing": 30, "rankSpacing": 40, "diagramPadding": 20}}}%%
flowchart TB
  U["<b>Usuari</b> (titular)"]:::actor

  subgraph W["<b>Cartera</b> (EUDI Wallet)"]
    direction LR
    WU["<b>Unitat de cartera</b><br/>Proveïdor: estat o organització reconeguda<br/>Solució de cartera (certificada)<br/>Instància · WSCA · WSCD<br/>Magatzem de claus · QSCD<br/>WIA · KA (acreditacions)<br/>Estats: instal·lada · operativa · vàlida · revocada"]
    CR["<b>Credencials</b><br/>PID<br/>EAA: QEAA · Pub-EAA · no qualificada<br/>Formats: mdoc · SD-JWT VC · W3C VCDM<br/>Divulgació selectiva · Vinculació al dispositiu<br/>Revocació · Llibre de regles"]
  end

  TS["<b>Serveis de confiança</b><br/>Signatura (QES) · segell<br/>Segell de temps · Entrega certificada<br/>QWAC · Arxiu · Llibres majors<br/>Signatura en remot (QESRC)"]
  PR["<b>Protocols</b><br/>OpenID4VCI (emissió)<br/>OpenID4VP (remot)<br/>ISO/IEC 18013-5 (presencial) · 18013-7<br/>HAIP · DCQL<br/>API de credencials digitals · Dades transaccionals"]
  EM["<b>Emissors</b><br/>Proveïdor de PID<br/>Proveïdors d'EAA: QTSP · públic · no qualificat<br/>Fonts autèntiques<br/>Catàleg d'esquemes i d'atributs"]:::actor
  RP["<b>Part usuària</b> (verificador)<br/>Banc · botiga · administració<br/>Intermediaris<br/>Certificat d'accés · de registre"]:::actor
  TR["<b>Infraestructura de confiança</b><br/>Certificats X.509 · Àncora de confiança<br/>Llistes de confiança (ETSI TS 119 612)<br/>LoTE (ETSI TS 119 602)<br/>Registrador · Autoritat de certificats d'accés<br/>CAB · NAB · Supervisió<br/>Certificació (CSA · ENISA)"]

  U -- controla --> W
  TS -- "QES&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" --> W
  W -- usa --> PR
  EM == emet ==> W
  W == presenta ==> RP
  TR -- registra --> EM
  TR -- certifica --> W
  TR -- registra --> RP
  RP -. "es fia de l'emissor per les llistes" .-> EM

  classDef default fill:#e8f1fa,stroke:#0065bd,color:#1a1a1a,text-align:left
  classDef actor fill:#fff4e0,stroke:#b3541e,stroke-width:2px,color:#1a1a1a,text-align:left
  style W fill:#f6f9fc,stroke:#0065bd,stroke-width:2px
```

---

## Del reglament a la cartera

- **eIDAS** (2014) regulava la identificació electrònica i els serveis de confiança; **eIDAS 2.0** (2024) el modifica i crea el marc europeu d'identitat digital
- Els **actes d'execució** concreten els detalls tècnics; l'**ARF** explica com construir-ho, però no obliga
- El resultat és la **EUDI Wallet**: cada estat n'ha d'oferir almenys una, gratuïta, voluntària i de **nivell de garantia alt**

---

## De l'emissor a la part usuària

- Els **emissors** (proveïdor de PID; proveïdors de QEAA, Pub-EAA i EAA) emeten credencials a la cartera, comprovant les dades contra **fonts autèntiques**
- L'**usuari** les guarda a la seva **unitat de cartera** i decideix què presenta
- La **part usuària** demana atributs, registrada davant d'un **registrador** i identificada amb un **certificat d'accés**
- Al voltant, qui fa que tot sigui de fiar: **CAB**, **NAB**, organismes de supervisió i el **proveïdor de la cartera**

---

## De la credencial al protocol

- Dues menes de credencial: el **PID** (qui ets) i les **EAA** (què és cert sobre tu); més la **signatura qualificada** (QES)
- Dos formats obligatoris, **mdoc** i **SD-JWT VC**, amb el mateix patró: hashes amb sal, **divulgació selectiva** i **vinculació al dispositiu**
- Tres protocols: **OpenID4VCI** per emetre, **OpenID4VP** per presentar en remot, **ISO/IEC 18013-5** per presentar en persona
- **HAIP** fixa les opcions perquè tot sigui interoperable

---

## De la confiança a la privadesa

- Tot es verifica amb **certificats X.509** que encadenen fins a una **àncora** publicada en una **llista de confiança** (estats) o una **LoTE** (Comissió)
- Els **serveis de confiança** qualificats (signatura, segell, temps, entrega, arxiu, llibres majors) tenen presumpció legal de validesa
- El punt feble conegut és la **vinculabilitat**: els mètodes A–D mitiguen la de les parts usuàries; la de l'emissor només la resoldran les **proves de coneixement zero**
- Mentrestant, la **implementació de referència** i els **pilots** van provant tot plegat

---

## Idees clau del llibre

1. eIDAS 2.0 és la **SSI regulada**: el model d'interacció de la SSI, amb la confiança ancorada en el marc legal
2. L'usuari té el **control**: res no surt de la cartera sense la seva aprovació, i només els atributs necessaris
3. Tothom que participa està **registrat, acreditat o certificat**
4. Els **estàndards oberts** (OpenID, ISO, IETF, ETSI) són el que fa que una cartera d'un estat funcioni a tots els altres
5. Queden coses per resoldre, i la **privadesa forta** és la més important

---

## Per continuar

- El **[glossari](../../glossary.md)** té cada terme del mapa amb la definició i el tema on s'explica
- Els **[recursos](../../resources.md)** enllacen les fonts primàries: reglament, actes d'execució, ARF i especificacions
- Per a la pràctica, el tema 10: la implementació de referència es pot compilar i provar
