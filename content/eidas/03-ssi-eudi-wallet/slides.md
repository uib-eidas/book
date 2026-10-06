# De la SSI a la EUDI Wallet

---

## Dos punts de partida

- La **SSI** és un model d'identitat i un conjunt de tecnologies
  - Sorgeix d'una comunitat tècnica, sense cap autoritat central
- **eIDAS 2.0** és un marc legal
  - Diu què ha de fer la cartera, però no com s'ha de construir
- El pont entre tots dos és l'**ARF**

---v

## L'ARF

- **_Architecture and Reference Framework_**: el document tècnic de referència de la cartera
- Forma part de la **caixa d'eines comuna de la Unió** (_Common Union Toolbox_)
  - L'elaboren els estats membres i la Comissió
- És **informatiu**, no jurídicament vinculant
  - L'únic obligatori són el reglament i els seus actes d'execució
- Evoluciona contínuament: aquí es fa servir la **versió 3.0** (juliol de 2026)

---

## El triangle es manté

![Ecosistema de la EUDI Wallet: emissors, titular i part usuària, sobre una infraestructura de confiança](./img/ecosistema.svg)

---

## De la SSI a eIDAS 2.0: vocabulari

| SSI                               | eIDAS 2.0                                                                                                                |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Emissor**                       | Proveïdor de PID (_PID Provider_) o de declaracions d'atributs (_Attestation Provider_)                                  |
| **Titular**                       | Usuari de la cartera                                                                                                     |
| **Cartera i agent**               | Unitat de cartera (_Wallet Unit_)                                                                                        |
| **Verificador**                   | Part usuària (_Relying Party_)                                                                                           |
| **Credencial verificable**        | PID (_Person Identification Data_) i declaracions electròniques d'atributs (EAA, _Electronic Attestation of Attributes_) |
| **DID**                           | Certificats X.509                                                                                                        |
| **Registre de dades verificable** | Llistes de confiança (_Trusted Lists_)                                                                                   |
| **Marc de governança**            | Reglament, actes d'execució i esquemes de declaració (_Attestation Schemes_)                                             |

---

## Els emissors

- **Proveïdor de PID** (_PID Provider_): verifica la identitat de l'usuari amb nivell de garantia alt i n'emet les dades d'identificació
- **Proveïdor de QEAA** (_Qualified EAA_): un prestador **qualificat** de serveis de confiança (_QTSP_)
- **Proveïdor de Pub-EAA** (_Public body EAA_): un organisme públic responsable d'una font autèntica, o algú en nom seu
- **Proveïdor d'EAA** (_non-qualified EAA_): qualsevol prestador de serveis de confiança **no qualificat**

---v

## Fonts autèntiques (_Authentic Sources_)

- Una **font autèntica** és el registre oficial on una dada és veritat per definició
  - El padró, per a l'adreça; el registre civil, per al naixement; la universitat, per a un títol
- Quan un emissor vol posar una dada en una declaració, la **comprova** contra la font autèntica
  - La declaració no inventa res: certifica el que ja diu el registre
- Si qui emet és el mateix **organisme responsable** del registre, la declaració és una Pub-EAA

---

## El titular: usuari i unitat de cartera

- **Proveïdor de la cartera** (_Wallet Provider_): un estat membre, o una organització amb mandat o reconeixement d'un estat
- **Solució de cartera** (_Wallet Solution_): el producte complet, que ha d'estar **certificat**
- **Unitat de cartera** (_Wallet Unit_): la configuració concreta que controla un usuari
  - La **instància** de la cartera (_Wallet Instance_): l'aplicació instal·lada al dispositiu
  - Un **dispositiu criptogràfic segur** (WSCD, _Wallet Secure Cryptographic Device_), que custodia les claus privades

---v

## Acreditar i revocar una cartera

- El proveïdor **acredita** cada unitat: li dona un certificat que demostra que és una cartera autèntica, amb les claus en un dispositiu segur
  - Els emissors ho comproven abans d'emetre-hi res
  - Com el certificat d'un lloc web, però per a la cartera
- Si la cartera es perd o es compromet, el proveïdor la **revoca**
  - Deixa de ser acceptada, i els PID que contenia es revoquen també

---

## El verificador: la part usuària (_Relying Party_)

- Un proveïdor de serveis que **demana atributs** a la cartera, amb l'aprovació de l'usuari
- S'ha de **registrar** a l'estat membre on està establert
- Rep un **certificat d'accés** (_access certificate_) per a cada una de les seves instàncies
  - Permet a la cartera autenticar qui li demana les dades
- Els **intermediaris** que actuen en nom seu també es consideren parts usuàries, i no poden guardar el contingut de les transaccions

---

## Què s'adopta de la SSI

- **Control de l'usuari**: cap dada surt de la cartera sense la seva aprovació
- **Credencials a la cartera**: es presenten sense passar per l'emissor
  - L'emissor no ha de saber on ni quan es fan servir
- **Divulgació selectiva**: només els atributs necessaris
- **Pseudònims**, quan no cal identificar l'usuari
- El **model de tres rols** i els formats de credencial verificable

---

## Què canvia respecte de la SSI

|                        | SSI                      | EUDI Wallet                            |
| ---------------------- | ------------------------ | -------------------------------------- |
| **Identificadors**     | DID                      | Certificats X.509                      |
| **Arrel de confiança** | Registre descentralitzat | Llistes signades per estats i Comissió |
| **Qui pot emetre**     | Qualsevol                | Entitats registrades                   |
| **Qui pot verificar**  | Qualsevol                | Parts usuàries registrades             |
| **Cartera**            | Qualsevol                | Solució certificada                    |
| **Governança**         | Marcs voluntaris         | Reglament                              |

> Les declaracions no qualificades (EAA) poden adoptar altres models de confiança.

---

## D'on surt la confiança

- No d'un registre descentralitzat, sinó de **llistes signades** per una autoritat (_Trusted Lists_)
  - Les dels prestadors qualificats, les signa cada **estat membre**
  - Les de proveïdors de cartera, de PID i de Pub-EAA, les signa la **Comissió**
- Emissors i parts usuàries s'han de **registrar** al seu estat membre, davant d'un registrador (_Registrar_)
  - Reben certificats amb què s'autentiquen davant la cartera

Es veurà amb detall al tema d'infraestructura de confiança.

---

## Formats i protocols

- **Formats** que tota cartera ha de suportar:
  - **mdoc** (ISO/IEC 18013-5)
  - **SD-JWT VC**
  - El model de dades del W3C és opcional, i només per a declaracions no qualificades
- **Emissió**: OpenID4VCI
- **Presentació remota**: OpenID4VP
- **Presentació presencial**: ISO/IEC 18013-5

Es veuran amb detall als temes de credencials i protocols.

---

## És SSI, la EUDI Wallet?

- **Sí**, en la interacció: l'usuari guarda les credencials i decideix què presenta i a qui
- **No**, en la confiança: no és descentralitzada
  - Emissors, verificadors i carteres han de ser admesos per una autoritat
- Es pot entendre com una **SSI regulada**: el model de la cartera, amb la confiança ancorada en el marc legal

---

## Referències

- Comissió Europea, [_Architecture and Reference Framework_](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/), versió 3.0 (2026), sota llicència CC BY 4.0
- [Reglament (UE) 2024/1183](https://eur-lex.europa.eu/eli/reg/2024/1183/oj)
- [Reglament d'execució (UE) 2025/848](https://eur-lex.europa.eu/eli/reg_impl/2025/848/oj), sobre el registre de les parts usuàries
