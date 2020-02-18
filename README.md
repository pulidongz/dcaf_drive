# dcaf_drive

Landsat data storage and automated processing of landsat data for DCAF Project of IESM.

## running the app
```json
cd dcaf_drive
python3 manage.py runserver

celery -A dcaf_drive worker -l info
celery -A dcaf_drive beat -l info
```

## dependencies
```json
# Install Redis as a Celery 'broker'
sudo apt install redis-server

# Enable redis to start on system reboot
sudo systemctl enable redis-server.service

```