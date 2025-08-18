OrangeHRM Automation Tests
Automatizovani testovi za OrangeHRM aplikaciju, napisani u Python-u koristeći Selenium WebDriver i Pytest framework.

🔧 Tehnologije korišćene
Python 3.x

Selenium WebDriver

Pytest

Page Object Model (POM)

(Opcionalno) pytest-html / Allure za izveštaje

📁 Struktura projekta
graphql
Copy
Edit
orangehrm-tests/
│
├── pages/         # Page Object modeli
├── tests/         # Test slučajevi
├── utils/         # Pomoćne funkcije (npr. lokatori, konfiguracije)
├── conftest.py    # Pytest konfiguracija i fixture-i
├── requirements.txt
└── README.md

▶️ Pokretanje testova
Instaliraj zavisnosti:

bash
Copy
Edit
pip install -r requirements.txt
Pokreni testove:

bash
Copy
Edit
pytest tests/
(Opcionalno) Generiši HTML izveštaj:

bash
Copy
Edit
pytest --html=report.html

🧪 Primer test scenarija

Valid login

Invalid login

Navigacija kroz dashboard

Provera vidljivosti UI elemenata

✅ TODO
 Dodati PyTest izveštaje

 Pokriti edge-case testove

 CI integracija (GitHub Actions)

📌 Napomene
Ovaj projekat koristi Page Object Model kako bi odvojio logiku interakcije sa stranicama od samih testova.

👨‍💻 Autor
Ivan Djukanović - GitHub