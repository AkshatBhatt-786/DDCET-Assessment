from icecream import ic
from rich import print
from rich.panel import Panel
from rich.align import Align
from rich.padding import Padding
import rich.box as rich_box
from rich.console import Console
from rich.table import Table

console = Console(record=True)
ic.configureOutput(prefix="<[Chemistry]/console>: ")

data = {
    "chemical_reactions_&_equations": {
        "questions": {
            1: "What happens when milk is left at room temperature during summers?",
            2: "What is the result of exposing an iron tawa to a humid atmosphere?",
            3: "What change occurs during the fermentation of grapes?",
            4: "What happens when food is cooked?",
            5: "What is the product when magnesium burns in air?",
            6: "Why is magnesium ribbon cleaned with sandpaper before burning?",
            7: "What is the observation when magnesium ribbon burns?",
            8: "What is the nature of the change when food is digested?",
            9: "What precaution should be taken while burning a magnesium ribbon?",
            10: "What indicates a chemical reaction has occurred?",
            11: "What is the bright flame observed when magnesium burns attributed to?",
            12: "Why does milk spoil faster during summers compared to winters?",
            13: "Which of the following reactions represents the rusting of iron?",
            14: "In the activity involving magnesium ribbon, what type of reaction occurs?",
            15: "What kind of chemical change is digestion classified as?",
            16: "What type of chemical reaction is responsible for the fermentation of grapes?",
            17: "Which of the following is NOT a sign of a chemical reaction?",
            18: "What is the color of the ash formed when magnesium burns in air?",
            19: "Why is magnesium ribbon cleaned before burning in Activity 1.1?",
            20: "Which gas reacts with magnesium during its burning to form magnesium oxide?",
            21: "Which of the following is a necessary precaution during Activity 1.1?",
            22: "What kind of flame is produced during the burning of magnesium ribbon?"
        },
        "options": {
            1: [
                "It freezes",
                "It spoils",
                "It evaporates",
                "It remains unchanged"
            ],
            2: [
                "Rusting (formation of iron oxide)",
                "Iron melts",
                "Iron expands",
                "No change occurs"
            ],
            3: [
                "Sugar converts to alcohol and carbon dioxide",
                "Grapes dry up",
                "Grapes dissolve",
                "No change occurs"
            ],
            4: [
                "A chemical change occurs",
                "A physical change occurs",
                "No change occurs",
                "Only water evaporates"
            ],
            5: [
                "Magnesium chloride",
                "Magnesium hydroxide",
                "Magnesium oxide",
                "Magnesium carbonate"
            ],
            6: [
                "To break it into smaller pieces",
                "To remove the oxide layer for effective burning",
                "To polish it",
                "To make it flexible"
            ],
            7: [
                "A bright white flame and formation of white ash",
                "No change",
                "It melts",
                "It turns black"
            ],
            8: [
                "Physical change",
                "Chemical change",
                "Both physical and chemical changes",
                "No change"
            ],
            9: [
                "No precaution is needed",
                "Keep it away from eyes and wear protective eyewear",
                "Hold it with bare hands",
                "Burn it indoors"
            ],
            10: [
                "Formation of a new product",
                "Change in the identity of the substance",
                "Both a and b",
                "No change occurs"
            ],
            11: [
                "Heat produced during the reaction",
                "High reactivity of magnesium with oxygen",
                "Friction during ignition",
                "Absorption of light energy"
            ],
            12: [
                "Higher humidity in summers",
                "Bacteria multiply faster at higher temperatures",
                "Milk absorbs moisture from the air",
                "Milk reacts with sunlight"
            ],
            13: [
                "Fe + O₂ → FeO",
                "Fe + H₂O + O₂ → Fe₂O₃·xH₂O",
                "Fe + CO₂ → FeCO₃",
                "Fe + Cl₂ → FeCl₂"
            ],
            14: [
                "Combination reaction",
                "Decomposition reaction",
                "Displacement reaction",
                "Neutralization reaction"
            ],
            15: [
                "Endothermic reaction",
                "Exothermic reaction",
                "Both endothermic and exothermic",
                "Neutral reaction"
            ],
            16: [
                "Oxidation reaction",
                "Reduction reaction",
                "Anaerobic respiration",
                "Combustion reaction"
            ],
            17: [
                "Change in color",
                "Formation of precipitate",
                "Change in physical state only",
                "Emission of light"
            ],
            18: [
                "Black",
                "White",
                "Grey",
                "Red"
            ],
            19: [
                "To polish the ribbon",
                "To remove the oxide layer that prevents burning",
                "To make it flexible",
                "To increase its weight"
            ],
            20: [
                "Carbon dioxide",
                "Oxygen",
                "Hydrogen",
                "Nitrogen"
            ],
            21: [
                "Perform the activity in a closed room",
                "Use protective eyewear and maintain a safe distance",
                "Burn the ribbon using bare hands",
                "Collect ash in a metal container only"
            ],
            22: [
                "Blue flame",
                "Yellow flame",
                "Bright white flame",
                "No flame is produced"
            ]
        },
        "answer-key": {
            1: "b",
            2: "a",
            3: "a",
            4: "a",
            5: "c",
            6: "b",
            7: "a",
            8: "b",
            9: "b",
            10: "c",
            11: "b",
            12: "b",
            13: "b",
            14: "a",
            15: "c",
            16: "c",
            17: "c",
            18: "b",
            19: "b",
            20: "b",
            21: "b",
            22: "c"
        }
    }
}

# Function to load questions, options, or answers


def load_data(key):
    return data["chemical_reactions_&_equations"][key]


def chem_chapter_1():
    # Display the title panel
    title = Panel(
        "[bold][blue]Chemical Reactions & Equations[/]",
        title="Chapter 1",
        subtitle="MCQ Question Bank",
        subtitle_align="right",
        border_style="green",
    )
    console.print(title)

    # Load questions, options, and answers
    questions = load_data("questions")
    options = load_data("options")
    answers = load_data("answer-key")

    # Display questions with options in table format
    for q_no, question in questions.items():
        console.print(Padding(f"[red][bold]Que {q_no}: [/][white]{question}", pad=(1, 0, 0, 0)))

        table = Table(show_header=False, box=rich_box.HEAVY, padding=(0, 1), show_edge=True, show_lines=True)
        table.add_column("Option")
        table.add_column("Choice")
        opts = options[q_no]
        table.add_row("A", opts[0], "B", opts[1])
        table.add_row("C", opts[2], "D", opts[3])
        console.print(table)

        correct_answer = answers[q_no].upper()
        console.print(Padding(f"[green][bold]Answer: [/]{correct_answer}\n", pad=(0, 0, 1, 0)))


# Run the function to display the content
if __name__ == "__main__":
    chem_chapter_1()
