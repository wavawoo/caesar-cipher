# Caesar Cipher

A simple and efficient implementation of the Caesar cipher in Python.

## Description

The Caesar cipher is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

This repository contains two implementations:

- **Basic version** (`caesar.py`) - Pure Caesar cipher implementation
- **Advanced version** (`caesar_advanced.py`) - Extended version with brute force cracking

## Files

- `caesar.py` - Basic implementation with encryption/decryption only
- `caesar_advanced.py` - Advanced version with brute force attack capability

## Features

### Both versions include:
- **Text encryption** with a given shift value
- **Text decryption** with a given shift value
- **Multi-language support** for both English and Russian alphabets
- **Preserves case** - uppercase and lowercase letters remain as is
- **Non-letter characters unchanged** - spaces, punctuation, and numbers are preserved

### Advanced version additionally includes:
- **Brute force attack** - automatic cracking by trying all possible shifts
- **Readability scoring** - intelligent ranking of decryption results
- **Interactive menu** - unified interface for all operations
- **Best match detection** - automatically finds the most probable solution
