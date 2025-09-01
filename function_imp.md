# Understanding the `return` Statement in Python

In Python, the `return` statement is used inside a function to send a value back to the caller. Once `return` is executed, the function ends, and the specified value is passed back.

---

## Example Code

```python
def function1(message):
    return message


def function2(message):
    return f"The message is  {message}"


output = function2(function1('Hello World'))
print(output)
```

---

## Step-by-Step Explanation

1. **`function1('Hello World')` is called:**

   * Inside `function1`, the parameter `message` receives the value `'Hello World'`.
   * The `return` statement sends `'Hello World'` back to the caller.

   So, `function1('Hello World')` evaluates to `'Hello World'`.

2. **`function2(function1('Hello World'))` is called:**

   * Now, `function2` receives `'Hello World'` as its argument.
   * The `return` statement in `function2` returns a formatted string: `"The message is  Hello World"`.

   So, `function2('Hello World')` evaluates to `"The message is  Hello World"`.

3. **The result is stored in `output`:**

   ```python
   output = "The message is  Hello World"
   ```

4. **`print(output)` displays:**

   ```
   The message is  Hello World
   ```

---

## Key Takeaways

* The `return` statement passes data back from a function.
* Without `return`, a function gives back `None` by default.
* Returned values can be passed as inputs to other functions.
* You can use formatted strings (`f-strings`) to build more descriptive outputs.

---

## Visual Flow

```
function1('Hello World')  →  returns 'Hello World'
function2('Hello World')  →  returns 'The message is  Hello World'
output = 'The message is  Hello World'
```

➡️ Final output on the screen: **The message is  Hello World**
