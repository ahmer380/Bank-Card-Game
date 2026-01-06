# Test Guide

## Writing tests the Test-Driven way
Test-Driven Development (TDD) is the act of writing the tests prior to writing the code, rather than the other way around. I particularly am a strong advocate for TDD since it encourages clear problem definition and provides fast feedback that catches defects early-on in development.

NOTE: Due to time constraints, these tests are intentionally not exhaustive but rather focus on the core, high-impact mechanics needed for the task at hand.

## How to Run Tests

### All tests
```powershell
python -m unittest
```

### One test file
```powershell
python -m unittest tests.test_card
```

### One test case
```powershell
python -m unittest tests.test_card.TestCard.test_card_value
```