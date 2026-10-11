# \# 🏔️ Himachal Tourism


# \### Explore the Himalayas. Discover your next journey.


# A Django-powered tourism and travel booking web application designed to help users explore Himachal Pradesh tour packages, arrange taxi services, and manage their bookings through a convenient web interface.


# \[🌐 Live Demo](https://kushalsharma08.pythonanywhere.com) · \[📂 Source Code](https://github.com/Kushal57169/Himachal-tourism)


# \---


# \## ✨ Key Features


# \- \*\*User Authentication:\*\* Registration and login for user access.

# \- \*\*Tour Packages:\*\* Explore tourism packages and plan trips across Himachal Pradesh.

# \- \*\*Taxi Booking:\*\* Book transportation with options such as Sedan, SUV, and 7-seater vehicles.

# \- \*\*Booking Confirmations:\*\* Email confirmation for bookings.

# \- \*\*Coupon Generation:\*\* Generate booking coupons through the supported booking workflow.

# \- \*\*PDF Tickets:\*\* Generate and download booking tickets in PDF format.

# \- \*\*My Tickets:\*\* Access previously generated booking tickets.


# \## 🛠️ Technology Stack


# | Category | Technologies |

# |---|---|

# | Backend | Python, Django 5.2.1 |

# | Frontend | HTML5, CSS3, JavaScript, Bootstrap |

# | Database | SQLite |

# | PDF Generation | xhtml2pdf, ReportLab |

# | Supporting Libraries | Pillow, django-widget-tweaks, Requests |


# \## 📁 Project Structure


# ```text

# Himachal-tourism/

# ├── media/              # Media files

# ├── tourism\_project/    # Django project configuration

# ├── tours/              # Tourism application

# ├── manage.py           # Django management entry point

# ├── requirements.txt    # Python dependencies

# ├── .gitignore          # Files excluded from Git

# └── README.md           # Project documentation

# ```


# \## 🚀 Getting Started


# Follow these steps to run the project locally.


# \### Prerequisites


# \- Python 3.10 or a compatible newer version

# \- Git

# \- pip


# \### 1. Clone the repository


# ```bash

# git clone https://github.com/Kushal57169/Himachal-tourism.git

# cd Himachal-tourism

# ```


# \### 2. Create a virtual environment


# \*\*Windows:\*\*


# ```cmd

# py -m venv venv

# venv\\Scripts\\activate

# ```


# \### 3. Install dependencies


# ```bash

# python -m pip install --upgrade pip

# pip install -r requirements.txt

# ```


# \### 4. Configure the project


# Review `tourism\_project/settings.py` and configure the Django secret key, allowed hosts, debug settings, and email settings for your local environment.


# Keep private credentials and production secrets out of GitHub.


# \### 5. Apply database migrations


# ```bash

# python manage.py migrate

# ```


# \### 6. Start the development server


# ```bash

# python manage.py runserver

# ```


# Open the following address in your browser:


# ```text

# http://127.0.0.1:8000/

# ```


# \*\*Note:\*\* Email confirmations require suitable email settings. Additional database records or configuration may be necessary depending on the existing project setup.


# \## 🎯 Project Highlights


# \- Developed a web-based tourism and booking solution using Django.

# \- Connected booking workflows with email confirmation and PDF ticket generation.

# \- Organized the project into a Django project configuration and a dedicated tourism application.

# \- Used Python packages to support form handling, media processing, and PDF generation.


# \## 🔮 Future Improvements


# \- Add destination search and filtering.

# \- Improve mobile responsiveness and accessibility.

# \- Add online payment integration.

# \- Enhance booking history and trip management.

# \- Introduce automated tests for critical booking workflows.


# \## 👨‍💻 Author


# \*\*Kushal Sharma\*\*


# \- GitHub: \[@Kushal57169](https://github.com/Kushal57169)

# \- Project: \[Himachal Tourism](https://github.com/Kushal57169/Himachal-tourism)


# \---


# \*Built to make exploring Himachal Pradesh and planning travel more convenient.\*
