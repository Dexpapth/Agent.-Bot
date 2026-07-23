# EMI Calculator — Sub-task 1 (Sprint 2)

**Owner:** DEXPATH (Project Lead) — implemented/finalized by Ravi Teja
**Status:** ✅ Complete
**Files touched:**
- `python_versions/chatbot_core.py`
- `python_versions/flask_app/templates/index.html`

---

## What it does

Replaces the old placeholder EMI flow with a fully working, in-chat EMI calculator. Users get a real calculation (not a "coming soon" message), with input validation and a visual breakdown of principal vs. interest.

## How to trigger it

Either:
- Type **`emi`** in the chat box, or
- Click the **🧮 EMI Calculator** button in the Quick Actions sidebar

Both now correctly open the calculator panel. (Previously, typing just "emi" was being caught by the general `loan` intent instead of opening the calculator — this was fixed by moving the `"emi"` keyword into the `emi_calc` intent's key list in `chatbot_core.py`.)

## Inputs

| Field | Description | Validation |
|---|---|---|
| Loan Amount (INR) | Principal loan amount | Must be a positive number, no letters/symbols |
| Annual Interest Rate (%) | Yearly interest rate | Must be zero or positive, no letters/symbols |
| Loan Tenure (months) | Repayment period | Must be a positive whole number, no letters/symbols |

Negative signs, letters, and symbols are stripped/rejected as the user types or on submit. Invalid input shows a clear red inline error instead of failing silently or crashing.

## Formula

Standard reducing-balance EMI formula:

```
EMI = P × r × (1 + r)^n / ((1 + r)^n − 1)
```

Where:
- `P` = principal (loan amount)
- `r` = monthly interest rate (annual rate ÷ 12 ÷ 100)
- `n` = tenure in months

If the interest rate is `0`, EMI falls back to a simple `P / n` split (no compounding).

Implemented server-side in `calculate_emi()` inside `chatbot_core.py`, and served via the Flask `/emi` POST route in `app.py`.

## Output

On successful calculation, the panel displays:
- **Monthly EMI**
- **Total Interest**
- **Total Repayment**
- A color-coded **principal vs. interest bar** with percentage legend, so users can visually see how much of their repayment is principal vs. interest

## Testing it locally

```bash
cd python_versions/flask_app
pip install flask
python app.py
```

Then open `http://localhost:5000`, log in (`customer` / `bank123`), and type `emi` in chat.

**Test cases covered:**
1. Valid input (e.g. 500000 / 9.5 / 60) → correct EMI, interest, repayment, and visual bar
2. Letters/symbols in any field → red validation error, no crash
3. Negative numbers → blocked at input level
4. Zero or empty tenure/principal → rejected with a clear message
5. Server/connection failure → graceful error message instead of a silent hang

## Notes for the rest of the team

- No backend routes were added/removed — `/emi` and `/chat` already existed and are unchanged in behavior, only the intent-matching logic and front-end form were updated.
- Member 2 (Dashboard) and Member 3 (Voice Input) should pull the latest `index.html` before starting, since this sub-task was scheduled first in Week 1 for exactly that reason.
