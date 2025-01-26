import os
import sys
import time
import pickle
from icecream import ic
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.align import Align
from rich.padding import Padding   
from rich.table import Table
from pyfiglet import Figlet
import rich.box as rich_box
import questionary as que
from worksheet1 import data

# Constants
APP_NAME = "React & Prepare"
GITHUB_LINK = "https://github.com/AkshatBhatt-786/React-Prep"
DEVELOPER_NAME = "Akshat S Bhatt"
TERMS_TEXT = """
Terms and Conditions

- This app is for personal and educational use only.
- Feel free to share, but credit must be given to:
  - Developer: Akshat S Bhatt
  - Idea: React & Prepare
  - GitHub Link: https://github.com/AkshatBhatt-786/React-Prep

- Commercial use is strictly prohibited.
- The developer is not liable for any outcomes resulting from app usage.
"""

# Initialize console
console = Console(record=True)

# Clear window function
def clear_window():
    """Clears the console screen based on the OS."""
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

# Load data function
def load_data(key):
    """Loads data from the worksheet."""
    return data["chemical_reactions_&_equations"][key]

# Function to display the terms and conditions
def display_terms():
    """Displays the terms and conditions in a rich panel."""
    terms_message = Panel(
        Text(TERMS_TEXT, justify="left"),
        border_style="bold yellow",
        subtitle="[cyan]React And Prepare[/cyan]",
        subtitle_align="right",
        box=rich_box.DOUBLE
    )
    console.print(terms_message, justify="center")

# Function to display the welcome message
def display_welcome():
    """Displays the welcome message with ASCII art."""
    figlet = Figlet(font="script")
    ascii_art = figlet.renderText(APP_NAME)
    console.print(Align.center(ascii_art, vertical="middle"), style="bold blue")
    
    welcome_message = Panel(
        Text(f"Welcome to {APP_NAME}\n\nPrepare smarter, react confidently, and master your MCQs!", justify="center"),
        border_style="bold green",
        box=rich_box.DOUBLE
    )
    console.print(welcome_message, justify="center")

# Function to display subject selection menu
def select_subject():
    """Prompts the user to select a subject."""
    return que.select(
        "Choose your subject:",
        choices=["Chemistry", "Physics", "Computer Science"],
        use_arrow_keys=True
    ).ask()


def display_logo_starwars():
    figlet = Figlet(font="starwars")
    ascii_art = figlet.renderText("React & Prepare")
    console.print(Align.center(ascii_art))
# Function to handle Chemi
def getResourcePath(filepath):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, filepath)
#stry questions
def handle_chemistry():
    """Handles chemistry practice logic."""
    data = None
    while True:
        chapter_selection = que.select("Choose Chemistry Chapter you want to prepare ?", choices=["Chapter 1: Chemical Reactions and Equations", "Chapter 2: Acid Bases & Salts"], instruction="Use arrow keys").ask()

        if chapter_selection == "Chapter 1: Chemical Reactions and Equations":
            filepath = getResourcePath("database\\chemistry.chemical-reaction-and-equations(v1.0).db")
            with open(filepath, "rb") as f:
                data = pickle.load(f)
                break
        if chapter_selection == "Chapter 2: Acid Bases & Salts":
            filepath = getResourcePath("database\\chemistry.acid-bases-salt(v1.0).db")
            with open(filepath, "rb") as f:
                data = pickle.load(f)
                break
        ic("Data is not available!")

    if data is None:
        ic("Data is not available!")
        return

    chapter_no = load_data("chapter")
    chapter_name = load_data("chapter-name")
    questions = load_data("questions")
    options = load_data("options")
    answers = load_data("answer-key")

    title = Panel(
        Text("Chemical Reactions & Equations\nMCQ Question Bank", style="bold blue", justify="center"),
        title=f"[bold green]Chapter {chapter_no}[/bold green]",
        border_style="magenta",
    )
    display_logo_starwars()
    console.print(title)
    console.print(f":books: [cyan]Total Questions: [bold]{len(questions)}[/bold][/cyan]\n")
    
    # Show loading progress
    with Progress(
        SpinnerColumn(style="bold magenta", spinner_name="dots"),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=None, style="bold blue", complete_style="bold green"),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        TextColumn("[bold cyan]{task.completed}/{task.total}"),
        transient=True,
        console=console
    ) as progress:
        task = progress.add_task("[cyan]Loading questions...", total=len(questions))
        for _ in questions:
            time.sleep(0.5)  # Simulate loading delay
            progress.update(task, advance=1)
    
    # Display each question and options in table format
    for q_no, question in questions.items():
        gradient_text = Text(f"Que {q_no}: {question}", style="bold red")
        gradient_text.stylize("bold grey50", 4)

        console.print(Padding(gradient_text, pad=(1, 0, 0, 0)))

        # Create and display the options table
        table = Table(
            show_header=False,

            box=rich_box.SQUARE_DOUBLE_HEAD,
            padding=(0, 2),
            show_edge=True,
            show_lines=True
        )
        table.add_column("Option", justify="center", style="bold yellow")
        table.add_column("Choice", justify="left", style="white")
        opts = options[q_no]
        table.add_row("A", opts[0])
        table.add_row("B", opts[1])
        table.add_row("C", opts[2])
        table.add_row("D", opts[3])

        console.print(table)

        # Highlight correct answer
        correct_answer = answers[q_no].upper()
        correct_choice = opts["ABCD".index(correct_answer)]
        console.print(
            Padding(
                f"[green bold]Answer: [/] ({correct_answer}) {correct_choice}\n",
                pad=(0, 0, 1, 0)
            )
        )

def display_logo():
    figlet = Figlet(font="script")
    ascii_art = figlet.renderText(APP_NAME)
    console.print(Align.center(ascii_art, vertical="middle"), style="bold blue")

def comming_soon():
    display_logo_starwars()

    coming_soon_text = Panel(
    Text("🚀 Coming Soon... Stay tuned for updates!", style="bold yellow", justify="center"),
    border_style="bold blue",
    box=rich_box.SQUARE
    ,
    padding=(1, 2)
    )
    console.print(coming_soon_text)

# Main function to run the app
def main():
    display_welcome()  # Display welcome message and ASCII art
    display_terms()  # Display terms and conditions

    # User agreement
    user_cmd = que.press_any_key_to_continue("\n▶ Press [Enter] to agree and start the app! ◀").ask()
    clear_window()

    display_logo()
    while True:
        clear_window()
        display_logo()
        subject = select_subject()  # Select subject
        if subject == "Chemistry":
            clear_window()
            handle_chemistry()  # Handle chemistry questions
        elif subject == "Physics":
            clear_window()
            comming_soon()
        elif subject == "Computer Science":
            clear_window()
            comming_soon()
    
        continue_prompt = que.select(
            "Do you want to choose another subject?",
            choices=["Yes", "No"],
            use_arrow_keys=True
        ).ask()
        
        if continue_prompt == "No":
            print("Exiting the app. Have a great day!")
            time.sleep(3)
            break

if __name__ == "__main__":
    main()
