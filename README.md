# test_project
 
# 🖥️ Deploy to Server with Available Port

## 📌Set up the Application on the Server

**1. Open Terminal**

**2. Navigate to the Directory to Clone the Project**

**3. Set Up Python Environment, including Python, `pip`, and `virtualenv`**

   - Linux/macOs
     ```bass
     sudo apt-get update
     sudo apt-get install python3-pip
     sudo pip3 install virtualenv
     ```
   - Windows
     ```bass
     python --version
     pip --version
     pip install virtualenv
     ```

**4. Clone Project from Repository GitHub and Navigate to the Directory**

```bass
git clone https://github.com/vionaaindah/django_rest_framework_crud_api.git
cd django_rest_framework_crud_api
```

**5. Create an Isolated Python Environment**
   - Linux/macOs
     ```bass
     virtualenv env
     ```
   - Windows
     ```bass
     python -m venv env
     ```

**6.Activate an Isolated Python Environment**
   - Linux/macOs
     ```bass
     source env/bin/activate
     ```
   - Windows
     ```bass
     env\scripts\activate
     ```

**7. Install dependencies**

```bass
pip install -r requirements.txt
```

**8. Open **`settings.py`** File**
   - Linux/macOs
     ```bass
     sudo vim test_project/settings.py
     ```
     <b>Note : </b> To **`editing file`**  type **`i`** and to **`save file`** click Esc and type **`:wq`**
   - Windows
     
     Open settings.py file in test_project folder


**9. Configuring **`settings.py`****

Set all requirements needed

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<db_name>',
        'USER': '<db_username>',
        'PASSWORD': '<db_password>',
        'HOST': '<db_host>',
        'PORT': '3306',
    }
}
```

Save **`settings.py`**

**10. Run the Django migrations to set up your models**

```bash
python manage.py makemigrations
python manage.py makemigrations users
python manage.py migrate
```

**11. Run Application**
   - Start on Local Machine
     ```bass
     python manage.py runserver
     ```
   - Start with External IP
     ```bass
     python manage.py runserver 0.0.0.0:{port_available}
     ```
   - Linux (Run in the background)
     ```bass
     screen
     source env/bin/activate
     python manage.py runserver 0.0.0.0:{port_available}
     ```
     <b>Note:</b> use **`screen -r`** to enter screen already exist and **`ctrl+a d`** to exit from screen
