# 📖 Glossari

Sigles i termes que apareixen al llarg dels temes, amb el nom original en anglès i el tema on s'expliquen.

Aquesta documentació segueix la terminologia de la versió castellana del reglament, adaptada al català. Quan un terme és una traducció pròpia, s'indica el nom en anglès perquè es pugui contrastar amb les fonts.

## Marc legal i documents

| Terme                | En anglès                                                      | Què és                                                                                                   | Tema                                     |
| -------------------- | -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| **eIDAS**            | _electronic IDentification, Authentication and trust Services_ | Reglament (UE) 910/2014, sobre identificació electrònica i serveis de confiança                          | [2](./eidas/02-eidas-2/page.md)          |
| **eIDAS 2.0**        |                                                                | Nom habitual del Reglament (UE) 2024/1183, que modifica eIDAS i crea el marc europeu d'identitat digital | [2](./eidas/02-eidas-2/page.md)          |
| **Acte d'execució**  | _implementing act_                                             | Reglament de la Comissió que concreta com s'aplica eIDAS 2.0                                             | [2](./eidas/02-eidas-2/page.md)          |
| **ARF**              | _Architecture and Reference Framework_                         | Document tècnic de referència de la cartera, orientatiu i no vinculant                                   | [3](./eidas/03-ssi-eudi-wallet/page.md)  |
| **Llibre de regles** | _Rulebook_                                                     | Document que defineix un tipus de declaració: atributs, significat i codificació                         | [5](./eidas/05-credentials/page.md)      |
| **RGPD**             | _GDPR_                                                         | Reglament General de Protecció de Dades                                                                  | [9](./eidas/09-privacy-security/page.md) |

## Model i actors

| Terme                    | En anglès                                        | Què és                                                                                      | Tema                                    |
| ------------------------ | ------------------------------------------------ | ------------------------------------------------------------------------------------------- | --------------------------------------- |
| **SSI**                  | _Self-Sovereign Identity_                        | Identitat digital sobirana: model en què l'usuari guarda i presenta les seves credencials   | [1](./eidas/01-introduction/page.md)    |
| **Emissor**              | _issuer_                                         | Qui emet una credencial. A eIDAS 2.0, un proveïdor de PID o de declaracions                 | [1](./eidas/01-introduction/page.md)    |
| **Titular**              | _holder_                                         | Qui guarda i presenta les credencials. A eIDAS 2.0, l'usuari de la cartera                  | [1](./eidas/01-introduction/page.md)    |
| **Verificador**          | _verifier_                                       | Qui demana i comprova credencials. A eIDAS 2.0, la part usuària                             | [1](./eidas/01-introduction/page.md)    |
| **Part usuària**         | _relying party_ (RP)                             | Qui confia en la cartera per prestar un servei                                              | [2](./eidas/02-eidas-2/page.md)         |
| **IDP**                  | _Identity Provider_                              | Proveïdor d'identitat del model federat                                                     | [1](./eidas/01-introduction/page.md)    |
| **Font autèntica**       | _authentic source_                               | Registre reconegut per llei que conté atributs sobre persones                               | [3](./eidas/03-ssi-eudi-wallet/page.md) |
| **CAB**                  | _Conformity Assessment Body_                     | Organisme d'avaluació de la conformitat: certifica carteres i audita prestadors qualificats | [4](./eidas/04-architecture/page.md)    |
| **Registrador**          | _registrar_                                      | Organisme de cada estat que registra emissors i parts usuàries                              | [7](./eidas/07-trust/page.md)           |
| **Prestador qualificat** | _Qualified Trust Service Provider_ (QTSP)        | Prestador de serveis de confiança amb estatus qualificat                                    | [8](./eidas/08-trust-services/page.md)  |
| **QESRC**                | _Qualified Electronic Signature Remote Creation_ | Proveïdor de creació remota de signatura qualificada                                        | [4](./eidas/04-architecture/page.md)    |

## Cartera

| Terme                       | En anglès                                 | Què és                                                              | Tema                                   |
| --------------------------- | ----------------------------------------- | ------------------------------------------------------------------- | -------------------------------------- |
| **EUDI Wallet**             | _European Digital Identity Wallet_        | Cartera europea d'identitat digital                                 | [2](./eidas/02-eidas-2/page.md)        |
| **Unitat de cartera**       | _Wallet Unit_                             | La configuració concreta de cartera que controla un usuari          | [4](./eidas/04-architecture/page.md)   |
| **Instància de la cartera** | _Wallet Instance_                         | L'aplicació instal·lada al dispositiu                               | [4](./eidas/04-architecture/page.md)   |
| **WSCD**                    | _Wallet Secure Cryptographic Device_      | Dispositiu resistent a manipulacions que custodia les claus         | [4](./eidas/04-architecture/page.md)   |
| **WSCA**                    | _Wallet Secure Cryptographic Application_ | Aplicació que gestiona les claus dins el WSCD                       | [4](./eidas/04-architecture/page.md)   |
| **WIA**                     | _Wallet Instance Attestation_             | Acreditació de la instància: certifica que l'aplicació és autèntica | [4](./eidas/04-architecture/page.md)   |
| **KA**                      | _Key Attestation_                         | Acreditació de claus: certifica les propietats del WSCD             | [4](./eidas/04-architecture/page.md)   |
| **QSCD**                    | _Qualified Signature Creation Device_     | Dispositiu qualificat de creació de signatura                       | [8](./eidas/08-trust-services/page.md) |
| **HSM**                     | _Hardware Security Module_                | Maquinari de servidor que custodia claus                            | [4](./eidas/04-architecture/page.md)   |

## Credencials

| Terme                        | En anglès                              | Què és                                                                    | Tema                                 |
| ---------------------------- | -------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------ |
| **PID**                      | _Person Identification Data_           | Dades d'identificació de la persona                                       | [5](./eidas/05-credentials/page.md)  |
| **EAA**                      | _Electronic Attestation of Attributes_ | Declaració electrònica d'atributs                                         | [2](./eidas/02-eidas-2/page.md)      |
| **QEAA**                     | _Qualified EAA_                        | Declaració qualificada, emesa per un prestador qualificat                 | [2](./eidas/02-eidas-2/page.md)      |
| **Pub-EAA**                  |                                        | Declaració emesa per un organisme públic responsable d'una font autèntica | [2](./eidas/02-eidas-2/page.md)      |
| **mdoc**                     | _mobile document_                      | Format de credencial binari, definit a ISO/IEC 18013-5                    | [5](./eidas/05-credentials/page.md)  |
| **mDL**                      | _mobile Driving Licence_               | Permís de conduir mòbil                                                   | [5](./eidas/05-credentials/page.md)  |
| **SD-JWT VC**                | _SD-JWT-based Verifiable Credential_   | Format de credencial en JSON amb divulgació selectiva                     | [5](./eidas/05-credentials/page.md)  |
| **Divulgació selectiva**     | _selective disclosure_                 | Presentar només alguns atributs d'una credencial                          | [5](./eidas/05-credentials/page.md)  |
| **Vinculació al dispositiu** | _device binding_                       | Lligam criptogràfic entre una credencial i les claus d'un dispositiu      | [5](./eidas/05-credentials/page.md)  |
| **DID**                      | _Decentralized Identifier_             | Identificador descentralitzat de la SSI; eIDAS 2.0 no en fa servir        | [1](./eidas/01-introduction/page.md) |

## Protocols

| Terme                    | En anglès                                   | Què és                                                                   | Tema                              |
| ------------------------ | ------------------------------------------- | ------------------------------------------------------------------------ | --------------------------------- |
| **OpenID4VCI**           | _OpenID for Verifiable Credential Issuance_ | Protocol d'emissió                                                       | [6](./eidas/06-protocols/page.md) |
| **OpenID4VP**            | _OpenID for Verifiable Presentations_       | Protocol de presentació remota                                           | [6](./eidas/06-protocols/page.md) |
| **HAIP**                 | _High Assurance Interoperability Profile_   | Perfil que fixa les opcions dels protocols OpenID                        | [6](./eidas/06-protocols/page.md) |
| **Dades transaccionals** | _transactional data_                        | Dades que la part usuària afegeix a la petició perquè l'usuari les signi | [6](./eidas/06-protocols/page.md) |

## Confiança i privadesa

| Terme                         | En anglès                                      | Què és                                                                                                                 | Tema                                     |
| ----------------------------- | ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| **Àncora de confiança**       | _trust anchor_                                 | Clau o certificat arrel en què es confia per endavant                                                                  | [7](./eidas/07-trust/page.md)            |
| **PKI**                       | _Public Key Infrastructure_                    | Infraestructura de clau pública: autoritats de certificació que emeten certificats per dir de qui és cada clau pública | [1](./eidas/01-introduction/page.md)     |
| **Llista de confiança**       | _Trusted List_                                 | Llista de prestadors qualificats, signada per cada estat membre                                                        | [7](./eidas/07-trust/page.md)            |
| **LoTE**                      | _List of Trusted Entities_                     | Llista d'entitats de confiança, signada per la Comissió                                                                | [7](./eidas/07-trust/page.md)            |
| **Certificat d'accés**        | _access certificate_                           | Certificat amb què un emissor o una part usuària s'autentica davant la cartera                                         | [7](./eidas/07-trust/page.md)            |
| **Certificat de registre**    | _registration certificate_                     | Certificat que recull què ha declarat una entitat en registrar-se                                                      | [7](./eidas/07-trust/page.md)            |
| **QWAC**                      | _Qualified Website Authentication Certificate_ | Certificat qualificat d'autenticació de llocs web                                                                      | [8](./eidas/08-trust-services/page.md)   |
| **Vinculabilitat**            | _linkability_                                  | Possibilitat de relacionar diverses presentacions del mateix usuari                                                    | [9](./eidas/09-privacy-security/page.md) |
| **Prova de coneixement zero** | _Zero-Knowledge Proof_ (ZKP)                   | Prova que una afirmació és certa sense revelar res més                                                                 | [9](./eidas/09-privacy-security/page.md) |
