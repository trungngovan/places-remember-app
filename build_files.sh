npm ci
npm run build

echo "Copy favicon to static folder"
cp favicon.ico static

echo "Build and collect static files"
python manage.py collectstatic --noinput

