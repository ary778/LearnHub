# LearnHub

A modern, full-stack web application that aggregates learning resources from YouTube, Google Books, and Codeforces into a single, powerful search platform.

## Key Features

-   **Multi-Source Aggregation**: Fetches and displays content from YouTube, Google Books, and Codeforces (problems & blogs) in one place.
-   **Performance Caching**: Implements Django's caching framework to reduce external API calls and improve response times on repeated searches.
-   **RESTful API**: Includes a dedicated API endpoint built with Django REST Framework to serve search results in JSON format.
-   **Modern UI/UX**: A fully responsive, custom-designed frontend featuring a unique, animated homepage and a clean, light-themed results page.

---
## Tech Stack

| Category  | Technologies                                                              |
| :-------- | :------------------------------------------------------------------------ |
| **Backend** | Python, Django, Django REST Framework, PostgreSQL                         |
| **Frontend** | HTML5, CSS3, JavaScript, `tsParticles.js`, `Typed.js`                     |
| **APIs** | YouTube Data API v3, Google Books API, Codeforces API                     |

---
## Getting Started

To get a local copy up and running, follow these steps.

### Prerequisites

-   Python 3.9+
-   Git
-   PostgreSQL database instance

### Installation

1.  **Clone the repo**
    ```sh
    git clone [https://github.com/ary778/learnhub.git](https://github.com/ary778/learnhub.git)
    cd learnhub
    ```
2.  **Create and activate a virtual environment**
    ```sh
    # Windows
    python -m venv .venv
    .venv\Scripts\activate

    # macOS/Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```
3.  **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```
4.  **Set up environment variables**
    -   Create a `.env` file in the project root.
    -   Add your secret keys and database credentials using `.env.example` as a template:
        ```env
        SECRET_KEY='your-django-secret-key'
        YOUTUBE_API_KEY='your-youtube-api-key'
        GOOGLE_BOOKS_API_KEY='your-google-books-api-key'
        DB_NAME='your-db-name'
        DB_USER='your-db-user'
        DB_PASSWORD='your-db-password'
        ```
5.  **Run database migrations**
    ```sh
    python manage.py migrate
    ```
6.  **Run the development server**
    ```sh
    python manage.py runserver
    ```
    The site will be available at `http://127.0.0.1:8000`.

---
## API Usage

The REST API endpoint is available for fetching search results programmatically.

-   **Endpoint**: `/api/search/`
-   **Method**: `GET`
-   **Query Parameter**: `q` (your search term)
-   **Example**: `http://127.0.0.1:8000/api/search/?q=data+structures`

---
## Demo
<img width="1919" height="976" alt="Learnhub_home" src="https://github.com/user-attachments/assets/c7ace926-c5a6-4e14-ab7f-f0efd0cacd82" />
<img width="1898" height="977" alt="result1" src="https://github.com/user-attachments/assets/1dec79f7-d64a-42b1-8fc4-f51ab42c5457" />
<img width="1896" height="976" alt="result2" src="https://github.com/user-attachments/assets/256a148c-fb6c-4883-b7d5-c8089f54f528" />

---
## Contact

[cite_start]**Aryan Suthar** - [linkedin.com/in/aryansuthar](https://linkedin.com/in/aryansuthar) [cite: 3]
