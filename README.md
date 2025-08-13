# OrangeHRM Automated Tests

##  Što ovaj repo radi
Automatizuje testiranje OrangeHRM web aplikacije koristeći Python + pytest + Selenium (Page Object Model).  
Pokriveni scenariji: login, pretraga zaposlenih, CRUD operacije nad entitetima.

##  Tehnologije
| Komponenta         | Detalji                        |
|-------------------|--------------------------------|
| Python            | verzija 3.x                   |
| pytest            | test framework                |
| Selenium WebDriver| browser automation            |
| pytest-html/allure| izveštaji                     |
| Page Object Model | organizacija koda             |

##  Instalacija
```bash
git clone https://github.com/iduk1618/orangehrm-tests.git
cd orangehrm-tests
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # unesi URL, korisnika, lozinku
