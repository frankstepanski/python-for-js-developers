# Python for JavaScript Developers

## How Python Thinks Differently

You'll feel at home quickly, but these will catch you:

**Indentation is syntax.** Python uses whitespace to define code blocks — there are no curly braces. This isn't just style enforcement; inconsistent indentation is a syntax error. Most editors handle this automatically, but it's a hard rule.

```python
# This is valid
def greet(name):
    if name:
        print(f"Hello, {name}")
    else:
        print("Hello, stranger")

# This will break
def greet(name):
    if name:
    print(f"Hello, {name}")  # IndentationError
```

**No `var`, `let`, or `const`.** Variables are just assigned. There's no block scoping via declaration keywords. Python has scoping rules, but they work differently — a variable assigned inside a function is local, but there's no way to signal immutability at the language level (though convention uses `UPPER_CASE` for constants).

```python
x = 10        # just assignment
x = "hello"   # still fine — Python is dynamically typed
```

**`None` instead of `null`/`undefined`.** Python has one null-like value: `None`. There's no `undefined`.

**`True`/`False` are capitalized.** Unlike JS's lowercase `true`/`false`.

**The `this` keyword doesn't exist.** In Python classes, the instance is passed explicitly as the first argument to methods, conventionally named `self`. It's verbose but unambiguous.

```python
class User:
    def __init__(self, name):
        self.name = name   # explicit, no implicit `this`

    def greet(self):
        return f"Hi, I'm {self.name}"
```

**String formatting.** f-strings are the modern approach and the closest to JS template literals:

```python
name = "Alice"
print(f"Hello, {name}")  # same idea as `Hello, ${name}`
```

**Equality.** `==` works similarly, but Python has `is` for identity comparison (reference equality). Use `==` for value comparison and `is` for checking against `None`:

```python
x = None
if x is None:   # correct
    pass
if x == None:   # works, but not idiomatic
    pass
```

## The Import System

Python's module system will feel familiar but has some quirks.

```python
import os                        # import entire module
from os import path              # import specific name
from os import path as p         # alias
import numpy as np               # aliasing is common convention in data libs
```

There's no equivalent to JS's `require()` vs `import` split — modern Python uses `import` everywhere. The `__init__.py` file in a directory makes it a package (roughly analogous to an `index.js`).

## The Environment: Why It's More Complicated Than Node

This is where most JS developers get confused, because Node's model and Python's model are meaningfully different.

**Node's model:** `npm install` puts packages in `./node_modules` in your project directory. Each project is automatically isolated. Running `node index.js` uses the local packages.

**Python's default model:** `pip install` puts packages in your *global* Python installation. Every project shares the same packages. This causes dependency conflicts instantly when two projects need different versions of the same library.

**The solution: virtual environments.** A virtual environment is a self-contained Python installation for a specific project. Think of it as `node_modules` that you have to explicitly create and activate.

```
WITHOUT venv (global mess)          WITH venv (isolated)
──────────────────────────────      ──────────────────────────────────────
  Global Python                       Project A/          Project B/
  ┌─────────────────────────┐         venv/               venv/
  │  Project A  │ Project B │        ┌─────────────┐     ┌─────────────┐
  │  needs 2.28 │ needs 2.31│        │requests 2.28│     │requests 2.31│
  └──────┬──────┴─────┬─────┘        │numpy 1.23   │     │numpy 1.24   │
         └─────┬──────┘              │flask 2.3    │     │flask 3.0    │
               ↓                     └─────────────┘     └─────────────┘
    site-packages/                   ✓ completely        ✓ completely
    requests 2.31  ← only one           isolated            isolated
    numpy 1.24        version
    flask 3.0         can exist
    ✗ conflict!
```


### Step 1: Install Python

Download Python 3 from [python.org](https://python.org). During installation on Windows, check **"Add Python to PATH"** — this is easy to miss and breaks everything if skipped.

### Step 2: Verify Installation

**Windows:**
```bash
python --version
```

**macOS/Linux:**
```bash
python3 --version
```

macOS ships with Python 2 (or a stub) at `python`, so the Python 3 binary is `python3`. If `python` doesn't work on macOS, use `python3` — nothing is broken.

### Step 3: Verify and Update pip

`pip` is Python's package manager — the equivalent of `npm`. It ships with Python automatically, so you don't install it separately. Verify it's available:

**Windows:**
```bash
pip --version
```

**macOS/Linux:**
```bash
pip3 --version
```

You should see something like:

```
pip 24.0 from /usr/local/lib/python3.12/site-packages/pip (python 3.12)
```

The output also confirms *which* Python installation pip is tied to — useful later when you're working with virtual environments and want to make sure you're using the right one.

pip often ships slightly out of date. Update it before doing anything else:

**Windows:**
```bash
python -m pip install --upgrade pip
```

**macOS/Linux:**
```bash
python3 -m pip install --upgrade pip
```

The reason for `python -m pip` instead of just `pip` is that it ensures you're running pip against the exact Python version you just verified — not some other pip that might be on your system PATH. Get into this habit early.

### Step 4: Install VS Code + Python Extension

Install [VS Code](https://code.visualstudio.com), then install the **Python extension by Microsoft** from the Extensions panel. This gives you syntax highlighting, linting, debugging, and the ability to select which Python interpreter VS Code uses.

> Some developers prefer **PyCharm**, which has strong Python-specific tooling and handles virtual environments more automatically. Either works. These instructions cover VS Code since you're likely already using it.

That's all for now — come back to VS Code after Steps 5 and 6 to point it at your virtual environment.

### Step 5: Create a Virtual Environment

In your project directory:

**macOS/Linux:**
```bash
python3 -m venv venv
```

**Windows:**
```bash
python -m venv venv
```

This creates a `venv/` folder containing a local Python binary and a local `pip`. The first `venv` is the Python module that creates virtual environments; the second `venv` is just the name of the folder — you could call it anything, but `venv` is the convention.

**Always add `venv/` to your `.gitignore`** — just like you never commit `node_modules/` in a JS project, you never commit the `venv/` folder. The reasons are the same:

- It's large and auto-generated
- It contains files compiled specifically for your OS and machine — it won't work on someone else's computer
- Anyone who clones your project can recreate it themselves by running `pip install -r requirements.txt` — requirements.txt is a plain text file that lists every package your project needs, the equivalent of `package.json`

Your `.gitignore` should include:

```
venv/
```

What you *do* commit is `requirements.txt` — that's the file that lets others recreate your exact environment. Think of it as `package.json` for Python.

### Step 6: Activate the Environment

You must activate the environment in each new terminal session. This is the step JS devs forget most often — there's no Node equivalent.

**What activation actually does**

Activating the venv temporarily rewrites your terminal's PATH so that `python` and `pip` point to the venv's local versions instead of the global ones. In practice this means:

- **`python` runs the venv's interpreter** — not whatever Python is installed globally on your machine
- **`pip install` puts packages inside `venv/lib/`** — completely isolated from other projects
- **`import` statements resolve locally** — when your script does `import requests`, Python looks inside the venv first. If you installed it while the venv was inactive, your script won't find it even though it's on your machine somewhere

Nothing is permanently changed — deactivating restores your PATH to normal. It's purely session-scoped.

**macOS/Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

Your prompt will confirm it's active:

**macOS/Linux:**
```
(venv) user@project %
```

**Windows:**
```
(venv) PS C:\Users\user\project>
```

If you don't see the `(venv)` prefix, the environment is not active and any `pip install` will go to your global Python — not your project.

> ⚠ **Rule of thumb:** Before every `pip install`, check your prompt for `(venv)`.
> No `(venv)` = wrong Python. The package will install globally and your project won't find it.
**Deactivating the environment**

When you're done, or switching to a different project:

```bash
deactivate
```

Same command on all platforms. Your prompt returns to normal, and you'll need to re-activate next time you open a terminal for this project.

### Step 7: Point VS Code at Your Virtual Environment

Now that the venv exists, tell VS Code to use it. This is the step most people skip, and it causes confusing bugs — VS Code can run your files against the global Python while your terminal uses the venv, so package imports randomly fail even though you installed them.

Open the command palette (`Ctrl+Shift+P` on Windows/Linux, `Cmd+Shift+P` on macOS), type `Python: Select Interpreter`, and choose the entry that shows `venv` in the path:

```
venv (3.14.3) ./venv/bin/python
```

Once set, VS Code remembers this per project.

> **Shortcut:** At the top of the interpreter list you'll also see **"+ Create Virtual Environment..."**. This lets you create and select a venv in one step without touching the terminal. Either approach works — the terminal method is covered here so you understand what's happening under the hood.

**Windows: auto-activate your venv in the terminal**

On Windows, VS Code's integrated terminal doesn't always activate the virtual environment automatically when you open it. To fix this, add the following to your `~/.bashrc` file (create it if it doesn't exist):

```bash
if [ -f ./venv/Scripts/activate ]; then
    source ./venv/Scripts/activate
fi
```

This checks for a `venv` folder whenever you open a terminal and activates it automatically. If you named your folder something other than `venv`, adjust the path accordingly.


### Step 8: Install Packages

`requests` is a good first install — it's the standard HTTP library for Python, and the use case maps directly to `fetch` in JS.

```bash
pip install requests
```

This installs `requests` into `venv/lib/python3.x/site-packages/` — not your project folder. When your script runs `import requests`, Python finds it there. The `import` statement doesn't copy anything into your project; it just locates the package in the venv and loads it into memory for that script's runtime.

The resolution order when you write `import requests` is:

```
import requests
       │
       ▼
┌─────────────────────┐
│  1. Built-in module?│ ── found ──→ ✓ loaded
│  (os, sys, json...) │
└─────────┬───────────┘
          │ not found
          ▼
┌─────────────────────┐
│  2. Current dir?    │ ── found ──→ ✓ loaded
│  (your project)     │
└─────────┬───────────┘
          │ not found
          ▼
┌─────────────────────────────┐
│  3. venv/lib/site-packages/ │ ── found ──→ ✓ loaded
│  ← pip install lands here   │
└─────────┬───────────────────┘
          │                   ⚠ skipped entirely if venv not activated
          │ not found
          ▼
┌─────────────────────┐
│  4. Global Python   │ ── found ──→ ✓ loaded
│  (system packages)  │
└─────────┬───────────┘
          │ not found
          ▼
   ModuleNotFoundError
```

> **See diagram above** — note the warning on step 3: if your venv isn't activated, Python skips it entirely and jumps straight to the global installation. This is why you can `pip install` a package and still get `ModuleNotFoundError` — the venv was off when you installed it, or is off now when you're running the script.

This is why activation matters — without it, step 3 points at the wrong place and Python skips your venv's packages entirely.

Try it immediately to confirm everything is working:

```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)          # 200
print(response.json()["current_user_url"])  # https://api.github.com/users/{user}
```

This is the Python equivalent of:

```javascript
const response = await fetch("https://api.github.com");
const data = await response.json();
console.log(response.status);
console.log(data.current_user_url);
```

Note that `requests` is synchronous by default — no `await` needed. For async HTTP in Python, there's `httpx`, but `requests` is the right starting point.

### Step 9: Managing Dependencies

**What is `requirements.txt`?**

`requirements.txt` is a plain text file that lists every package your project depends on with its exact version. It's the Python equivalent of `package.json` — it's what you commit to git so others can recreate your environment.

The critical difference from npm: **it is never created or updated automatically.** Unlike `package.json` which npm maintains for you, `requirements.txt` is your responsibility. You have to generate it manually and remember to update it every time you add or remove a package.

**Creating and updating it**

`pip freeze` outputs every package currently installed in your virtual environment, and `>` writes that output to a file:
```bash
pip freeze > requirements.txt
```

The resulting `requirements.txt` looks like this:
```
certifi==2024.2.2
charset-normalizer==3.3.2
idna==3.6
requests==2.31.0
urllib3==2.2.1
```

You'll notice packages you didn't install directly — those are dependencies of `requests` that pip pulled in automatically. This is the same as seeing transitive dependencies in `package-lock.json`.

> ⚠ **Run `pip freeze > requirements.txt` every time you install or remove a package.** If you forget, your `requirements.txt` will be out of sync and anyone cloning the project will get the wrong environment.

Commit `requirements.txt` to git. When someone else clones the project, they run:
```bash
pip install -r requirements.txt
```

This installs every package at the exact pinned version — equivalent to `npm ci`.

**Uninstalling packages**

This is one of the biggest behavioral differences between pip and npm, and it will catch you if you assume they work the same way.

When you install `requests`, pip also installs everything `requests` itself depends on:
```
pip install requests
           │
           └── pulls in automatically:
                 certifi==2024.2.2
                 charset-normalizer==3.3.2
                 idna==3.6
                 urllib3==2.2.1
```

When you uninstall, pip only removes what you name:
```
pip uninstall requests
           │
           └── removes: requests only
                 certifi==2024.2.2         ← orphaned, still in venv
                 charset-normalizer==3.3.2 ← orphaned, still in venv
                 idna==3.6                 ← orphaned, still in venv
                 urllib3==2.2.1            ← orphaned, still in venv
```

pip has no memory of *why* those packages were installed — it just sees a flat list of everything in your venv. It doesn't know they're now useless.

**Why npm behaves differently**

npm tracks the full dependency tree in `package-lock.json`, so it knows exactly which packages were installed *because of* another package. When you `npm uninstall`, it walks that tree and removes everything that's no longer needed.

pip has no equivalent — it only tracks what's installed, not why. That's the entire reason `pip-autoremove` exists.

| | npm | pip |
|---|---|---|
| Uninstall command | `npm uninstall requests` | `pip uninstall requests` |
| Removes the package | ✓ | ✓ |
| Removes its dependencies | ✓ automatically | ✗ by default |
| Tracks why packages were installed | ✓ `package-lock.json` | ✗ flat list only |
| Clean uninstall tool | built-in | `pip-autoremove` (third-party) |

**To uninstall a package and all its dependencies, use `pip-autoremove`:**
```bash
pip install pip-autoremove
pip-autoremove requests -y
```

The `-y` flag skips the confirmation prompt. `pip-autoremove` traces the full dependency tree and removes everything that was only installed because of `requests` — unless another package in your venv also depends on them, in which case it's smart enough to leave them alone.

After uninstalling, always re-freeze your dependencies:
```bash
pip freeze > requirements.txt
```

**Checking what's installed**
```bash
pip list
```

## Cloning an Existing Python Project

In JavaScript, the first thing you do after cloning a project is `npm install`. Python has the same concept but requires a couple of extra steps because the venv doesn't exist yet on your machine.

**The full sequence:**

```bash
# 1. Clone the project
git clone https://github.com/user/project
cd project

# 2. Create a fresh venv
python3 -m venv venv        # macOS/Linux
python -m venv venv         # Windows

# 3. Activate it
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows

# 4. Install all dependencies from requirements.txt
pip install -r requirements.txt
```

Step 4 is the Python equivalent of `npm install` — it reads `requirements.txt` and installs every package at the exact pinned version, recreating the same environment the original developer had.

**How do you know what packages to install?** You look for `requirements.txt` in the root of the project. If it's there, `pip install -r requirements.txt` handles everything. If it's missing, the project is either poorly maintained or uses a different dependency tool like `Poetry` or `Pipenv` — in that case check the README for instructions.

| JavaScript | Python |
|---|---|
| `git clone` → `npm install` | `git clone` → create venv → activate → `pip install -r requirements.txt` |
| `node_modules/` recreated automatically | `venv/` must be created manually first |
| `package.json` tells npm what to install | `requirements.txt` tells pip what to install |

> ⚠ **Don't skip creating the venv.** If you run `pip install -r requirements.txt` without activating a venv first, all the packages install globally on your machine instead of into the project.

## The Equivalent Mental Map

| JavaScript | Python |
|---|---|
| `node_modules/` | `venv/` |
| `package.json` | `requirements.txt` |
| `npm install` | `pip install` |
| `node index.js` | `python main.py` / `python3 main.py` |
| `null` / `undefined` | `None` |
| `true` / `false` | `True` / `False` |
| `===` | `==` (no strict equality needed — no type coercion) |
| Template literals | f-strings |
| `this` | `self` (explicit) |
| Arrow functions | `lambda` (limited) / `def` |

## Run Your First Script

**Before running anything, confirm your setup is complete:**
```
✓ Python 3 installed and verified (python3 --version)
✓ pip updated (python3 -m pip install --upgrade pip)
✓ VS Code + Python extension installed
✓ venv created (python3 -m venv venv)
✓ venv activated — you see (venv) in your prompt
✓ VS Code pointed at your venv (Python: Select Interpreter)
✓ requests installed (pip install requests)
✓ venv/ added to .gitignore
```

If all of the above are done, this script will work. If anything is missing, it will fail — and the error message will tell you exactly what's wrong.

**Create `main.py` in your project root — the same folder that contains `venv/`, not inside it:**
```
my-project/
├── venv/               ← Python + packages, never put your code here
├── main.py             ← create your file here
├── requirements.txt
└── .gitignore
```

**Add the following to `main.py`:**
```python
import requests

def fetch_github_user(username: str) -> dict:
    response = requests.get(f"https://api.github.com/users/{username}")
    return response.json()

def display_user(user: dict) -> None:
    print(f"Name:         {user.get('name', 'N/A')}")
    print(f"Username:     {user['login']}")
    print(f"Public repos: {user['public_repos']}")
    print(f"Followers:    {user['followers']}")
    print(f"Profile:      {user['html_url']}")

user = fetch_github_user("torvalds")
display_user(user)
```

**Run it from your project root:**
```bash
python3 main.py        # macOS/Linux
python main.py         # Windows
```

**Expected output:**
```
Name:         Linus Torvalds
Username:     torvalds
Public repos: 8
Followers:    236952
Profile:      https://github.com/torvalds
```

This script touches several things at once — a third-party import, type hints on function signatures, f-strings, dictionary access with `.get()` for safe fallbacks, and a real HTTP call to a public API. All things you'll use constantly in Python.

If you see output like the above, your entire environment is wired up correctly — Python, venv, pip, and package imports are all working.

If you get `ModuleNotFoundError: No module named 'requests'`, your venv is not activated. Run `source venv/bin/activate` (macOS/Linux) or `venv\Scripts\activate` (Windows) and try again.

---

You now have a fully working Python environment and enough context to read Python code, understand how the ecosystem differs from Node, and start building. The next module covers Python's core data structures — and how they compare to what you already know from JS.