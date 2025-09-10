
# 🔍 Debugging in Python with Breakpoints and Step Into

Debugging is the process of finding and fixing errors (bugs) in your code. Modern IDEs like **PyCharm**, **VS Code**, or even **IDLE** provide built-in debugging tools that make this process much easier than just using `print()` statements.

---

## 🛑 Breakpoints
A **breakpoint** is a marker you set in your code to tell the debugger:  
“Pause execution here so I can inspect what’s going on.”

- You usually set it by **clicking in the margin** (left of the line numbers) in your IDE.
- When the program reaches that line, it **stops execution**.
- At that point, you can:
  - See variable values.
  - Check the call stack.
  - Step through the code line by line.

Example in VS Code:
1. Click to the left of `new_item += items * 2` in your function.  
2. Run the debugger → execution will pause there.  
3. Inspect `new_item` and `items` in the VARIABLES panel.

---

## 👣 Step Into
When the debugger is paused, you have several stepping options:

- **Step Over** → Run the current line, but don’t go inside any function calls.  
- **Step Into** → If the current line calls a function, the debugger will go *inside* that function and let you debug it line by line.  
- **Step Out** → Finish the current function and return to the caller.

Example:
```python
def double(x):
    return x * 2

def main():
    value = 5
    result = double(value)  # <-- breakpoint here
    print(result)
```

- If you **Step Over**, execution skips into the next line (`print(result)`).
- If you **Step Into**, execution will enter the `double(x)` function so you can debug *inside* it.

---

## ✅ Why Use Breakpoints and Step Into?
- Easier than adding multiple `print()` statements.  
- Lets you see the **state of the program** at any point.  
- Helps trace logic errors and unexpected variable values.  
- Essential for debugging larger, more complex projects.

---
