#!/bin/bash
exec gunicorn image_annotate.wsgi:application \
    --name furuno \
    --bind 0.0.0.0:8000 \
    --workers 5 \
    --timeout 0 \
"$@"
