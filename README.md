# Life Decision Simulator

This project is a decision simulator where you choose from multiple options that lead to different outcomes. It's essentially a choose your own adventure.


## Requirements

* python 3


## Installation

1. Download as a zip file or clone from github
 * git clone https://github.com/WTCSC/life-decision-simulator-DexterityB.git
2. (_Unzip if neccessary_) and open life-decision-simulator-DexterityB in the terminal
 * cd life-decision-simulator-DexterityB
3. Run decision-tree.py using python3
 * python3 decision-tree.py


## Examples

Basic usage:

```python
match scenario:
    case 0:
        print("After waking up, you check the weather. Looks like it's going to rain")
        print("Do you bring a raincoat and umbrella?")
        print("1) Yes")
        print("2) No")
        scenario = decision(1, 3)
```


Advanced usage:

```python
case 2:
    print("While you're walking, there's a flash flood, and you drown\n")
    if deaths == 3:
        scenario = 25
    else:
        print('You wake up in a cold sweat. "What just happened?!?"')
        print("Do you check the weather before your day starts?")
        print("1) Yes")
        print("2) No")
        deaths += 1
        scenario = decision(0, 4)
```


Intended flow of decisions:
[**Flow chart**](https://drive.google.com/file/d/1ePfmt6hy4Rpavh0l_nYYiSGNXTk0__7f/view?usp=sharing)


Decision function:

```python
def decision(yes, no):
    while True:
        yesno = input("")
        if yesno == "1":
            return_value = yes
            break
        elif yesno == "2":
            return_value = no
            break
    return return_value
```


## Contributing

* You can add scenarios to the match statement, using the decision function to choose which two paths the story will follow
* Use push requests


## Testing

* Just run the code using python3, and run through the code to make sure it works properly, meaning:
 * Decisions lead to the right places
 * Days advance when you reach the end of the day
 * Deaths increase when you die
 * Game ends when you die or reach the end
* Don't push if there are errors


## License

This project is not licensed


[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/iDZRBYvt)
