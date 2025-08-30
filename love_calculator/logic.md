# ❤️ Love Calculator – Python Project  

This project is a fun **Love Calculator** that combines two names and calculates a "compatibility score" based on the letters in the words **TRUE** and **LOVE**.  

---

## 🧮 How the Calculation Works  

1. **Combine the Names**  
   - Both names are joined together and converted to **uppercase**.  
   - Example:  
     ```
     name1 = "Angela Yu"
     name2 = "Jack Bauer"
     combined = "ANGELAYUJACKBAUER"
     ```

2. **Count the Letters in "TRUE"**  
   - Count how many times each letter from the word **TRUE** appears in the combined name.  
   - Example:  
     ```
     T occurs 0 times  
     R occurs 1 time  
     U occurs 2 times  
     E occurs 2 times  
     Total = 5
     ```

3. **Count the Letters in "LOVE"**  
   - Do the same for the word **LOVE**.  
   - Example:  
     ```
     L occurs 1 time  
     O occurs 0 times  
     V occurs 0 times  
     E occurs 2 times  
     Total = 3
     ```

4. **Form the Love Score**  
   - Take the first total (from **TRUE**) and the second total (from **LOVE**), then **combine them as a string**.  
   - Example:  
     ```
     First total = 5
     Second total = 3
     Love Score = "53"
     ```

---

## 🎯 Example Walkthrough  

### Input  
```python
name1 = "Angela Yu"
name2 = "Jack Bauer"
