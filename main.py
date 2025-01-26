from icecream import ic
from rich import print
from rich.panel import Panel
import time
from rich.progress import track, Progress, SpinnerColumn, TextColumn, BarColumn
from worksheet1 import data
from rich.align import Align
from rich.padding import Padding
import rich.box as rich_box
from rich.console import Console
from rich.text import Text
from rich.table import Table
from pyfiglet import print_figlet, Figlet
from rich.layout import Layout
import questionary as que

console = Console(record=True)
ic.configureOutput(prefix="[DDCET-2025](_<) ")

ic("Starting App")

def load_data(key):
    return data["chemical_reactions_&_equations"][key]


def chem_chapter_1():
    questions = load_data("questions")
    options = load_data("options")
    answers = load_data("answer-key")

    title = Panel(
        Text("Chemical Reactions & Equations\nMCQ Question Bank", style="bold blue", justify="center"),
        title="[bold green]Chapter 1[/bold green]",
        border_style="magenta",
    )

    figlet = Figlet(font="starwars")
    ascii_art = figlet.renderText("ddcet")

    # Load questions, options, and answers
    console.print(Align.center(ascii_art))
    console.print(title)
    console.print(f":books: [cyan]Total Questions: [bold]{len(questions)}[/bold][/cyan]\n")
    with Progress(
            SpinnerColumn(style="bold magenta", finished_text=f"\n[bold magenta]Question {len(questions)} loaded![/bold magenta]", spinner_name="dots"),
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
    # Display questions with options in table format
    for q_no, question in questions.items():
        gradient_text = Text(f"Que {q_no}: {question}", style="bold")
        gradient_text.stylize("bold red", 0, 4)
        gradient_text.stylize("bold grey50", 4, 20)
        gradient_text.stylize("bold grey42", 20, len(gradient_text))

        # Print question with padding
        console.print(Padding(gradient_text, pad=(1, 0, 0, 0)))

        # Create and populate the options table
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

        # Highlight the correct answer
        correct_answer = answers[q_no].upper()
        correct_choice = opts["ABCD".index(correct_answer)]
        console.print(
            Padding(
                f"[green bold]Answer: [/] ({correct_answer}) {correct_choice}\n",
                pad=(0, 0, 1, 0)
            )
        )

        if int(q_no) == int(len(questions)):
            console.rule("[bold blue]:arrow_forward: Press Enter to Exit :arrow_backward:[/bold blue]")
        else:
            console.rule("[bold blue]:arrow_forward: Next Question :arrow_backward:[/bold blue]")


def main():
    figlet = Figlet(font="starwars")
    ascii_art = figlet.renderText("ddcet")
    while True:
        user_cmd =que.press_any_key_to_continue("Press Enter to Start the app")

if __name__ == "__main__":
    main()
