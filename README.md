# REAPR-web

A Flask-based web application that provides a searchable, filterable interface for viewing and exporting data from a MySQL database. Originally developed for the Skinwalker Ranch Insiders community to log and review observations from YouTube livestreams.

## Technology Stack

- **Backend**: Python 3.8, Flask
- **Database**: MySQL
- **Frontend**: HTML, jQuery, DataTables (for interactive tables)
- **Deployment**: Docker

## Features

- **Data Visualization**: Display database records in an interactive, sortable table
- **Filtering**: Filter records by category (Events, Thoughts, Requests, Feedback)
- **CSV Export**: Export all data to CSV format for external analysis
- **RESTful Routes**: Clean API endpoints for different views
- **Containerized**: Docker support for easy deployment

## Project Structure

```
reapr-web/
├── app.py              # Main Flask application
├── settings.py         # Database configuration
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker container configuration
├── template/
│   └── table.html      # HTML template with DataTables
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.8+
- MySQL database
- Docker (optional)

### Local Development

1. Clone the repository:
   ```bash
   git clone git@github.com:skinwalker-ranch-insiders/reapr-web.git
   cd reapr-web
   ```

2. Configure database settings in `settings.py`:
   ```python
   db_server = 'your-server-ip'
   db_user = 'your-username'
   db_passwd = 'your-password'
   db_name = 'reapr_db'
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser at `http://localhost:5000`

### Docker Deployment

```bash
docker build -t reapr-web .
docker run --name reapr-web -d -p 5000:5000 reapr-web
```

Then visit `http://[docker-ip]:5000`

## API Endpoints

| Route | Description |
|-------|-------------|
| `/` | View all records |
| `/events/` | Filter by Events |
| `/thoughts/` | Filter by Thoughts |
| `/requests/` | Filter by Requests |
| `/feedback/` | Filter by Feedback |
| `/export/` | Export all data as CSV |

## Skills Demonstrated

- Flask web application development
- MySQL database integration
- HTML template rendering with Jinja2
- jQuery and DataTables integration
- CSV generation and file downloads
- Docker containerization
- RESTful API design

## License

MIT License

## Author

Robert Kris Davies
