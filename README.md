# dj_small_shop

## Setup Instructions

### Prerequisites
Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

### Install Dependencies
 
### Go to Terminal 

1. **Create a Virtual Environment** (recommended):

   ```
    python -m venv venv
    ```

2. **Activate the Virtual Environment**:

    - On Windows:
      ```
      venv\Scripts\activate
      ```

    - On macOS and Linux:
      ```
      source venv/bin/activate
      ```
      
3. **Install Django Framework**

    ```
   pip install django
    ``` 
   
3. **Install Django REST Framework**

    ```
   pip install djangorestframework
    ``` 

4. **Install Pillow Library**
    
    ```
    pip install pillow
    ```
   
5. **Install PDF Library**
    ```
   pip install xhtml2pdf
    ```

6. **Install Django Cross-Origin Resource Sharing (CORS)**
    ```
    pip install django-cors-headers
    ```


7. **Project Setup**
    ```
    django-admin startproject config .
    ```


8. **Create Backend App**
    ```
    python manage.py startapp backend
    ```


9. **Create API V1 App**
    ```
    python manage.py startapp api_v1
    ```

10. **Create API V2 App**
    ```
    python manage.py startapp api_v2
    ```

3. **Create Migrations**:

    Run the following command to create new migration files based on the changes made to your models:

   - To create migrations for all apps:
    ```
    python manage.py makemigrations
    ``` 

    - To create migrations for a specific app (e.g., `backend`):
   
    ```
    python manage.py makemigrations backend
    ```

    This command will detect any changes to your models and create migration files in the `migrations` folder of each app.

    
12. **Apply Migrations**:

    Make sure to apply database migrations to set up your database schema:

    ```
    python manage.py migrate
    ```
   
11. **Install the Required Dependencies**:

    If you have a `requirements.txt` file, install the dependencies by running:

    ```
    pip install -r requirements.txt
    ```

4. **Run the Development Server**:

    Start the Django development server:

    ```
    python manage.py runserver
    ```
   
5. **Access the Application**:

    Open your web browser and navigate to:

    ```
    http://127.0.0.1:8000/
    ```

    To access the Django admin interface, go to:

    ```
    http://127.0.0.1:8000/admin/
    ```
   
3. **Run the Development Server**

    Start the Django development server with a specific IP address and port. By default, Django runs on `127.0.0.1:8000`, but you can change this to allow access from other devices on your network or to specify a different port.

    - To run the server on all available IP addresses (useful for accessing it from other devices on the same network), use:
      ```
      python manage.py runserver 0.0.0.0:8000
      ```

    - To run the server on a specific IP address and port (e.g., `192.168.1.100` and port `8000`), use:
      ```
      python manage.py runserver 192.168.1.100:8000
      ```

    Replace `192.168.1.100` with the IP address you want to use and `8000` with your desired port number.


4. **Access the Application**:

    - If you ran the server on `0.0.0.0:8000`, open your web browser and navigate to:
      ```
      http://<your-local-ip>:8000/
      ```
      Replace `<your-local-ip>` with your local IP address (e.g., `192.168.1.100`).

    - If you ran the server on a specific IP address, use that IP address and port in your browser:
      ```
      http://192.168.1.100:8000/
      ```

    - To access the Django admin interface, go to:
      ```
      http://<your-local-ip>:8000/admin/
      ```
   
### Stopping the Server

To stop the Django development server, press `Ctrl+C` in the terminal where the server is running.

For more details on running the Django development server, refer to the [Django documentation on the development server](https://docs.djangoproject.com/en/stable/ref/django-admin/#runserver).