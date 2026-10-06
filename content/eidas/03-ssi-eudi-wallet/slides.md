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

Els mateixos tres papers de la SSI, amb noms nous. Qui és cadascun, al tema 4.

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

## Què és un certificat X.509?

- Un fitxer que lliga una **clau pública** amb la **identitat** de qui la té
  - Diu de qui és, qui ho certifica, fins quan val, i porta la **signatura** de l'autoritat que l'ha emès
- X.509 és l'estàndard que en fixa el format; és el mateix dels certificats dels llocs web i del DNI electrònic
- Es verifica seguint la **cadena**: el certificat el signa una autoritat, que té el seu propi certificat, fins a arribar a una **àncora de confiança**

---v

## Com s'usen a eIDAS 2.0

- Els **emissors** signen el PID i les declaracions amb una clau que té certificat; la part usuària en segueix la cadena fins a una llista de confiança
- Les **parts usuàries** s'autentiquen davant la cartera amb un certificat d'accés
- El **proveïdor de la cartera** acredita cada unitat amb certificats propis
- Les **signatures qualificades** es basen en un certificat qualificat
- A la SSI aquest paper el fa el DID, resolt en un registre descentralitzat; aquí el fa el certificat, resolt en una llista signada

---

## Què s'adopta de la SSI

- **Control de l'usuari**: cap dada surt de la cartera sense la seva aprovació
- **Credencials a la cartera**: es presenten sense passar per l'emissor
  - L'emissor no ha de saber on ni quan es fan servir
- **Divulgació selectiva**: només els atributs necessaris
- **Pseudònims**, quan no cal identificar l'usuari
- El **model de tres rols** i els **formats** de credencial verificable: mdoc i SD-JWT VC

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

## És SSI, la EUDI Wallet?

- **Sí**, en la interacció: l'usuari guarda les credencials i decideix què presenta i a qui
- **No**, en la confiança: no és descentralitzada
  - Emissors, verificadors i carteres han de ser admesos per una autoritat
- Es pot entendre com una **SSI regulada**: el model de la cartera, amb la confiança ancorada en el marc legal

---

## Idees clau

- eIDAS 2.0 adopta la **manera d'interactuar** de la SSI: credencials a la cartera, divulgació selectiva, pseudònims
- No n'adopta la **confiança descentralitzada**: certificats X.509 i llistes signades, en lloc de DID i registres distribuïts
- Qui emet, qui verifica i qui proveeix carteres ha d'estar **registrat o certificat**
- L'**ARF** diu com construir-ho; només el reglament i els actes d'execució obliguen

---

## Referències

- Comissió Europea, [_Architecture and Reference Framework_](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/), versió 3.0 (2026), sota llicència CC BY 4.0
- [Reglament (UE) 2024/1183](https://eur-lex.europa.eu/eli/reg/2024/1183/oj)
- [Reglament d'execució (UE) 2025/848](https://eur-lex.europa.eu/eli/reg_impl/2025/848/oj), sobre el registre de les parts usuàries
