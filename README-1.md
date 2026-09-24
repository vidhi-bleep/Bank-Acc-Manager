# Bank Account Manager

A simple desktop GUI application built with **Python** and **PyQt6** that lets a user view account details, deposit money, and withdraw money from a small in-memory set of bank accounts.

## Features

- **View Account** — Look up an account by account number and display its details.
- **Deposit** — Add money to an existing account via a popup input dialog.
- **Withdraw** — Remove money from an account, with a balance check to prevent overdrafts.
- **Activity Log** — All actions are logged in a scrollable text panel within the app.
- Input validation for non-numeric or missing account numbers, with warning dialogs.

## Tech Stack

- Python 3.8+
- [PyQt6](https://pypi.org/project/PyQt6/) — GUI framework

## Screenshots

| View Account | Deposit | Insufficient Balance |
|---|---|---|
| ![View](screenshots/view_account.png) | ![Deposit](screenshots/deposit.png) | ![Insufficient Balance](screenshots/insufficient_balance.png) |

*(Add your screenshot images to a `screenshots/` folder in the repo for these to display.)*

## Getting Started

### Prerequisites
- Python 3.8 or higher installed

### Installation
```bash
git clone https://github.com/Vidhi-bleep/bank-account-manager.git
cd bank-account-manager
pip install -r requirements.txt
```

### Run the app
```bash
python bank_account_manager.py
```

## Sample Accounts

| Name | Account No. | Balance |
|---|---|---|
| Vidhi | 1001 | 20000 |
| Shloka | 1002 | 22000 |
| Prajakta | 1003 | 23000 |
| Pranjal | 1004 | 0 |
| Harsh | 1005 | 1000 |
| Ishant | 1006 | 100 |
| Queen Shivakshi | 1007 | 3000000 |

## Project Structure
```
bank-account-manager/
├── bank_account_manager.py   # Main application
├── requirements.txt          # Python dependencies
├── README.md
└── screenshots/              # App screenshots (optional)
```

## Future Enhancements

- Persist account data to a file or database instead of an in-memory list
- Add account creation and account deletion
- Add transaction history per account
- Add authentication/login before accessing accounts

## Author

Vidhi Upadhyay — CSE1021, Introduction to Problem Solving and Programming
[GitHub: @Vidhi-bleep](https://github.com/Vidhi-bleep)

## License

This project is for academic/educational purposes.
