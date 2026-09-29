# Problem Statement — Bank Account Manager

## The Problem

Many beginning programming exercises are limited to console input/output, making them feel disconnected to real-world applications. Banking operations such as check balances, deposits, and withdrawals are common operations in everyday life, but are non-trivial to implement securely and correctly.

This small project demonstrates a simple way to perform some basic banking operations on a set of sample accounts, while also enforcing some limitations and validations.

## The Solution

Bank Account Manager is a small Python desktop application developed using the PyQt6 framework. It provides a GUI for viewing, depositing, and withdrawing from a set of sample bank accounts. Features include:

- A dictionary-based account database storing name, account number, and balance

- A single account number input field used for all operations

- Separate dialogs for making deposits and withdrawals

- Contextual warnings for invalid input, not found accounts, and insufficient funds

- An activity log showing all performed operations

The application demonstrates proper use of Python functions to implement common banking operations such as deposits, withdrawals, and balance checks, while also showing how to implement simple input validation.

## Objectives

The project explores the following learning objectives:

1. Develop a Python graphical application for managing and demonstrating basic banking operations

2. Practice and demonstrate proficiency with common programming concepts like functions, conditionals, and data structures

3. Gain experience with the PyQt6 framework for developing GUI applications

4. Implement basic input validation and error handling

5. Show understanding of how fundamental programming concepts can be applied in real-world applications

## Validation Rules

The following input validations are implemented in the application:

- Account number input must be numeric or warning shown

- Invalid account number shows appropriate warning rather than crashing

- Cannot withdraw more than available balance (shows insufficient funds warning)

## Scope

The application is a single-user single-session desktop app that only stores account information in memory. It only implements basic operations against a fixed set of seven sample accounts. The focus of the project is to demonstrate proficiency with core programming concepts and a GUI framework, rather than implement production-level banking application features.

## Technologies

The application is implemented in Python using the PyQt6 framework for the GUI. There are plans to add file storage/database persistence in future iterations, but for now account data is stored in memory as a list of Python dictionaries.

## Possible Future Work

Some potential feature additions/enhancements that would be valuable to implement in future iterations of this project include:

1. Saving account data to file or database (e.g. SQLite)

2. Implement account creation and deletion features

3. Add transaction history for individual accounts

4. Add login/authentication system

5. Add currency formatting, localization, and multi-currency support

6. Package as executable (e.g. using PyInstaller)
