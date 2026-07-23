from datetime import datetime

CREDENTIALS = {
    "customer": {"username": "customer", "password": "bank123"},
    "employee": {"username": "employee", "password": "emp456"},
    "admin":    {"username": "admin",    "password": "admin789"},
}

FILLER = {
    "i", "my", "me", "the", "a", "an", "is", "are", "was",
    "please", "can", "you", "what", "how", "about", "want",
    "to", "do", "need", "help", "with", "and", "or", "in",
    "for", "of", "on", "at", "by", "from", "this", "that",
    "there", "here", "get", "show", "tell", "give",
}

KNOWLEDGE_BASE = [
    {
        "keys": ["hello", "hi", "hey", "good", "morning", "afternoon",
                 "evening", "start", "begin", "welcome"],
        "intent": "greeting",
    },
    {
        "keys": ["balance", "account", "funds", "money", "much", "available"],
        "intent": "balance",
    },
    {
        "keys": ["transfer", "send", "payment", "pay", "wire",
                 "remittance", "imps", "neft", "rtgs", "upi"],
        "intent": "transfer",
    },
    {
        "keys": ["statement", "history", "transactions", "record",
                 "mini", "past", "last"],
        "intent": "statement",
    },
    {
        "keys": ["fraud", "scam", "dispute", "unauthorized",
                 "suspicious", "chargeback", "hacked", "stolen", "unknown"],
        "intent": "fraud",
    },
    {
        "keys": ["loan", "borrow", "mortgage", "home",
                 "car", "personal", "credit", "instalment"],
        "intent": "loan",
    },
    {
        "keys": ["emi calculator", "calculate emi", "monthly payment",
                 "calculate loan", "instalment calculator", "emi"],
        "intent": "emi_calc",
    },
    {
        "keys": ["block", "freeze", "lost", "stolen", "disable",
                 "debit", "card", "cancel"],
        "intent": "block_card",
    },
    {
        "keys": ["open", "new", "create", "savings", "current",
                 "zero", "salary", "nri"],
        "intent": "new_account",
    },
    {
        "keys": ["kyc", "know", "customer", "aadhar", "aadhaar",
                 "pan", "identity", "verification", "document", "passport"],
        "intent": "kyc",
    },
    {
        "keys": ["interest", "rate", "fd", "fixed", "deposit",
                 "saving", "roi", "percent", "return"],
        "intent": "rates",
    },
    {
        "keys": ["atm", "branch", "nearest", "location", "find",
                 "where", "close", "nearby"],
        "intent": "atm",
    },
    {
        "keys": ["net", "internet", "online", "login", "password",
                 "reset", "otp", "banking", "forgot"],
        "intent": "net_banking",
    },
    {
        "keys": ["error", "system", "failed", "decline", "reject",
                 "issue", "working", "problem", "bug", "down"],
        "intent": "error",
    },
    {
        "keys": ["lookup", "find", "search", "customer", "details",
                 "view", "check", "acc", "account"],
        "intent": "lookup",
    },
    {
        "keys": ["report", "daily", "generate", "analytics",
                 "summary", "stats", "dashboard"],
        "intent": "report",
    },
    {
        "keys": ["status", "server", "health", "uptime",
                 "maintenance", "downtime", "live"],
        "intent": "system",
    },
    {
        "keys": ["help", "options", "menu", "commands",
                 "services", "what", "can", "do"],
        "intent": "help",
    },
    {
        "keys": ["thank", "thanks", "great", "awesome",
                 "perfect", "good", "nice", "well"],
        "intent": "thanks",
    },
    {
        "keys": ["bye", "goodbye", "exit", "close",
                 "quit", "done", "that's all", "thatall"],
        "intent": "bye",
    },
]


def reply_greeting(role):
    hour = datetime.now().hour
    if hour < 12:
        greet = "Good morning"
    elif hour < 17:
        greet = "Good afternoon"
    else:
        greet = "Good evening"

    return (
        f"{greet}! Welcome to BankBot AI.\n"
        f"I'm your intelligent banking assistant. You are logged in as: {role.upper()}\n\n"
        "How can I help you today? You can ask about:\n"
        "  Check my balance\n"
        "  Transfer money\n"
        "  Loan information\n"
        "  Block my card\n"
        "  Interest rates\n"
        "  Find nearest ATM\n"
        "  Report fraud\n"
        "  Type 'help' for the full list."
    )


def reply_balance(role):
    if role in ("employee", "admin"):
        return (
            "Customer Balance Lookup\n"
            "Enter the Account Number to view balance.\n"
            "Example: lookup ACC-78234\n"
            "Or type 'system report' for a full balance report."
        )
    return (
        "Account Balances  (as of " + datetime.now().strftime("%d %b %Y") + ")\n"
        "Savings Account   XXXX-XXXX-7823   INR 1,24,500.00   [Active]\n"
        "Current Account   XXXX-XXXX-3410   INR    38,250.75   [Active]\n"
        "Fixed Deposit     FD-2024-00412    INR 2,00,000.00   [Locked]\n"
        "Tip: Type 'show statement' to see recent transactions."
    )


def reply_transfer(role):
    return (
        "Fund Transfer Options\n"
        "  IMPS  — Instant  | 24x7  | Up to INR 5,00,000\n"
        "  NEFT  — Batched  | Mon-Sat | Any amount\n"
        "  RTGS  — Real-time| Bank hours | Min INR 2,00,000\n"
        "  UPI   — Instant  | 24x7  | Up to INR 1,00,000\n"
        "WARNING: Always verify recipient details before confirming.\n"
        "Transfers cannot be reversed once processed.\n"
        "To initiate, visit the secure portal or your branch."
    )


def reply_statement(role):
    return (
        "Mini Statement — Last 5 Transactions\n"
        "  18 Jun  UPI — Swiggy              -  INR    480\n"
        "  17 Jun  Salary Credit             +  INR 55,000\n"
        "  16 Jun  NEFT — Housing Loan       -  INR 18,500\n"
        "  15 Jun  ATM Withdrawal            -  INR  3,000\n"
        "  14 Jun  Interest Credit — FD      +  INR  1,250\n"
        "For full statement, visit your branch or net banking portal.\n"
        "Type 'email statement' to receive it at your registered email."
    )


def reply_loan(role):
    return (
        "Loan Products & Interest Rates\n"
        "  Home Loan        8.40% per annum\n"
        "  Car Loan         9.25% per annum\n"
        "  Personal Loan   11.50% per annum\n"
        "  Education Loan   8.65% per annum\n"
        "  Gold Loan        7.90% per annum\n"
        "Rates are indicative and subject to credit assessment.\n"
        "Processing fee: 0.5% to 1%\n"
        "Type 'emi calculator' to calculate your monthly instalment."
    )


def reply_emi_calc():
    return "__EMI_CALC__"


def reply_block_card(role):
    return (
        "Block / Freeze Card\n"
        "  Card ending in:  **** 9201\n"
        "  Type:            Debit Card (Visa)\n"
        "  Current status:  ACTIVE\n"
        "WARNING: Once blocked, you must visit a branch or call\n"
        "1800-XXX-XXXX to reactivate your card.\n\n"
        "To confirm block, type: CONFIRM BLOCK\n"
        "To report fraud instead, type: report fraud"
    )


def reply_new_account(role):
    return (
        "Open a New Account\n"
        "  Savings Account   Min balance: INR 1,000\n"
        "  Current Account   Min balance: INR 10,000\n"
        "  Salary Account    Zero balance required\n"
        "  NRI Account       Special NRI interest rates\n"
        "Documents required: Aadhaar, PAN, Photograph, Address Proof\n"
        "Type 'kyc' for document requirements.\n"
        "Visit your nearest branch or apply online at the portal."
    )


def reply_kyc(role):
    return (
        "KYC Requirements\n"
        "  Identity Proof   Aadhaar / Passport / Voter ID\n"
        "  PAN Card         Mandatory for all accounts\n"
        "  Address Proof    Utility bill / Aadhaar\n"
        "  Photograph       2 recent passport-size photos\n"
        "  Video KYC        Available online (no branch visit)\n"
        "To schedule Video KYC, visit the net banking portal.\n"
        "Type 'open account' to start the account opening process."
    )


def reply_rates(role):
    return (
        "Current Interest Rates  (effective 01 Jun 2026)\n"
        "  Savings Account       3.50% per annum\n"
        "  Fixed Deposit 1 yr    7.10% per annum\n"
        "  Fixed Deposit 3 yr    7.50% per annum\n"
        "  Fixed Deposit 5 yr    7.75% per annum\n"
        "  Recurring Deposit     6.80% per annum\n"
        "  Senior Citizen FD     +0.50% extra\n"
        "Rates subject to change. Contact branch for latest rates."
    )


def reply_atm(role):
    return (
        "Nearest ATM / Branch Locations\n"
        "  ATM  — MG Road        0.3 km  Open 24x7\n"
        "  Branch — Koramangala  1.2 km  Mon-Sat 9am-4pm\n"
        "  ATM  — Forum Mall     1.5 km  Open 24x7\n"
        "  Branch — Indiranagar  2.1 km  Mon-Sat 9am-4pm\n"
        "Based on your registered address.\n"
        "For more locations, visit the bank website."
    )


def reply_fraud(role):
    return (
        "FRAUD & DISPUTE ALERT LOGGED\n"
        "  24x7 Fraud Hotline   1800-XXX-FRAUD\n"
        "  Email                fraud@bankbot.in\n"
        "  Response Time        Under 2 hours\n"
        "IMPORTANT: Do NOT share OTP, CVV, or PIN with anyone,\n"
        "including bank staff. The bank will NEVER ask for these.\n\n"
        "Your report has been logged. A fraud officer will contact\n"
        "you within 2 hours on your registered mobile number."
    )


def reply_net_banking(role):
    return (
        "Net Banking / Online Banking Support\n"
        "  Password Reset    Visit portal > Forgot Password\n"
        "  OTP Issues        Check registered mobile / email\n"
        "  Account Locked    Call 1800-XXX-XXXX to unlock\n"
        "  Login Issues      Clear browser cache and retry\n"
        "Portal: https://netbanking.bankbot.in\n"
        "Support available Mon-Sat 8am to 8pm."
    )


def reply_error(role):
    if role == "customer":
        return (
            "We're sorry you're experiencing an issue.\n"
            "Please contact our support team:\n"
            "  Phone: 1800-XXX-XXXX\n"
            "  Email: support@bankbot.in\n"
            "  Hours: Mon-Sat 8am to 8pm"
        )
    return (
        "System Error Handler  [EMPLOYEE / ADMIN MODE]\n"
        "  Error Log ID:     ERR-" + datetime.now().strftime("%Y%m%d%H%M") + "\n"
        "  Timestamp:        " + datetime.now().strftime("%d %b %Y %H:%M:%S") + "\n"
        "Recommended actions:\n"
        "  1. Check system status dashboard\n"
        "  2. Restart the affected service module\n"
        "  3. Escalate to Level 2 if unresolved in 15 minutes\n"
        "  4. Log ticket in the internal helpdesk system"
    )


def reply_lookup(role):
    if role == "customer":
        return "Sorry, customer lookup is available for bank staff only."
    return (
        "Customer Lookup  [EMPLOYEE / ADMIN MODE]\n"
        "Enter account number or customer ID to view details.\n"
        "Example query: ACC-78234 or CUST-00142\n\n"
        "Sample result:\n"
        "  Name:      Dinesh Chowdary\n"
        "  Account:   ACC-78234\n"
        "  KYC:       Verified\n"
        "  Balance:   INR 1,24,500\n"
        "  Status:    Active"
    )


def reply_report(role):
    if role == "customer":
        return "System reports are available for bank staff only."
    return (
        "Daily Report  [" + datetime.now().strftime("%d %b %Y") + "]\n"
        "  Total Transactions:    1,248\n"
        "  Total Value:           INR 3,84,56,200\n"
        "  New Accounts Opened:   23\n"
        "  Loan Applications:     14\n"
        "  Fraud Alerts:          2\n"
        "  System Uptime:         99.97%\n"
        "Full report available in the Admin Portal."
    )


def reply_system(role):
    if role == "customer":
        return "System status is available for bank staff only."
    return (
        "System Health Status\n"
        "  Core Banking:     ONLINE    99.97% uptime\n"
        "  Net Banking:      ONLINE    99.95% uptime\n"
        "  Mobile App:       ONLINE    99.91% uptime\n"
        "  ATM Network:      ONLINE    99.89% uptime\n"
        "  UPI Gateway:      ONLINE    99.99% uptime\n"
        "  Fraud Detection:  ONLINE    Active\n"
        "Last checked: " + datetime.now().strftime("%d %b %Y %H:%M:%S")
    )


def reply_help(role):
    base = (
        "BankBot AI — Available Commands\n"
        "  'hello'            Greeting and role info\n"
        "  'check balance'    View account balances\n"
        "  'transfer money'   Fund transfer options\n"
        "  'show statement'   Last 5 transactions\n"
        "  'loan info'        Loan products and rates\n"
        "  'emi calculator'   Calculate monthly EMI\n"
        "  'block card'       Block/freeze your card\n"
        "  'open account'     New account options\n"
        "  'kyc'              KYC document requirements\n"
        "  'interest rates'   Current FD/savings rates\n"
        "  'nearest atm'      ATM and branch locator\n"
        "  'report fraud'     Fraud alert and dispute\n"
        "  'net banking'      Online banking support\n"
        "  'help'             Show this menu\n"
        "  'bye'              End session\n"
    )
    if role in ("employee", "admin"):
        base += (
            "  STAFF COMMANDS:\n"
            "  'lookup customer'  Customer details\n"
            "  'system error'     Error handling guide\n"
            "  'daily report'     Transaction summary\n"
            "  'system status'    Server health check\n"
        )
    return base


def reply_thanks():
    return (
        "You're most welcome! It was a pleasure assisting you.\n"
        "Is there anything else I can help you with today?\n"
        "(Type 'help' to see all available options)"
    )


def reply_bye():
    return (
        "Thank you for banking with BankBot AI.\n"
        "Your session has been securely ended.\n"
        "Have a wonderful day! Goodbye."
    )


def tokenize(text):
    words = text.lower().strip().split()
    return [w.strip("?!.,") for w in words if w.strip("?!.,") not in FILLER]


def detect_intent(text):
    tokens = tokenize(text)
    text_lower = text.lower()

    for entry in KNOWLEDGE_BASE:
        for key in entry["keys"]:
            if " " in key and key in text_lower:
                return entry["intent"]

    for token in tokens:
        for entry in KNOWLEDGE_BASE:
            if token in entry["keys"]:
                return entry["intent"]

    return None


def get_response(user_input, role="customer"):
    intent = detect_intent(user_input)

    if intent == "greeting":     return reply_greeting(role)
    if intent == "balance":      return reply_balance(role)
    if intent == "transfer":     return reply_transfer(role)
    if intent == "statement":    return reply_statement(role)
    if intent == "loan":         return reply_loan(role)
    if intent == "emi_calc":     return reply_emi_calc()
    if intent == "block_card":   return reply_block_card(role)
    if intent == "new_account":  return reply_new_account(role)
    if intent == "kyc":          return reply_kyc(role)
    if intent == "rates":        return reply_rates(role)
    if intent == "atm":          return reply_atm(role)
    if intent == "fraud":        return reply_fraud(role)
    if intent == "net_banking":  return reply_net_banking(role)
    if intent == "error":        return reply_error(role)
    if intent == "lookup":       return reply_lookup(role)
    if intent == "report":       return reply_report(role)
    if intent == "system":       return reply_system(role)
    if intent == "help":         return reply_help(role)
    if intent == "thanks":       return reply_thanks()
    if intent == "bye":          return reply_bye()

    return (
        "I'm sorry, I didn't quite understand that.\n"
        "Here are some things you can ask me:\n"
        "  'check balance', 'transfer money', 'loan info',\n"
        "  'block card', 'report fraud', 'help'\n"
        "Type 'help' for the full list of commands."
    )


def calculate_emi(principal, annual_rate, months):
    if annual_rate == 0:
        emi = principal / months
    else:
        r = annual_rate / (12 * 100)
        emi = principal * r * (1 + r)**months / ((1 + r)**months - 1)

    total_payment  = emi * months
    total_interest = total_payment - principal
    return round(emi, 2), round(total_payment, 2), round(total_interest, 2)


def verify_login(username, password, role):
    cred = CREDENTIALS.get(role)
    if not cred:
        return False
    return username == cred["username"] and password == cred["password"]
