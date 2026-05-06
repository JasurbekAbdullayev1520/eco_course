# eco_course

## Media PDF import

If you already have PDF files under `media/lectures/`, `media/practice/`, or `media/resources/`, run:

```bash
python manage.py import_media_pdfs
```

This will create Django records linked to the existing files.

## PythonAnywhere notes

- Set `DEBUG=False` and `ALLOWED_HOSTS=myusername.pythonanywhere.com` in your `.env`
- In PythonAnywhere web settings, map `/media/` to the `media` directory for serving uploaded PDFs
