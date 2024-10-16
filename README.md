# Dudoxx Audio Manager

## Overview
The Dudoxx Audio Manager module is designed to manage a vast collection of vocal recordings, including their transcriptions, translations, chunks, updates, and improvements. It provides a comprehensive solution for organizing and securing audio data, integrating with cloud storage, and ensuring seamless access control.

## Features
- Manage audio recordings with metadata, transcriptions, and translations.
- Organize recordings into folders for better management.
- Implement access control for different user roles.
- Custom widgets for audio playback and editing.
- Integration with cloud storage for secure data management.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Dudoxx/dudoxx_audio_manager.git
   ```
2. Navigate to the Odoo addons directory and copy the module:
   ```bash
   cp -r dudoxx_audio_manager /path/to/your/odoo/addons/
   ```
3. Install the required dependencies and update the Odoo apps list.

## Configuration
- Configure the database and cloud storage settings in the `.env` file:
  ```plaintext
  DB_HOST=localhost
  DB_PORT=5432
  DB_NAME=dudoxx_audio_manager
  DB_USER=your_username
  DB_PASSWORD=your_password

  CLOUD_STORAGE_URL=https://your-cloud-storage-url
  CLOUD_STORAGE_KEY=your_cloud_storage_key
  CLOUD_STORAGE_SECRET=your_cloud_storage_secret
  ```

## Usage
- Access the module from the Odoo interface to upload, manage, and organize audio recordings and their associated data.
- Use the provided menu entries to navigate through audio recordings, translations, chunks, and folders.

## Testing
To run the tests, use the following command:
```bash
odoo-bin test -d your_database_name -i dudoxx_audio_manager
```

## License
This module is licensed under the Dudoxx UG (GmbH) license.

## Acknowledgments
- Developed by Walid Boudabbous, Dudoxx UG (GmbH).
- For more information, visit [Dudoxx](https://www.dudoxx.com).
