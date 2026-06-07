# Analizor NLP pentru Texte

Acesta este un proiect simplu, scris în Python, pe care l-am făcut ca să experimentez cu NLP (Procesarea Limbajului Natural). 

Practic, programul citește o propoziție de la tastatură și încearcă să-și dea seama despre ce e vorba. El împarte textele în 3 categorii:
* Discuție normală / de zi cu zi
* Problemă tehnică
* Formulă matematică

## Cum gândește codul (explicat simplu)?
* **Face curățenie:** Prima dată ia textul și șterge semnele de punctuație și cuvintele de legătură care doar încurcă la analiză (de, la, pe, și, o, un).
* **Caută matematică:** Se uită prin text după chestii care arată a ecuații matematice (de exemplu, structuri cu `=` și `+`).
* **Partea „deșteaptă” (Stemming):** Când caută cuvinte tehnice, programul nu o face orbește. El e capabil să taie sufixele românești de la finalul cuvintelor. Adică, dacă tu scrii „senzorului” sau „senzorilor”, codul taie terminațiile, vede că rădăcina e „senzor” și recunoaște cuvântul instantaneu din dicționarul lui.
  
