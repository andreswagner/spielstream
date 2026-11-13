# Publishing spielstream 0.0.1 to PyPI

1. Create a PyPI account at https://pypi.org and enable two-factor authentication.
2. Create an API token (Account settings → API tokens), scope "Entire account".
3. From this folder:

   ```
   python -m pip install --upgrade build twine
   python -m build
   python -m twine check dist/*
   python -m twine upload dist/*
   ```

   When asked for credentials, use `__token__` as the username and paste the token as
   the password.
4. Check https://pypi.org/project/spielstream/ and test: `pip install spielstream && spielstream info`.
5. After the upload, delete the account-wide token and create one scoped to the
   `spielstream` project only (or set up Trusted Publishing from GitHub Actions).
