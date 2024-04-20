# Simple Event Management System
## Setup Instructions

### 1. Clone the repository using https or ssh

```bash
git clone https://github.com/futurezayka/event_management_api.git

git clone git@github.com:futurezayka/event_management_api.git
```
### 2. Create .env file
  Use the .env.example file to create your own

### 3. Run this command to build docker image
```bash
sudo docker-compose --up --build
```

### 4. Run this commands to make and apply migrations
```bash
sudo docker-compose run web python manage.py makemigrations
sudo docker-compose run web python manage.py migrate
```

### 5. Run this command to create a superuser
```bash
sudo docker-compose run web python manage.py createsuperuser
```
### 6. The development server should be running at http://localhost:8000/

# API Endpoints

## User Management

- **Create User**
  - **Method:** POST
  - **URL:** `/api/user/register/`
  - **Description:** Register a new user.
  - **Request Body:** JSON object with user data (email, password).
  - **Permission:** Accessible to all.

- **User Login**
  - **Method:** POST
  - **URL:** `/api/user/login/`
  - **Description:** Log in an existing user.
  - **Request Body:** JSON object with user data (email, password).
  - **Permission:** Accessible to all.

## Event Management

- **List Events**
  - **Method:** GET
  - **URL:** `/api/events/`
  - **Description:** Get a list of all events.
  - **Permission:** Authenticated users.

- **Retrieve Event Information**
  - **Method:** GET
  - **URL:** `/api/events/{event_id}/`
  - **Description:** Get detailed information about a specific event by its ID.
  - **Permission:** Authenticated users.

- **Search Events**
  - **Method:** GET
  - **URL:** `/api/events/search?q={search_query}`
  - **Description:** Search events by title, description, or location.
  - **Permission:** Authenticated users.

- **Register for Event**
  - **Method:** POST
  - **URL:** `/api/event-registration/`
  - **Description:** Register for participation in an event.
  - **Request Body:** JSON object with event ID (event).
  - **Permission:** Authenticated users.

- **Update Event**
  - **Method:** PUT
  - **URL:** `/api/events/{event_id}/`
  - **Description:** Update details of a specific event.
  - **Permission:** Event organizer or admin.

- **Delete Event**
  - **Method:** DELETE
  - **URL:** `/api/events/{event_id}/`
  - **Description:** Delete a specific event.
  - **Permission:** Event organizer or admin.
