#!/bin/bash
# backup.sh: Automates data backup and disaster recovery procedures.

echo "Starting backup process for SkyOptima data..."

# Backup database (example using pg_dump)
pg_dump -h db.skyoptima.com -U skyoptima_user -d skyoptima_db > backups/skyoptima_db_$(date +%F).sql

# Backup important files (using tar)
tar -czvf backups/skyoptima_files_$(date +%F).tar.gz config/ src/ docs/

echo "Backup completed successfully."
