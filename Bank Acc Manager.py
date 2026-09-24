import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QTextEdit, QMessageBox, QGroupBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

Accounts = [
    {'name': 'Vidhi', 'acc_no': 1001, 'balance': 20000},
    {'name': 'Shloka', 'acc_no': 1002, 'balance': 22000},
    {'name': 'Prajakta', 'acc_no': 1003, 'balance': 23000},
    {'name': 'Pranjal', 'acc_no': 1004, 'balance': 0},
    {'name': 'Harsh', 'acc_no': 1005, 'balance': 1000},
    {'name': 'Ishant', 'acc_no': 1006, 'balance': 100},
    {'name': 'Queen Shivakshi', 'acc_no': 1007, 'balance': 3000000},
]


def find_account(acc_no, accounts):
    for acc in accounts:
        if acc['acc_no'] == acc_no:
            return acc
    return None


class BankApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bank Account Manager")
        self.setMinimumWidth(420)
        self.build_ui()

    def build_ui(self):
        main_layout = QVBoxLayout()

        title = QLabel("Bank Account Manager")
        title.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title)

        # Account number input
        acc_group = QGroupBox("Account")
        acc_layout = QHBoxLayout()
        acc_layout.addWidget(QLabel("Account No:"))
        self.acc_input = QLineEdit()
        self.acc_input.setPlaceholderText("e.g. 1001")
        acc_layout.addWidget(self.acc_input)
        acc_group.setLayout(acc_layout)
        main_layout.addWidget(acc_group)

        # Action buttons
        btn_layout = QHBoxLayout()
        self.view_btn = QPushButton("View")
        self.deposit_btn = QPushButton("Deposit")
        self.withdraw_btn = QPushButton("Withdraw")
        btn_layout.addWidget(self.view_btn)
        btn_layout.addWidget(self.deposit_btn)
        btn_layout.addWidget(self.withdraw_btn)
        main_layout.addLayout(btn_layout)

        self.view_btn.clicked.connect(self.view_account)
        self.deposit_btn.clicked.connect(self.deposit_money)
        self.withdraw_btn.clicked.connect(self.withdraw_money)

        # Output log
        main_layout.addWidget(QLabel("Log:"))
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        main_layout.addWidget(self.output)

        # Exit button
        exit_btn = QPushButton("Exit")
        exit_btn.clicked.connect(self.close)
        main_layout.addWidget(exit_btn)

        self.setLayout(main_layout)

    def get_acc_no(self):
        text = self.acc_input.text().strip()
        if not text.isdigit():
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid account number.")
            return None
        return int(text)

    def log(self, message):
        self.output.append(message)

    def view_account(self):
        acc_no = self.get_acc_no()
        if acc_no is None:
            return
        acc = find_account(acc_no, Accounts)
        if acc:
            self.log(f"Account: {acc}")
        else:
            self.log(f"No account found with number {acc_no}")
            QMessageBox.warning(self, "Not Found", f"No account found with number {acc_no}")

    def deposit_money(self):
        acc_no = self.get_acc_no()
        if acc_no is None:
            return
        acc = find_account(acc_no, Accounts)
        if not acc:
            QMessageBox.warning(self, "Not Found", f"No account found with number {acc_no}")
            return

        amount_text, ok = self.prompt_amount("Deposit Amount", "Enter amount to deposit:")
        if not ok:
            return
        acc['balance'] += amount_text
        self.log(f"Amount deposited: {acc}")

    def withdraw_money(self):
        acc_no = self.get_acc_no()
        if acc_no is None:
            return
        acc = find_account(acc_no, Accounts)
        if not acc:
            QMessageBox.warning(self, "Not Found", f"No account found with number {acc_no}")
            return

        amount_text, ok = self.prompt_amount("Withdraw Amount", "Enter amount to withdraw:")
        if not ok:
            return
        if amount_text > acc['balance']:
            QMessageBox.warning(self, "Insufficient Balance", "Withdrawal amount exceeds balance.")
            return
        acc['balance'] -= amount_text
        self.log(f"Amount withdrawn: {acc}")

    def prompt_amount(self, title, label):
        from PyQt6.QtWidgets import QInputDialog
        value, ok = QInputDialog.getInt(self, title, label, min=1, max=100000000)
        return value, ok


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BankApp()
    window.resize(480, 400)
    window.show()
    sys.exit(app.exec())
