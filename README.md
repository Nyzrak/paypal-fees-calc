# 🖩 Paypal Goods & Services Calculator

This Django-Project is for calculating the Goods & Services fees when a buying a product via Paypal.

It gives you calculations for payments with:
* Friends & Family
* Goods & Services (Private sells over Facebook marketplace for example)
* Collecting donations
* Micropayments
* Payments with Dealer/Seller conditions (0€ - 2.000€)
* Payments with Dealer/Seller conditions (2.000,01€ - 5.000€)
* Payments with Dealer/Seller conditions (5.000,01€ - 25.000€)
* Payments with Dealer/Seller conditions (25.000,01€ - 100.000€)
* Payments with Dealer/Seller conditions (> 100.000€)

---

## 🚀 Getting Started

This project uses [`just`](https://github.com/casey/just) as a command runner to simplify development. All setup and common tasks are automated.

### Prerequisites

* Python 3.10+
* `python3-venv` (may be a separate package on some Linux distributions)
* [`just`](https://github.com/casey/just)

### Recommended Setup (with `just`)

This is the fastest and easiest way to get up and running.

**1. Install Dependencies**

Run the following command from the project root:

```bash
just install
```

This will automatically:

* Create a virtual environment in .venv.
* Install all required packages from requirements.txt.

**2. Run the development server**

```bash
just up
```
Your server is now running at http://127.0.0.1:8000/ or just http://localhost:8000.

**Note:** With this setup, you never need to run source .venv/bin/activate or deactivate yourself. just handles the virtual environment for you.

### 📖 Common Commands

All commands are run using `just [command]` from the project root.

| Command | Description |
| :--- | :--- |
| `just install` | Sets up the venv and installs all dependencies. |
| `just up` | Starts the Django development server. |
| `just test` | Runs the project's test suite. |
| `just migrate` | Applies any pending database migrations. |
| `just migrations` | Scans for model changes and creates new migration files. |
| `just cmd [args]` | Runs an arbitrary `manage.py` command (e.g., `just cmd createsuperuser`). |
| `just clean` | Removes the `.venv` and all `__pycache__` directories. |


### Manual Setup (Without `just`)

If you prefer not to use `just`, you can follow the traditional Python setup steps.

<details>
<summary>Click to view manual setup instructions</summary>

1.  **Create the virtual environment:**
    ```bash
    python3 -m venv .venv
    ```
2.  **Activate the virtual environment:**
    ```bash
    source .venv/bin/activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the server:**
    ```bash
    python manage.py runserver
    ```
5.  **When you are finished, deactivate:**
    ```bash
    deactivate
    ```
</details>

### 🤝 Contributing

**Feel free to contribute to this project and help me make it even better!**

I will provide a domain and a webserver where this project will be hosted.

If you find any errors or have ideas, you can always let me know by:

* Forking the repo and submitting a pull request.

* Creating an issue in the repository.

* Texting me on Discord.

I'll appreciate any and all help :)
