"""
DEFINING AND CALLING FUNCTIONS
===============================
A function is a named block you can run whenever you want.
Run:  python 01_defining_and_calling.py
"""

# --- 1. def creates it, calling runs it -------------------------------------
# Defining a function does NOT run it. Nothing happens until you call it.

def greet(name,student_id):
    print(f"Record check starting for {name}")
    print(f"Checking {student_id}")

greet("fareeha","m0102994")
greet("tanuri","m902994")


# --- 3. return sends a value back out ----------------------------------------
# print() SHOWS something. return GIVES something back to use.

def add_tax(price):
    return price * 1.2

total = add_tax(100)
print(total)              # 120.0 - total holds the returned value

add_tax(100)               # this line does nothing visible - the value
                            # came back but nothing caught it


# --- 4. A function without return gives back None ---------------------------

def show(price):
    print(price)           # this SHOWS the value...

result = show(100)
print(result)              # ...but there was no return, so result is None


# --- 5. Same idea, three fields ---------------------------------------------
# One job, written once, reused for every row / line / server.

def clean(row):                                    # AI / Data Science
    return row.strip().lower()

def is_suspicious(ip):                              # Cyber Security
    return ip.startswith("10.0.0.")

def ping(host):                                     # IT
    return f"{host} is up"

for row in [" Yes ", "NO", " maybe "]:
    print(clean(row))

for ip in ["10.0.0.5", "8.8.8.8"]:
    print(ip, "->", is_suspicious(ip))

for host in ["srv-01", "srv-02"]:
    print(ping(host))

# --- TRY IT ------------------------------------------------------------------
# 1. Write a function called divider that prints a line of 34 "=" characters.
#    Call it twice.
def divider():
    print("="*34)
divider()
divider()

# 2. Write a function double(n) that RETURNS n * 2, not prints it. Store the
#    result of double(21) in a variable and print that.
def double(n):
    return n*2
answer=double(21)
print(answer)

# 3. Predict, then check: what does print(greet()) show, given greet() from
#    section 1?
#It prints a None after the function is called and executed because theres no return statement?

